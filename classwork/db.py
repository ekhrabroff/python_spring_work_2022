import psycopg

class DB:
    def __init__(self, database, user, passw):
        self.database = database
        self.user = user
        self.passw = passw

    def getconnect(self):
        conn = psycopg.connect(f"dbname={self.database} user={self.user} password={self.passw}")
        return conn

class Auth:
    def __init__(self, login, passw):
        self.isAuth = False
        pass

    def login(self):
        pass

    def logout(self):
        pass

    def registration(self):
        pass

class Profile:
    def __init__(self, login, passw):
        self.login = login
        self.password = passw

    def getprofile(self, conn, login):
        obj = conn.execute(f"SELECT * FROM public.user WHERE login like '{login}'")
        #print(obj.fetchall())
        return obj.fetchall()

    def setprofile(self):
        pass

class Test:
    def __init__(self):
        pass

    def get_list(self):
        pass

    def get_question(self):
        pass


class TestSystem:
    def __init__(self):
        pass

    def get_list_test(self, count_tests):
        pass


class View:
    def render(self, data):
        pass

class ListView(View):
    def render(self, data):
        pass

class QuestionView(View):
    def render(self, data):
        pass




#dbase = DB('testsystem', 'testsystem', 'test12345')


base = DB('testsystem', 'testsystem', 'test12345').getconnect()

# with base.cursor() as cur:
#     cur.execute("""SELECT * FROM profile""")
#     mass = cur.fetchall()

profile = Profile('ekhrabroff', 'qwerty12345')
profile = profile.getprofile(base,'ekhrabroff')


print(profile)


