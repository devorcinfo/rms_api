
from connectivity import py_connectivity
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
env_path = str(Path(__file__).absolute().parents[1] / "config.env")
load_dotenv(env_path)


def fn_purchase_list(request_header):
    purchases = []
    try:
        sql = (
            "select purchase_pk_id as id,name,description,qty,total_price,invoice_url,items,suppliers,DATE_FORMAT("
            "created_at,'%d %M %Y %r') as created_at,DATE_FORMAT(purchased_at,'%d %M %Y %r') as purchased_at from "
            "stc_purchase")
        result, key = py_connectivity.fetch_result_set(sql, request_header)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                purchases.append(json_data)
        return {"purchases": purchases}
    except Exception as e:
        print("fn_purchase_list " + str(e))
        return {"purchases": purchases}


def fn_add_purchase(request_header, request):
    try:
        dt = datetime.fromisoformat(request['Date'].replace("Z", "+00:00"))
        date_only = dt.date()
        py_connectivity.fetch_result_set_proc('sp_investment', (date_only, request['InvestmentPrice']), request_header)
        return {"rval": 1, "message": "Your response have been updated successfully"}
    except Exception as e:
        print("fn_add_purchase " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def check_file_type(file, file_type):
    if len(file) > 0:
        file_data = file.replace('data:' + str(file_type) + ';base64,', '')
        file_type = "." + str(file_type.split("/")[1])
        return file_data, file_type
