import csv

def getinfo_csv_file(filename):
    """
    Преобразуем csv file в список словарей с информацией о каждом человеке

    Параметры:
    filename - название файла
    """
    data = []

    file = open(filename)
    csv_reader = csv.reader(file)

    header = True

    for row in csv_reader:
        if header:
            header = False
            continue
        info ={
                'id' : row[0],
                'name' : row[1],
                'id_project' : int(row[2]),
                'class' : row[3],
                'score' : row[4],
            }
        data.append(info)
    return data

data = getinfo_csv_file('students.csv')

user_input = input().lower()

while user_input != 'стоп':
    for row in data:
        if int(user_input) == row['id_project'] and row['score'] != 'None':
            print(f'Проект № {int(user_input)} делал: {row["name"].split()[1][0]}. {row["name"].split()[0]} он(а) получил(а) оценку - {row["score"]}')
            break
    else:
        print('Ничего не найдено')
    user_input = input().lower()





