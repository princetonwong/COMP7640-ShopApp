import pymysql

class Database:

    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.db =pymysql.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
            charset="utf8"
        )
        self.cursor = self.db.cursor()
        self.db.autocommit(value=True)

    def execute(self, query):
        try:
            print(f"{query=}")
            self.cursor.execute(query)
            # self.db.commit()
            data = self.cursor.fetchall()
            return data

        except pymysql.Error as e:
            print(e.args)
            print(e.args[0], e.args[1])
            return None