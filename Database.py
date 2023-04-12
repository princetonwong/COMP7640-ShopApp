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

    # Shortcut for execute
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

    # Initiate mock data from group57_insert_sql.txt
    def initiateMockData(self):
        with open("group57_insert_sql.txt", "r") as f:
            content = f.read()
            # self.execute(content)
            sqlCommands = content.split(';')
            for command in sqlCommands:
                try:
                    self.execute(command)
                except Exception as msg:
                    print("Command skipped: ", msg)
        print("Mock data initiated")


if __name__ == "__main__":
    db = Database(
        user="root",
        password="my-secret-pw",
        host="139.59.124.127",
        port=3306,
        database="SHOPAPP"
    )
    db.initiateMockData()
