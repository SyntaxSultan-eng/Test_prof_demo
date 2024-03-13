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

def need_info(data):
    """
    Получает новый список словарей, где ключ - оценка, а значение - ФИО

    Параметры:
    data - список словарей с информацией
    """
    new_list = []

    for row in data:
        scores = {}

        if row['score'] != 'None' and '10' in row['class']:
            scores[row['name']] = int(row['score'])
            new_list.append(scores)

    return new_list


def Insertion_sort(array):
    """
    Стандартная сортировка вставками, но на вход подается список словарей

    Параметры:
    array - список словарей
    """

    length = len(array)

    for num in range(length):
        temp = array[num]
        neighbor = num - 1
        while neighbor >= 0 and list(array[neighbor].values())[0] > list(temp.values())[0]:   
            array[neighbor+1] = array[neighbor]          
            neighbor -= 1                                
            array[neighbor+1] = temp

    return array

data = getinfo_csv_file('students.csv')

new = need_info(data)

new = (Insertion_sort(new))

print("10 класс")
count = 0
for row in new:
    if count < 3 and list(row.values())[0] == 5:
        count += 1
        print(f'{count} место: {list(row.keys())[0].split()[1][0]}. {list(row.keys())[0].split()[0]}')






