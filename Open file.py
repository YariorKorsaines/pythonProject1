import os.path
from pprint import pprint


def strings_counting(file:str) -> int:
    with open(file, 'r', encoding="UTF-8") as f:
        return sum(1 for _ in f)


def reading_of_catalog(file_name: str) -> dict:
    with open(file_name, encoding="UTF-8") as file:
        dict = {}
        for line in file:
            dish_name = line.strip()
            dict[dish_name] = []
            for j in range(int(file.readline())):
                consist = file.readline().split(' | ')
                if len(consist) == 3:
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
            print(f'Dishes {dish} not in the recipe book')
    return result



def rewriting(file_for_writing: str, base_path, location):
    files = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        arr = [strings_counting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i]
        files.append(arr)
    for file_from_list in sorted(files):
        opening_files = open(file_for_writing, 'a', encoding="UTF-8")
        opening_files.write(f'{file_from_list[2]}\n')
        opening_files.write(f'{file_from_list[0]}\n')
        with open(file_from_list[1], 'r', encoding="UTF-8") as file:
            counting = 1
            for line in file:
                opening_files.write(f'line in № {counting} in file {file_from_list[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()

if __name__ == '__main__':
    file_with_recipes = os.path.abspath('Recipe.txt')
    dishes = ['Omelet', 'Fahjitos', 'Herring under a fur coat', 'Baked potato']
    pprint(reading_of_catalog(file_with_recipes))
    print(list_of_stores_with_ingredients(dishes, 2, reading_of_catalog(file_with_recipes)))
    open("Result.txt", "w", encoding="UTF-8")
    file_for_writing = os.path.abspath('Result.txt')
    base_path = os.getcwd()
    location = os.path.abspath('txts_for_Opening and reading a file, writing to a file')
    rewriting(file_for_writing, base_path, location)


