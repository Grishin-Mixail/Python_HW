import data_modification as dm

def data_search():
    name = input("Введите данные для поиска: ")
    col = dm.find_data(name)
    if col is not None:
        print(col)
    else:
        print("Данных не обнаружено!")
    return col
    
def data_del():
    name = input("Введите данные для поиска и удаления: ")
    col = dm.data_delete(name)
    col = col[:-2]
    print(col + "  <======= Это строка удалена!")

def data_insert():
    data = input("Введите данные в формате: id, ФИО, Год рождения, Компания, Город, телефон:  ")
    col = dm.data_add(data)
    print(col + "  <======= Это строка добавлена!")

def data_modified():
    data = input("Введите данные для поиска и обновления: ")
    col = dm.data_mod(data)
    print(col[:-2] + "  <======= Это строка обновлена!")
    


