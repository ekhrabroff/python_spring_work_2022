from flask import Flask
from flask_restx import Api, Resource, reqparse
import psycopg

app = Flask(__name__)

@app.route("/student/list")

def get_profile():
    with psycopg.connect(f'dbname = testsystem user = testsystem password = test12345') as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM student")

            return f'<p>{cur.fetchall()}</p>'


class Student(Resource):
    def __init(self):
        pass
    #router /student/{id}
    def get(self, id):
        """ Получаем студента по его id """
        pass
    #router /student/{id}
    def post(self):
        """ Передаем изменения в json """
        pass

    # router /student/
    def put(self):
        """ Добавить студента в json """
        pass

    # router /student/{id}
    def delete(self):
        """ Удалим студента по {id}"""
        pass