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

def give_score(Name,data):
    """
    Выводит оценку за проект определенного человека

    Параметры:
    Name - имя человека(полное ФИО)
    data - список словарей с информацией по людям

    """

    for row in data:
        if row['name'] == Name:
            print(f'Ты получил: {row["score"]}, за проект - {row["id_project"]}')

def replacing(data):
    """
    Находит среднее значение и изменяет None на это среднее
    
    Параметры:
    data - список словарей с информацией

    """
    counter = 0
    average = 0
    for row in data:
        if row['score'] != 'None':
            average += int(row['score'])
            counter += 1
    average = round(average/counter, 3)
    
    for row in data:
        if row['score'] == 'None':
            row['score'] = average

    return data

data = getinfo_csv_file('students.csv')
give_score('Хадаров Владимир Валериевич',data)
data = replacing(data)

with open("student_new.csv", "w") as csv_write:
    file = csv.writer(csv_write)

    file.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])

    for row in data:
        file.writerow(list(row.values()))

