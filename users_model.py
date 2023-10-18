from database import Database

class UserModel:
    def __init__(self) -> None:
        pass

    def transform(self, data):
        data_json = []

        for datum in data:
            data_json.append(dict(datum))

        return data_json

    def get_users(self):
        try:
            db = Database()
            connection = db.connect()

            users = connection.execute("SELECT id, name, is_active, is_rich FROM users where is_deleted = %s", 0)
        except Exception as e:
            return 'process failed'
        
        return self.transform(users)

    def get_user(self, user_id):
        db = Database()
        connection = db.connect()

        user = connection.execute("select name, is_active, is_rich from users where id = %s and is_deleted = %s", (user_id, 0))
        return self.transform(user)

    def create_user(self, data):
        db = Database()
        connection = db.connect()

        connection.execute("insert into users (name, is_active, is_rich) values (%s, %s, %s)", data['name'], data['is_active'], data['is_rich'])
        return '200'

    def update_user(self, user_id, data):
        db = Database()
        connection = db.connect()

        connection.execute("update users set name = %s, is_active = %s, is_rich = %s where id = %s", (data['name'], data['is_active'], data['is_rich'], user_id))
        return '200'

    def delete_user(self, user_id):
        db = Database()
        connection = db.connect()

        connection.execute("update users set is_deleted = %s where id = %s", (1, user_id))
        # status = connection.execute("delete from users where id = %s", user_id)

        return '200'
