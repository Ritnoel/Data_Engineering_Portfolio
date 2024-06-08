import psycopg2
connection = psycopg2.connect(dbname = "supermarket_db", user = "supermarket_user", password = "Passw0rd", host = "localhost", port = "5434")
cursor = connection.cursor()

cursor.execute("select count(*) from supermarket.sales;")


print(cursor.fetchall())