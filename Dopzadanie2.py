from csv import reader
import operator


if __name__ == "__main__":


    on_hands = []
    number = -1


    with open('books-en.csv', 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        table = sorted(table, key=operator.itemgetter(5), reverse = True) #Сортировка исходного файла. Причём макимальные значения, выдаваемые программой меньше, чем максимальные значения, которые есть в файле. Почему так, я не знаю. Всё упирается в девятку...        
        for row in table:
            number+=1
            if number < 20:
                
                print(f' {number}) {row[2]}. {row[1]}, {row[5]} ')
        




   


