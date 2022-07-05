import os.path
from pprint import pprint


def strings_counting(file:str) -> int:
    with open(file, 'r') as f:
        return sum(1 for _ in f)


def reading_of_catalog(file_name: str) -> dict:
    with open(file_name) as file:
        dict = {}
        for line in file:
            dish_name = line.strip()
            dict[dish_name] = []
            for j in range(int(file.readline())):
                consist = file.readline().split(' | ')
                dict[dish_name].append({'ingredient_name': consist[0],
                                        'quantity': int(consist[1]),
                                        'measure': consist[2].strip()})
            file.readline()
    return dict


def list_of_stores_with_ingredients(dishes: list, person_count: int, cook_book: dict) -> dict:
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],
                                                       'quantity': (consist['quantity'] * person_count)}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    return result



def rewriting(file_for_writing: str, base_path, location):
    files = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        files.append([strings_counting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i])
    for file_from_list in sorted(files):
        opening_files = open(file_for_writing, 'a')
        opening_files.write(f'{file_from_list[2]}\n')
        opening_files.write(f'{file_from_list[0]}\n')
        with open(file_from_list[1], 'r') as file:
            counting = 1
            for line in file:
                opening_files.write(f'строка № {counting} в файле {file_from_list[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()

if __name__ == '__main__':
    file_with_recipes = os.path.abspath("C:\\Users\\ЯРОСЛАВ-ПК\\PycharmProjects\\pythonProject6\\Recipe.txt")
    dishes = ['Омлет', 'Фахитос', 'Сельдь под шубой', 'Запеченный картофель']
    pprint(reading_of_catalog(file_with_recipes))
    print(list_of_stores_with_ingredients(dishes, 2, reading_of_catalog(file_with_recipes)))
    file_for_writing = os.path.abspath(C:\\Users\\ЯРОСЛАВ-ПК\\PycharmProjects\\pythonProject6\\Result.txt")
    base_path = os.getcwd()
    location = os.path.abspath("C:\\Users\\ЯРОСЛАВ-ПК\\PycharmProjects\\pythonProject6\\txts_for_Opening and reading a file, writing to a file")
    rewriting(file_for_writing, base_path, location)



