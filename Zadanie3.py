from random import *
from csv import reader


if __name__=="__main__":
    output = open('Zadanie3.txt', 'w')
    numer = 0
    indexx = 0
    itog = []



    with open('books-en.csv', 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            indexx +=1
            itog.append(f'{row[2]}. {row[1]} - {row[3]} \n')

    for i in range(20):
        number = randint(1,9410)
        numer += 1
        output.write(f'{numer}) {itog[number]}')


    output.close()





