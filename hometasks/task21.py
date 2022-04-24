# todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">

  <p>?</p>

 </body>
</html>
"""

mass = list(template)
count = 0

for key,value in page.items():
        count = 0
        for i in mass:
                count += 1
                if i == '?':
                        mass[count-1] = value
                        break



string = ''.join(mass)
f = open('../../hometasks/index.html', 'w', encoding="UTF8")
string = string[2:]
f.write(string)
print(string)
f.close()
