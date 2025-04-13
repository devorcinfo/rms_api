import json
import uvicorn
from fastapi import FastAPI, Request, HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware
from mysql.connector import pooling, Error
from auth import py_jwt
from contextlib import asynccontextmanager


def initialize_connection_pool() -> None:
    try:
        MYSQL_HOST = '103.235.105.148'
        MYSQL_USER = 'root'
        MYSQL_PASSWORD = 'F199gDmr}qf@bZ{r'
        MYSQL_PORT = '3306'
        MYSQL_DB = 'rms'
        # MYSQL_HOST = '127.0.0.1'
        # MYSQL_USER = 'root'
        # MYSQL_PASSWORD = 'root'
        # MYSQL_PORT = '3306'
        # MYSQL_DB = 'rms'
        app.mysql_pool = pooling.MySQLConnectionPool(
            pool_name="rms_pool",
            pool_size=5,
            host=MYSQL_HOST,
            port=int(MYSQL_PORT),
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB,
            pool_reset_session=True
        )
    except Error as e:
        print("initialize_connection_pool", str(e))


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("db---start")
    initialize_connection_pool()
    yield
    initialize_connection_pool(app)


app = FastAPI(lifespan=lifespan)
origins = ["*"]
from app import route

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"Info": "In live"}


@app.get("/rms/")
async def index():
    return {"Info": "In live"}


