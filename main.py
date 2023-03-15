# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# пара-ра-рам рам-пам-папам па-ра-па-да


stih = input("Введите текст стихотворения: ")
# stih = str.split(stih, " ")

def search_glasn (text):
    glasn = "аиеёоуыэюя"
    count = 0
    for i in text:
        if i in glasn:
            count += 1
    return count

# count = search_glasn(stih[0])
# print(count)

def check_rythm (stih):
    lines = stih.split()
    counts = []
    for line in lines:
        words = line.split("-")
        line_count = sum([search_glasn(word) for word in words])
        counts.append(line_count)
    if len(set(counts)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")

check_rythm(stih)