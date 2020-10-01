import MySQLdb


def connection():
    conn = MySQLdb.connect(host = "localhost",
                           user = "root",
                           passwd = "Aa@123456",
                           db = "51_finance")
    cur = conn.cursor()
    return conn, cur

conn,cur=connection()

cur.execute("CREATE TABLE IF NOT EXISTS transactions (transaction_id serial PRIMARY KEY, transaction_type VARCHAR(10),section VARCHAR(30),section_description VARCHAR(550),payment_method VARCHAR(20),payment_description VARCHAR(550),date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),gross_money_in INT(30),amount_type VARCHAR(20),percent_value INT(15),net_money_in INT(30),pending_output INT(30),money_out INT(30),loan_flag BOOLEAN DEFAULT FALSE,employee_name VARCHAR(60),user VARCHAR(30),modified_user VARCHAR(30),modified_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() )")

cur.execute("CREATE TABLE IF NOT EXISTS employee (employee_id serial PRIMARY KEY,mobile INT(20),employee_name VARCHAR(60))")

cur.execute("CREATE TABLE IF NOT EXISTS instructor (instructor_id serial PRIMARY KEY,mobile INT(20),instructor_name VARCHAR(60))")

cur.execute("CREATE TABLE IF NOT EXISTS section (section_id serial PRIMARY KEY,section VARCHAR(60))")

cur.execute("CREATE TABLE IF NOT EXISTS user (user_id serial PRIMARY KEY,username VARCHAR(20),password VARCHAR(30),name VARCHAR(20),role VARCHAR(20),age INT(20),gender VARCHAR(20))")
conn.close()
