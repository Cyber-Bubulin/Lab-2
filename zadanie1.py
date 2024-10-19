from csv import reader

if __name__ == "__main__":
    count = 0


    with open('books-en.csv', 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            if len(row[1]) >= 30:
                count+=1 


    print(count)

