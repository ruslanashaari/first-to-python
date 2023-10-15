from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

def connect_db():
    db_username = os.getenv("DB_USERNAME")
    db_secret = os.getenv("DB_SECRET")
    db_server = os.getenv("DB_SERVER")
    db_name = os.getenv("DB_NAME")

    connnection_string = 'mysql+mysqlconnector://' + db_username + ':' + db_secret + '@' + db_server + '/' + db_name

    engine = create_engine(connnection_string)
    return engine.connect()

def transform(data):
    data_json = []

    for datum in data:
        data_json.append(dict(datum))

    return data_json

def get_users():
    try:
        connection = connect_db()

        users = connection.execute("SELECT name, is_active, is_rich FROM users where is_deleted = %s", 0)
    except:
        return 'process failed'
    
    return transform(users)

def get_user(user_id):
    connection = connect_db()

    user = connection.execute("select name, is_active, is_rich from users where id = %s and is_deleted = %s", (user_id, 0))
    return transform(user)

def create_user(data):
    connection = connect_db()

    connection.execute("insert into users (name, is_active, is_rich) values (%s, %s, %s)", data['name'], data['is_active'], data['is_rich'])
    return '200'

def update_user(user_id, data):
    connection = connect_db()

    connection.execute("update users set name = %s, is_active = %s, is_rich = %s where id = %s", (data['name'], data['is_active'], data['is_rich'], user_id))
    return '200'

def delete_user(user_id):
    connection = connect_db()

    connection.execute("update users set is_deleted = %s where id = %s", (1, user_id))
    # status = connection.execute("delete from users where id = %s", user_id)

    return '200'
