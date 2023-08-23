import psycopg2


class Database():
    def __init__(self, ):
        self.connect = psycopg2.connect(host="localhost", port = 5432, database="Database", user="postgres", password="Nazi1488")
        self.cursor = self.connect.cursor()
        print("Database opened successfully")


    def check_login(self, name):
        result = self.cursor.execute("SELECT * FROM users WHERE name ='{0}';".format(name))
        result2 = self.cursor.fetchone()
        
        if result2:
            print("В базе есть такой пользователь")
            return result2[1]
        else:
            return 
    
    
    def check_password(self, password):
        result = self.cursor.execute("SELECT * FROM users WHERE password = '{0}';".format(password))
        result2 = self.cursor.fetchone()

        if result2:
            print("В базе есть такой пользователь")
            return result2[2]
        else:
            return
        

    def insert(self, name, password):
        self.cursor.execute("INSERT INTO users (name, password) VALUES ('{0}', '{1}');".format(name, password))
        self.connect.commit()




