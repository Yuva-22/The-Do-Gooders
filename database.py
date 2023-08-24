import mysql.connector

host = "localhost"
user = "root"
password = ""
database_name = "NGO"   
table_name = "DONATIONS"

def createDB():
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        cursor = connection.cursor()
        check_query = f"SHOW DATABASES LIKE '{database_name}'"

        cursor.execute(check_query)
        result = cursor.fetchone()

        if not result:
            create_query = f"CREATE DATABASE {database_name}"
            cursor.execute(create_query)
            print(f"The '{database_name}' database has been created.")
        else:
            print(f"The '{database_name}' database already exists.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
        return True
    
def createTable():
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )

        cursor = connection.cursor()

        check_query = f"SHOW TABLES LIKE '{table_name}'"

        cursor.execute(check_query)

        result = cursor.fetchone()

        if not result:
            create_table_query = f"""
            CREATE TABLE {table_name} (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                PERSON_NAME VARCHAR(100),
                ORGANIZATION VARCHAR(100),
                CONTACT VARCHAR(12),
                EMAIL VARCHAR(100),
                FOOD_QUANTITY VARCHAR(100),
                CHARITY_NAME VARCHAR(100),
                TRANSPORT VARCHAR(20),
                NGO_MEMBER VARCHAR(5)
            )
            """
            cursor.execute(create_table_query)
            print(f"The '{table_name}' table has been created in the '{database_name}' database.")
        else:
            print(f"The '{table_name}' table already exists in the '{database_name}' database.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def fetchData():
    connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )

    cursor = connection.cursor()
    check_query = f"SELECT * FROM {table_name}"

    cursor.execute(check_query)

    result = cursor.fetchall()
    print(result)
    
    if (len(result) == 0):
        print("No data found")
        return []
    else:
        return result
    