from pprint import pprint

with open('dishes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dishes_name = line.strip()
        ingredient_count = int(file.readline())
        detail = []
        for _ in range(ingredient_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            detail.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
        file.readline()
        cook_book[dishes_name] = detail
    # pprint(cook_book, sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish in dishes:
        if dish in cook_book:
            detail_list = cook_book[dish]
            for ingredient in detail_list:
                if ingredient['ingredient_name'] in res:
                    res[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    res[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
    # pprint(res, sort_dicts=False)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

file_all = open('file_all.txt', 'w', encoding='utf-8')
dict_file_len = {}
dict_file_content = {}
with open('1.txt', encoding='utf-8') as file1:
    file_content = file1.readlines()
    file1.seek(0)
    len_list = len(file1.readlines())
    dict_file_len[file1.name] = len_list
    dict_file_content[file1.name] = file_content

with open('2.txt', encoding='utf-8') as file1:
    file_content = file1.readlines()
    file1.seek(0)
    len_list = len(file1.readlines())
    dict_file_len[file1.name] = len_list
    dict_file_content[file1.name] = file_content

with open('3.txt', encoding='utf-8') as file1:
    file_content = file1.readlines()
    file1.seek(0)
    len_list = len(file1.readlines())
    dict_file_len[file1.name] = len_list
    dict_file_content[file1.name] = file_content

sorted_dict = dict(sorted(dict_file_len.items(), key=lambda item: item[1]))

for file in sorted_dict:
    file_all.write('\n'+file+'\n')
    file_all.write(str(sorted_dict[file])+'\n')
    for line1 in dict_file_content[file]:
        file_all.write(line1)

print(dict_file_len)
print(dict_file_content)
print(sorted_dict)




file_all.close()