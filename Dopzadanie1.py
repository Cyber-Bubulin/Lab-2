from csv import reader 

if __name__ == '__main__':
    publisher = []


    with open('books-en.csv', 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        for raw in table:
            publisher.append(raw[4])



    publisher = set(publisher)
    g = list(publisher)
    answer = sorted(g)


    print(answer)
