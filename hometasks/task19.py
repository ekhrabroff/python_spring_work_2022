#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

count = 0

#Каждое значение из списка должно находится на отдельной строке.

f = open("../../hometasks/algoritm.csv", "wt")

for i in range(11):
    if i == 10:
        f.write(str(i)+'\n')
    elif i == 0:
        f.write('id'+',')
    else:
        f.write(str(i) + ',')

for i in algoritm:
   f.write(i+'\n')

f.close()

