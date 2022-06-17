from flask import Flask
import psycopg

app = Flask(__name__)

@app.route("/list")
def hello_world():
    out = ''
    with psycopg.connect('dbname = testsystem user = testsystem password = test12345') as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM student')
            for i in cur.fetchall():
               out += f'<li>{i[2]} {i[3]}</li>\n'
    return f"""<h3>Список студентов</h3>
                <ol>{out}</ol>"""