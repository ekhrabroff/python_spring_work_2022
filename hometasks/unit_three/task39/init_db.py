from task39 import db, Post, Comment

post1 = Post(title='Первый пост', content='Это содержание певого поста')
post2 = Post(title='Второй пост', content='А тут контентик для второго поста')
post3 = Post(title='Третий пост', content='Тут содержание третьего поста')

comment1 = Comment(content='Comment for the first post', post=post1)
comment2 = Comment(content='Comment for the second post', post=post2)
comment3 = Comment(content='Another comment for the second post', post_id=2)
comment4 = Comment(content='Another comment for the first post', post_id=1)


db.session.add_all([post1, post2, post3])
db.session.add_all([comment1, comment2, comment3, comment4])

db.session.commit()