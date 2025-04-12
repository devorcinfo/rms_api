from connectivity import py_connectivity
from datetime import datetime, timedelta
from collections import defaultdict


def fn_sales(request_header, request):
    date_range = request.get('date_range')
    total_investment = 0
    total_sales = 0
    total_tax = 0
    records_grouped = []
    try:
        if date_range == 'today':
            start_date, end_date = fn_convert_date_range(date_range)
            sql = (f"SELECT sum(investment) investment,round(sum(sale_price),2) "
                   f"sale_price,sum(tax) tax FROM sales_investment_1hr where dt between '{start_date}' and '{end_date}'")
            print(sql, "---d")
            result, key = py_connectivity.fetch_result_set(sql, request_header)
            if result and len(result) > 0:
                profit_loss = result[0][1] - result[0][2] - result[0][0]
                return {"total_investment": result[0][0], "total_sales": result[0][1],
                        "total_tax": round(result[0][2], 2), "profit_loss": round(profit_loss, 2)}
        else:
            start_date, end_date = fn_convert_date_range(date_range)
            sql = f"SELECT sum(investment) investment, sum(sale_price) sale_price, round(sum(tax),2) tax FROM sales_overall where dt between '{start_date}' and '{end_date}'"
            result, key = py_connectivity.fetch_result_set(sql, request_header)
            if result and len(result) > 0:
                profit_loss = result[0][1] - result[0][2] - result[0][0]
                return {"total_investment": result[0][0], "total_sales": result[0][1],
                        "total_tax": round(result[0][2], 2), "profit_loss": round(profit_loss, 2)}
    except Exception as e:
        print("fn_sales " + str(e))
        return {"records": []}


def fn_sales_by_category(request_header, request):
    date_range = request.get('date_range')
    records_grouped = []
    try:
        if date_range == 'today':
            sql = ("with a as (select otype, sum(grand_total) tot from orders where created_at between concat("
                   "current_date(),' 00:00:00') and current_timestamp() group by otype), b as (select sum("
                   "grand_total) as all_tot from orders where created_at between concat(current_date(),' 00:00:00') "
                   "and current_timestamp()) select ot.type_name category, ifnull(a.tot,0) as tot_price, "
                   "case when ifnull(a.tot,0)=0 then 0 else round((ifnull(a.tot,0)/all_tot)*100,2) end as perc from "
                   "order_types ot left join a on a.otype=ot.type_id left join b on 1=1")
            print(sql)
            result, key = py_connectivity.fetch_result_set(sql, request_header)
            if result and len(result) > 0:
                for row in result:
                    data = dict(zip(key, row))
                    records_grouped.append(data)
        else:
            start_date, end_date = fn_convert_date_range(date_range)
            sql = (f"WITH cte AS ("
                   f"  SELECT SUM(tot_price) AS tot "
                   f"  FROM sales_by_category "
                   f"  WHERE dt BETWEEN '{start_date}' AND '{end_date}'"
                   f") "
                   f"SELECT s.category, "
                   f"       SUM(s.tot_price) AS tot_price, "
                   f"       ROUND((SUM(s.tot_price) / cte.tot) * 100, 2) AS perc "
                   f"FROM sales_by_category s "
                   f"JOIN cte ON 1=1 "
                   f"WHERE s.dt BETWEEN '{start_date}' AND '{end_date}' "
                   f"GROUP BY s.category, cte.tot")
            result, key = py_connectivity.fetch_result_set(sql, request_header)
            if result and len(result) > 0:
                for row in result:
                    data = dict(zip(key, row))
                    records_grouped.append(data)
        return {"records": records_grouped}
    except Exception as e:
        print("fn_sales_by_category " + str(e))
        return {"records": []}


def fn_sales_by_items(request_header, request):
    date_range = request.get('date_range')
    records_grouped = []
    try:
        if date_range == 'today':
            sql = ("with a as (select sum(price) as tot from order_items where dt between concat(current_date(),"
                   "' 00:00:00') and current_timestamp()) SELECT o.dish_name as items, SUM(o.price) AS price, "
                   "SUM(o.qty) as qty, round((sum(o.price)/a.tot)*100,2) perc FROM order_items o left join a on "
                   "1=1 where o.dt between concat(current_date(),' 00:00:00') and current_timestamp() GROUP BY "
                   "o.dish_name, a.tot ORDER BY price DESC LIMIT 5")
            result, key = py_connectivity.fetch_result_set(sql, request_header)
            if result and len(result) > 0:
                for row in result:
                    data = dict(zip(key, row))
                    records_grouped.append(data)
        else:
            start_date, end_date = fn_convert_date_range(date_range)
            sql = (f"WITH cte AS ("
                   f"  SELECT SUM(price) AS tot "
                   f"  FROM sales_by_items "
                   f"  WHERE dt BETWEEN '{start_date}' AND '{end_date}'"
                   f") "
                   f"SELECT c.items, "
                   f"       SUM(c.price) AS price, "
                   f"       SUM(c.qty) AS qty, "
                   f"       ROUND((SUM(c.price) / cte.tot) * 100, 2) AS perc "
                   f"FROM sales_by_items c "
                   f"JOIN cte ON 1=1 "
                   f"WHERE c.dt BETWEEN '{start_date}' AND '{end_date}' "
                   f"GROUP BY c.items, cte.tot "
                   f"ORDER BY price DESC "
                   f"LIMIT 5")
            result, key = py_connectivity.fetch_result_set(sql, request_header)
            if result and len(result) > 0:
                for row in result:
                    data = dict(zip(key, row))
                    records_grouped.append(data)
        return {"records": records_grouped}
    except Exception as e:
        print("fn_sales_by_items " + str(e))
        return {"records": []}


def fn_convert_date_range(date_string):
    start_date = ''
    end_date = ''
    today = datetime.today()
    if date_string == 'today':
        # Today's date
        start_date = today
        end_date = today
    elif date_string == 'yesterday':
        # Yesterday's date
        start_date = today - timedelta(days=1)
        end_date = today - timedelta(days=1)
    elif date_string == 'last7days':
        # Last 7 days
        start_date = today - timedelta(days=7)
        end_date = today
    elif date_string == 'last30days':
        # Last 30 days
        start_date = today - timedelta(days=30)
        end_date = today
    elif date_string == 'thismonth':
        # Start and end date of this month
        start_date = today.replace(day=1)
        end_date = today
    elif date_string == 'lastmonth':
        # Start and end date of last month
        first_day_of_current_month = today.replace(day=1)
        last_day_of_last_month = first_day_of_current_month - timedelta(days=1)
        start_date = last_day_of_last_month.replace(day=1)
        end_date = last_day_of_last_month
    start_date = start_date.strftime('%Y-%m-%d') + ' 00:00:00'
    end_date = end_date.strftime('%Y-%m-%d') + ' 23:59:59'
    return start_date, end_date
