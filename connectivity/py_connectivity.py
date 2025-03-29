

def fetch_result_set(query, request_header):
    try:
        with request_header.app.mysql_pool.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            row = cursor.fetchall()
            field_names = [i[0] for i in cursor.description]
    except Exception as e:
        print("fetch_result_set ", str(e))
    return row, field_names


def fetch_result_set_proc(proc_name, params, request_header):
    try:
        with request_header.app.mysql_pool.get_connection() as connection:
            cursor = connection.cursor()
            result = cursor.callproc(proc_name, params)
            connection.commit()
    except Exception as e:
        print("fetch_result_set_proc ", str(e))
    return result


def exec_qry(query, request_header):
    with request_header.app.mysql_pool.get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
    return cursor.rowcount


def put_result(query, data, request_header):
    with request_header.app.mysql_pool.get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        connection.close()
    return cursor.rowcount