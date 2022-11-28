import data_modification as dm
import user_interface as ui

def user_view():
    data = int(input("Выберите операцию для выполенения с данными: 1 - Поиск; 2 - Удаление; 3 - Ввод; 4 - Обновление: "))
    if data == 1:
        dm.find_data(ui.data_search())
    elif data == 2:
        dm.data_delete(ui.data_del())
    elif data == 3:
        dm.data_add(ui.data_insert())
    elif data == 4:
        dm.data_mod(ui.data_modified())
    else:
        print("Wrong data!")
    
