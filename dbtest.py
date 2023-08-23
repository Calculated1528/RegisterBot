import psycopg2

# Замените следующие параметры на ваши реальные данные
db_params = {
    "dbname": "Database",
    "user": "postgres",
    "password": "Nazi1488",
    "host": "localhost",
    "port": "5432",
}

try:
    # Установление соединения с базой данных
    # connection = psycopg2.connect(**db_params)
    connection = psycopg2.connect(dbname='Database', user='postgres', password='Nazi1488', host='localhost', port="5432")
    # Создание курсора
    cursor = connection.cursor()
    
    # Вставка данных
    # first_name = "John"
    # last_name = "Doe"
    insert_query = f"INSERT INTO custom_table VALUES ('pizza', 566);"
    # insert_query = f"SELECT * FROM users"
    # cursor.execute(insert_query)
    s = cursor.fetchall()
    # # s = cursor.fetchone()
    s = cursor.execute(insert_query)
    # s = connection.cursor().execute("INSERT INTO custom_table (name, password) VALUES ('hello', 12345678)")


    print(s)
        

    # Подтверждение изменений и закрытие курсора
    connection.commit()
    cursor.close()
    
    print("Данные успешно добавлены!")
    
except (Exception, psycopg2.Error) as error:
    print("Ошибка при работе с PostgreSQL:", error)
    
finally:
    # Закрытие соединения
    if connection:
        connection.close()





