import csv
import random

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
                'login' : None,
                'password' : None,
            }
        data.append(info)
    return data
def generate_login(data):
    '''
    Создает логины людей

    Параметры:
    data - список словарей

    '''
    for row in data:
        row['login'] = f'{row["name"].split()[0]}_{row["name"].split()[1][0]}{row["name"].split()[2][0]}'

    return data

def generate_password(data):
    """
    Создает пароли пользователей 

    Параметры:
    data -список словарей
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    
    for row in data:
        password = ''

        for i in range(8):
            password += random.choice(alphabet)
        row['password'] = password

    return data




data = getinfo_csv_file('students.csv')
data = generate_login(data)
data = generate_password(data)

with open('students_password.csv', 'w') as csv_write:
    file = csv.writer(csv_write)

    file.writerow(['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])

    for row in data:
        file.writerow(list(row.values()))


