import pymysql

try:
    connection = pymysql.connect(host='localhost', user='root', password='')
    print("Connection successful")
except Exception as e:
    print(f"Error: {e}")
