# Напишите однострочный генератор словаря, который принимает на вход три списка 
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии

name = ["Ivan","Max", "John"]
base = [100, 120, 150]
reward = ["5.5", "10.1", "10.25"]

new_dict ={name[i]: base[i]*float(reward[i])*0.01 for i in range(0,len(name))}
print(new_dict)