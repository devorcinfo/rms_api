from connectivity import py_connectivity


def fn_dish_items(request_header, request):
    dish_item = []
    meal_type = request.get("meal_type")
    dish_type = request.get("dish_type")
    try:
        sql = ("select dish_id as id,dish_name,price,including_tax,DATE_FORMAT(created_at, '%d %M %Y %r') as "
               "created_at,DATE_FORMAT(updated_at, '%d %M %Y') as updated_at,type_id,type_name,category_id,"
               "category_name,printer_id,printer_name,status,dish_id,kot,avail_qty,swiggy_price,zomato_price,weight_fk,is_show from "
               "v_dish_items where 1=1 and status = 1")
        if meal_type:
            sql = sql + " and meal_id=" + str(meal_type)
        if dish_type:
            sql = sql + " and type_id=" + str(dish_type)
        result, key = py_connectivity.fetch_result_set(sql,request_header)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                dish_item.append(json_data)
        return {"dish_item": dish_item}
    except Exception as e:
        print("fn_dish_items " + str(e))
        return {"dish_item": dish_item}


def fn_dish_items1(request_header, request):
    dish_item = []
    meal_type = request.get("meal_type")
    dish_type = request.get("dish_type")
    try:
        sql = ("select dish_id as id,dish_name,price,including_tax,DATE_FORMAT(created_at, '%d %M %Y %r') as "
               "created_at,DATE_FORMAT(updated_at, '%d %M %Y') as updated_at,type_id,type_name,category_id,"
               "category_name,printer_id,printer_name,status,dish_id,kot,avail_qty,swiggy_price,zomato_price,weight_fk,is_show from "
               "v_dish_items where 1=1")
        if meal_type:
            sql = sql + " and meal_id=" + str(meal_type)
        if dish_type:
            sql = sql + " and type_id=" + str(dish_type)
        result, key = py_connectivity.fetch_result_set(sql, request_header)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                dish_item.append(json_data)
        return {"dish_item": dish_item}
    except Exception as e:
        print("fn_dish_items " + str(e))
        return {"dish_item": dish_item}


def fn_dish_items_user(request_header, request):
    dish_item = []
    order_type = request.get("order_type")
    try:
        sql = ("select dish_id as id,dish_name,price,including_tax,created_at,updated_at,type_id,type_name,category_id,"
               "category_name,printer_id,printer_name,status,dish_id,kot,avail_qty,swiggy_price,zomato_price,weight_fk,is_show from "
               "v_dish_items where status=1")
        result, key = py_connectivity.fetch_result_set(sql, request_header)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                if str(order_type) == '3':
                    json_data['price'] = json_data['swiggy_price']
                if str(order_type) == '4':
                    json_data['price'] = json_data['zomato_price']
                dish_item.append(json_data)
        return {"dish_item": dish_item}
    except Exception as e:
        print("fn_dish_items " + str(e))
        return {"dish_item": dish_item}


def fn_dish_manage(request_header, request):
    dish_id = request.get("dish_id")
    dish_name = request.get("dish_name")
    price = request.get("price")
    s_price = request.get("swiggy_price")
    z_price = request.get("zomato_price")
    category = request.get("category_id")
    dish_type = request.get("type_id")
    printer_type = request.get("printer_id")
    including_tax = request.get("including_tax")
    kot = request.get("kot")
    weight_fk = request.get("weight_fk")
    is_show = request.get("is_show")
    try:
        result = py_connectivity.fetch_result_set_proc('sp_dish_inup', (
        dish_id, dish_name, price, dish_type, category, printer_type, including_tax, kot, s_price, z_price, weight_fk,is_show, None), request_header)
        if result[-1] > 0:
            return {"val": 1, "message": "Your response have been updated successfully"}
        else:
            return {"val": 0, "message": "Dish Already Having!"}

    except Exception as e:
        print("fn_dish_manage " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def fn_dish_delete(request_header, request):
    dish_id = request.get("dish_id")
    try:
        result = py_connectivity.fetch_result_set_proc('sp_dish_del', (dish_id, None), request_header)
        return {"val": 1, "message": "Item have been removed successfully"}
    except Exception as e:
        print("fn_dish_delete " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def fn_dish_status(request_header, request):
    dish_id = request.get("dish_id")
    status = request.get("status")
    try:
        sql = f"update dish_items set status={status}  where dish_id={dish_id}"
        result = py_connectivity.exec_qry(sql, request_header)
        return {"val": 1, "message": "Item status have been updated successfully"}
    except Exception as e:
        print("fn_dish_status " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def fn_qty_update(request_header, request):
    dish_id = request.get("dish_id")
    qty = request.get("qty")
    try:
        sql = f"update dish_items set avail_qty={qty}  where dish_id={dish_id}"
        result = py_connectivity.exec_qry(sql, request_header)
        return {"val": 1, "message": "Item quantity have been updated successfully"}
    except Exception as e:
        print("fn_qty_update " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def fn_dishtype_temp_delete(request_header, request):
    type_id = request.get("type_id")
    status = request.get("status")
    try:
        sql = f"update dish_types set is_active= {status} where type_id={type_id}"
        result = py_connectivity.exec_qry(sql, request_header)
        return {"val": 1, "message": "Status have been updated successfully"}
    except Exception as e:
        print("fn_dishtype_temp_delete " + str(e))
        return {"val": 0, "message": "Something went wrong"}