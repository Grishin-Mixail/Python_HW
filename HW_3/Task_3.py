# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

def counter_wor_repit_top_10(text):
    with open(text, "r") as text:
        processed_text = text.read()

    chars = ".,!?,;:'(*&^%#@><_/=÷×+[]"

# 1. убираем все знаки припинания
    processed_text = processed_text[::-1]
    for i in processed_text:
        for j in chars:
            processed_text = processed_text.replace(j, "")

# 2. поднимаем все слова в верхний регистр и создаем список из слов
    processed_text = processed_text.upper().split(" ")

# 3. подсчитываем количество каждого слова
    counter_word = []
    for i in range(len(processed_text)):
        count = 0
        for j in processed_text:
            if processed_text[i] == j:
                count += 1
        counter_word.append(str(count) + " - " + processed_text[i][::-1])

# 4. делаем список уникальным
    counter_word = set(counter_word)
    counter_word = list(counter_word)

#5. сортируем список слов по их количеству
    counter_word = sorted(counter_word)[::-1]

#6. берём первые 10 слов с наибольшим кол-вом повторений
    counter_word = counter_word[:10:]

    with open("1.txt", "w") as count_word:
        for i in counter_word:
            count_word.write(str(i) + "\n")

counter_wor_repit_top_10("test.txt")