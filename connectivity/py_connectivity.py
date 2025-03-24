import mysql.connector


def get_mysql_connection():
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

    conn_string = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
    )
    return conn_string


def get_result(query):
    mysql_conn = get_mysql_connection()
    cursor_str = mysql_conn.cursor()
    cursor_str.execute(query)
    row = cursor_str.fetchall()
    field_names = [i[0] for i in cursor_str.description]
    mysql_conn.close()
    return row, field_names


def put_result(query, data):
    mysql_conn = get_mysql_connection()
    cursor_str = mysql_conn.cursor()
    cursor_str.execute(query, data)
    mysql_conn.commit()
    mysql_conn.close()
    return cursor_str.rowcount


def put_result_many(query, data):
    mysql_conn = get_mysql_connection()
    cursor_str = mysql_conn.cursor()
    cursor_str.executemany(query, data)
    mysql_conn.commit()
    mysql_conn.close()
    return cursor_str.rowcount


def exec_qry(query):
    mysql_conn = get_mysql_connection()
    cursor_str = mysql_conn.cursor()
    cursor_str.execute(query)
    mysql_conn.commit()
    mysql_conn.close()
    return cursor_str.rowcount


def call_proc(proc, params):
    mysql_conn = get_mysql_connection()
    cursor_login = mysql_conn.cursor()
    cur_res = cursor_login.callproc(proc, params)
    mysql_conn.commit()
    return cur_res