# Admin Apis
@app.post("/rms/admin/login")
async def admin_login(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.admin_login(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in admin_login: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/meal_type")
async def meal_type(request_header: Request):
    try:
        response = route.meal_type(request_header)
        return response
    except Exception as e:
        print("Exception in meal_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/filters/add_meal_type")
async def add_meal_type(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.add_meal_type(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in add_meal_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/filters/delete_dishtype")
async def delete_dishtype(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.delete_dishtype(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in delete_dishtype: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/dish_type")
async def dish_type(request_header: Request):
    try:
        response = route.dish_type(request_header)
        return response
    except Exception as e:
        print("Exception in dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/dish_type1")
async def dish_type1(request_header: Request):
    try:
        response = route.dish_type1(request_header)
        return response
    except Exception as e:
        print("Exception in dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/filters/add_dish_type")
async def add_dish_type(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.add_dish_type(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in add_dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/count_dishtype_items")
async def count_dishtype_items(request_header: Request, data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.count_dishtype_items(request_header, request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in add_dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/printer")
async def printer(request_header: Request):
    try:
        response = route.printer(request_header)
        return response
    except Exception as e:
        print("Exception in dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/reference")
async def reference(request_header: Request):
    try:
        response = route.reference(request_header)
        return response
    except Exception as e:
        print("Exception in dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/percentage")
async def percentage(request_header: Request):
    try:
        response = route.percentage(request_header)
        return response
    except Exception as e:
        print("Exception in dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/weight_type")
async def weight_type(request_header: Request):
    try:
        response = route.weight_type(request_header)
        return response
    except Exception as e:
        print("Exception in dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/get_bluetooth_config")
async def get_bluetooth_config(request_header: Request):
    try:
        response = route.get_bluetooth_config(request_header)
        return response
    except Exception as e:
        print("Exception in dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/hall")
async def hall(request_header: Request):
    try:
        response = route.hall(request_header)
        return response
    except Exception as e:
        print("Exception in hall: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/dish/dish_items")
async def dish_items(request_header: Request, data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.dish_items(request_header, request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in dish_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/dish/dish_items1")
async def dish_items1(request_header: Request, data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.dish_items1(request_header, request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in dish_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/dish/dish_items_user")
async def dish_items_user(request_header: Request, data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.dish_items_user(request_header, request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in dish_items_user: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/dish/manage")
async def dish_manage(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.dish_manage(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in dish_manage: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/dish/delete")
async def dish_delete(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.dish_delete(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in dish_delete: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/dish/status")
async def dish_status(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.dish_status(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in dish_status: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/dish/qty_update")
async def qty_update(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.qty_update(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in qty_update: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/users/user_list")
async def user_list(request_header: Request):
    try:
        response = route.user_list(request_header)
        return response
    except Exception as e:
        print("Exception in dish_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/users/prv_lst")
async def prv_lst(request_header: Request):
    try:
        response = route.prv_lst(request_header)
        return response
    except Exception as e:
        print("Exception in dish_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/users/manage")
async def user_manage(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.user_manage(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in user_manage: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/users/delete")
async def user_delete(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.user_delete(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in user_delete: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/users/status")
async def user_status(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.user_status(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in user_status: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/orders/order_types")
async def order_types(request_header: Request):
    try:
        response = route.order_types(request_header)
        return response
    except Exception as e:
        print("Exception in order_types: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/orders/order_stat")
async def order_stat(request_header: Request):
    try:
        response = route.order_stat(request_header)
        return response
    except Exception as e:
        print("Exception in order_status: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/orders/take_order")
async def take_order(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.take_order(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in take_order: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/orders/take_order1")
async def take_order(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.take_order(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in take_order: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/orders/add_order_items")
async def add_order_items(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.add_order_items(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in add_order_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/orders/running_orders")
async def running_orders(request_header: Request):
    try:
        response = route.running_orders(request_header)
        return response
    except Exception as e:
        print("Exception in running_orders: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/dish/dishtype_temp_delete")
async def dishtype_temp_delete(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.dishtype_temp_delete(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in qty_update: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/dash/dash_nav")
async def dash_nav(request_header: Request):
    try:
        response = route.dash_nav(request_header)
        return response
    except Exception as e:
        print("Exception in running_orders: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/orders/running_orderitems")
async def running_orderitems(request_header: Request, data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.running_orderitems(request_header, request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in running_orderitems: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/orders/order_complete")
async def order_status(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.order_complete(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in order_complete: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/orders/remove_items")
async def remove_items(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.remove_items(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in remove_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/orders/cancel_order")
async def cancel_order(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.cancel_order(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in cancel_order: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/orders/reprint_bill")
async def reprint_bill(request_header: Request, data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.reprint_bill(request_header, request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in reprint_bill: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/report/order_report")
async def order_report(request_header: Request, data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.order_report(request_header, request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in order_report: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/report/order_report_items")
async def order_report_items(request_header: Request, data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.order_report_items(request_header, request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in order_report_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/report/dish_report")
async def dish_report(request_header: Request, data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.dish_report(request_header, request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in dish_report: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/counters/counter_details")
async def counter_details(request_header: Request, data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.counter_details(request_header, request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in counter_details: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/counters/hall_details")
async def hall_details(request_header: Request):
    try:
        response = route.hall_details(request_header)
        return response
    except Exception as e:
        print("Exception in counter_details: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/counter/counter_manage")
async def counter_manage(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.counter_manage(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in counter_manage: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/counter/counter_delete")
async def counter_delete(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.counter_delete(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in counter_delete: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/counter/counter_delete")
async def counter_delete(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.counter_delete(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in counter_delete: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/purchase/suppliers")
async def suppliers(request_header: Request):
    try:
        response = route.suppliers(request_header)
        return response
    except Exception as e:
        print("Exception in suppliers: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/purchase/manage_suppliers")
async def manage_suppliers(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.manage_suppliers(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in manage_suppliers: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/purchase/items")
async def items(request_header: Request):
    try:
        response = route.items(request_header)
        return response
    except Exception as e:
        print("Exception in items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/purchase/manage_items")
async def manage_items(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.manage_items(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in manage_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/purchase/category")
async def category(request_header: Request):
    try:
        response = route.category(request_header)
        return response
    except Exception as e:
        print("Exception in items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/purchase/manage_category")
async def manage_category(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.manage_category(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in manage_category: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/purchase/list")
async def purchase_list(request_header: Request):
    try:
        response = route.purchase_list(request_header)
        return response
    except Exception as e:
        print("Exception in purchase_list: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/purchase/add")
async def add_purchase(request_header: Request):
    try:
        data = await request_header.json()
        if data is not None:
            response = route.add_purchase(request_header, data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in manage_category: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/dashboard/get_sales_stats")
async def get_sales_stats(request_header: Request, data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.sales(request_header, request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in get_sales_stats: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/dashboard/sales_by_category")
async def sales_by_category(request_header: Request, data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.sales_by_category(request_header, request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in sales_by_category: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/dashboard/sales_by_items")
async def sales_by_items(request_header: Request, data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.sales_by_items(request_header, request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in sales_by_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8066)
