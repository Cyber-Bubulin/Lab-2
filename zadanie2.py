from csv import reader

if __name__ == "__main__":
    author = input("Введите автора ")
    storage = []

    with open('books.csv', 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            if author in row[4] and ('2018' in row[6] or '2015' in row[6]):
                if row[1][1]=='#':
                    storage.append(f'ID:{row[0]};Название: {row[1][1:]};Возрастное ограничение:{row[5]}+;Дата поступления: {row[6]} \n')
                else:
                    storage.append(f'ID:{row[0]};Название: {row[1]};Возрастное ограничение:{row[5]}+;Дата поступления: {row[6]} \n')

    if len(storage)!=0:
        print('У этого автора для выдачи доступны: \n', *storage)
    else:
        print('Для выдачи недоступны книги этого автора')