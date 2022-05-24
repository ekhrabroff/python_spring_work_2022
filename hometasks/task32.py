# todo: Написать скрипт создания базы данных(ER-модели) TestSystem
# Скрипт  create_db.py  должен создавать таблицы, индексы , констрейнты в СУБД PostgresSQL
# В задании использовать библиотеку psycopg


# Ссылка на документацию
# https://www.psycopg.org/psycopg3/docs/basic/usage.html
# Для подключения использовать пользователя и базу отличную от postgres


import psycopg

with psycopg.connect('dbname=testsystem user=testsystem password=test12345') as conn:
    with conn.cursor() as cur:
        # создаем таблицы
        cur.execute("""
            CREATE TABLE "group" (
            "id_group" SERIAL PRIMARY KEY,
            "name" VARCHAR(256) UNIQUE NOT NULL);

            CREATE TABLE "student" (
            "id_student" SERIAL PRIMARY KEY,
            "id_group" INTEGER NOT NULL,
            "name" VARCHAR(256) NOT NULL,
            "surname" VARCHAR(256) NOT NULL,
            "age" INTEGER,
            "tel" INTEGER UNIQUE,
            "id_result" INTEGER NOT NULL);

            CREATE TABLE "result" (
            "id_result" SERIAL PRIMARY KEY,
            "status" BOOLEAN,
            "tm_result" TIME);

            CREATE TABLE "questions" (
            "id_question" SERIAL PRIMARY KEY,
            "id_result" INTEGER NOT NULL,
            "text_question" VARCHAR(256) NOT NULL);

            CREATE TABLE "answer" (
            "id_answer" SERIAL PRIMARY KEY,
            "id_questions" INTEGER NOT NULL,
            "id_result" INTEGER NOT NULL,
            "name_answer" VARCHAR(256) NOT NULL);

            CREATE TABLE "test" (
            "id_test" SERIAL PRIMARY KEY,
            "theme" VARCHAR(256) NOT NULL,
            "dt_test" DATE,
            "tm_test" TIME,
            "test_pass" BOOLEAN,
            "id_result" INTEGER NOT NULL);

            CREATE TABLE "student_test" (
            "id_student_test" SERIAL PRIMARY KEY,
            "id_student" INTEGER NOT NULL,
            "id_test" INTEGER NOT NULL,
            "dt_create" TIMESTAMP);

            CREATE TABLE "test_question" (
            "id_test_question" SERIAL PRIMARY KEY,
            "id_test" INTEGER NOT NULL,
            "id_questions" INTEGER NOT NULL);

            CREATE TABLE "user" (
            "id_user" SERIAL PRIMARY KEY,
            "login" VARCHAR(256) UNIQUE,
            "password" VARCHAR(256) NOT NULL,
            "dt_create" DATE);

            CREATE TABLE "profile" (
            "id_profile" SERIAL PRIMARY KEY,
            "id_user" INTEGER NOT NULL,
            "id_student" INTEGER NOT NULL,
            "name" VARCHAR(256) NOT NULL,
            "surname" VARCHAR(256) NOT NULL,
            "patronymic" VARCHAR(256) NOT NULL,
            "dt_birth" DATE,
            "tel" INTEGER UNIQUE,
            "avatar" VARCHAR(256))
            """)
        # создаем индексы
        cur.execute("""
            CREATE INDEX "idx_answer__id_questions" ON "answer" ("id_questions");
            CREATE INDEX "idx_answer__id_result" ON "answer" ("id_result");
            CREATE INDEX "idx_student__id_group" ON "student" ("id_group");
            CREATE INDEX "idx_student__id_result" ON "student" ("id_result");
            CREATE INDEX "idx_test__id_result" ON "test" ("id_result");
            CREATE INDEX "idx_student_test__id_student" ON "student_test" ("id_student");
            CREATE INDEX "idx_student_test__test" ON "student_test" ("id_test");
            CREATE INDEX "idx_test_question__id_questions" ON "test_question" ("id_questions");
            CREATE INDEX "idx_test_question__id_test" ON "test_question" ("id_test");
            CREATE INDEX "idx_profile__id_student" ON "profile" ("id_student");
            CREATE INDEX "idx_profile__user" ON "profile" ("id_user");
            """)
        # создаем констрейны
        cur.execute("""
            ALTER TABLE "questions" ADD CONSTRAINT "fk_questions__id_result" FOREIGN KEY ("id_result")
            REFERENCES "result" ("id_result") ON DELETE RESTRICT;

            ALTER TABLE "answer" ADD CONSTRAINT "fk_answer__id_questions" FOREIGN KEY ("id_questions")
            REFERENCES "questions" ("id_question") ON DELETE RESTRICT;

            ALTER TABLE "answer" ADD CONSTRAINT "fk_answer__id_result" FOREIGN KEY ("id_result")
            REFERENCES "result" ("id_result") ON DELETE RESTRICT;

            ALTER TABLE "student" ADD CONSTRAINT "fk_student__id_group" FOREIGN KEY ("id_group")
            REFERENCES "group" ("id_group") ON DELETE RESTRICT;

            ALTER TABLE "student" ADD CONSTRAINT "fk_student__id_result" FOREIGN KEY ("id_result")
            REFERENCES "result" ("id_result") ON DELETE RESTRICT;

            ALTER TABLE "test" ADD CONSTRAINT "fk_test__id_result" FOREIGN KEY ("id_result")
            REFERENCES "result" ("id_result") ON DELETE RESTRICT;

            ALTER TABLE "student_test" ADD CONSTRAINT "fk_student_test__id_student" FOREIGN KEY ("id_student")
            REFERENCES "student" ("id_student") ON DELETE RESTRICT;

            ALTER TABLE "student_test" ADD CONSTRAINT "fk_student_test__test" FOREIGN KEY ("id_test")
            REFERENCES "test" ("id_test") ON DELETE RESTRICT;

            ALTER TABLE "test_question" ADD CONSTRAINT "fk_test_question__id_questions" FOREIGN KEY ("id_questions")
            REFERENCES "questions" ("id_question") ON DELETE RESTRICT;

            ALTER TABLE "test_question" ADD CONSTRAINT "fk_test_question__id_test" FOREIGN KEY ("id_test")
            REFERENCES "test" ("id_test") ON DELETE RESTRICT;

            ALTER TABLE "profile" ADD CONSTRAINT "fk_profile__id_student" FOREIGN KEY ("id_student")
            REFERENCES "student" ("id_student");

            ALTER TABLE "profile" ADD CONSTRAINT "fk_profile__user" FOREIGN KEY ("id_user")
            REFERENCES "user" ("id_user")
            """)
        cur.execute("""
            INSERT INTO public.user (id_user, login, password, dt_create) VALUES (1, 'admin11', 'mypass11', '2022-05-20');

        """)
        # conn.commit()

