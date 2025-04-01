from counter import py_counter
from dashboard import py_dashboard
from dish import py_dish
from login import py_login
from filters import py_filters
from orders import py_order
from purchase import py_purchase
from report import py_report
from users import py_user


def admin_login(request_header, request):
    response = py_login.fn_admin_login(request_header, request)
    return response


def meal_type(request_header,):
    response = py_filters.fn_meal_type(request_header,)
    return response


def add_meal_type(request_header,request):
    response = py_filters.fn_add_meal_type(request_header,request)
    return response


def delete_dishtype(request_header,request):
    response = py_filters.fn_delete_dishtype(request_header,request)
    return response


def dish_type(request_header,):
    response = py_filters.fn_dish_type(request_header,)
    return response


def dish_type1(request_header,):
    response = py_filters.fn_dish_type1(request_header,)
    return response


def add_dish_type(request_header,request):
    response = py_filters.fn_add_dish_type(request_header,request)
    return response


def count_dishtype_items(request_header,request):
    response = py_filters.fn_count_dishtype_items(request_header,request)
    return response


def printer(request_header,):
    response = py_filters.fn_printer(request_header,)
    return response


def reference(request_header,):
    response = py_filters.fn_reference(request_header,)
    return response


def percentage(request_header,):
    response = py_filters.fn_percentage(request_header,)
    return response


def hall(request_header,):
    response = py_filters.fn_hall(request_header,)
    return response


def dish_items(request_header,request):
    response = py_dish.fn_dish_items(request_header,request)
    return response


def dish_items1(request_header,request):
    response = py_dish.fn_dish_items1(request_header,request)
    return response


def dish_items_user(request_header,request):
    response = py_dish.fn_dish_items_user(request_header,request)
    return response


def dish_manage(request_header,request):
    response = py_dish.fn_dish_manage(request_header,request)
    return response


def dish_delete(request_header,request):
    response = py_dish.fn_dish_delete(request_header,request)
    return response


def dish_status(request_header,request):
    response = py_dish.fn_dish_status(request_header,request)
    return response


def qty_update(request_header,request):
    response = py_dish.fn_qty_update(request_header,request)
    return response


def user_list(request_header,):
    response = py_user.fn_user_list(request_header,)
    return response


def user_manage(request_header,request):
    response = py_user.fn_user_manage(request_header,request)
    return response


def user_delete(request_header,request):
    response = py_user.fn_user_delete(request_header,request)
    return response


def user_status(request_header,request):
    response = py_user.fn_user_status(request_header,request)
    return response


def prv_lst(request_header,):
    response = py_user.fn_prv_lst(request_header,)
    return response


def order_types(request_header,):
    response = py_order.fn_order_types(request_header,)
    return response


def order_stat(request_header,):
    response = py_order.fn_order_stat(request_header,)
    return response


def weight_type(request_header,):
    response = py_filters.get_weight_type(request_header,)
    return response


def get_bluetooth_config(request_header,):
    response = py_filters.get_bluetooth_config(request_header,)
    return response


def take_order(request_header,request):
    response = py_order.fn_take_order(request_header,request)
    return response


def add_order_items(request_header,request):
    response = py_order.fn_add_order_items(request_header,request)
    return response


def running_orders(request_header,):
    response = py_order.fn_running_orders(request_header,)
    return response


def dash_nav(request_header,):
    response = py_order.fn_dash_nav(request_header,)
    return response


def dishtype_temp_delete(request_header,request):
    response = py_dish.fn_dishtype_temp_delete(request_header,request)
    return response


def running_orderitems(request_header,request):
    response = py_order.fn_running_orderitems(request_header,request)
    return response


def order_complete(request_header,request):
    response = py_order.fn_order_complete(request_header,request)
    return response


def remove_items(request_header,request):
    response = py_order.fn_remove_items(request_header,request)
    return response


def cancel_order(request_header,request):
    response = py_order.fn_cancel_order(request_header,request)
    return response


def order_report(request_header,request):
    response = py_report.fn_order_report(request_header,request)
    return response


def reprint_bill(request_header,request):
    response = py_order.fn_reprint_bill(request_header,request)
    return response


def order_report_items(request_header,request):
    response = py_report.fn_order_report_items(request_header,request)
    return response


def dish_report(request_header,request):
    response = py_report.fn_dish_report(request_header,request)
    return response


def counter_details(request_header,request):
    response = py_counter.fn_counter_details(request_header,request)
    return response


def hall_details(request_header,):
    response = py_counter.fn_hall_details(request_header,)
    return response


def counter_manage(request_header,request):
    response = py_counter.fn_counter_manage(request_header,request)
    return response


def counter_delete(request_header,request):
    response = py_counter.fn_counter_delete(request_header,request)
    return response


def purchase_list(request_header,):
    response = py_purchase.fn_purchase_list(request_header,)
    return response


def add_purchase(request_header,request):
    response = py_purchase.fn_add_purchase(request_header,request)
    return response


def sales(request_header,request):
    response = py_dashboard.fn_sales(request_header,request)
    return response


def sales_by_category(request_header,request):
    response = py_dashboard.fn_sales_by_category(request_header,request)
    return response


def sales_by_items(request_header,request):
    response = py_dashboard.fn_sales_by_items(request_header,request)
    return response