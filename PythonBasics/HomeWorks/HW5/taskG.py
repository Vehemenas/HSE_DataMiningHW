# -*- coding: utf-8 -*
# Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных символов идущих подряд.
# Cлова разделены одним или большим числом пробелов или символами конца строки.
# Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

# Входные данные
# Вводится текст.

# Выходные данные
# Выведите ответ на задачу.

fin = open("input.txt")
words_list = fin.read().split()
words_dict = dict()

for word in words_list:
    if word in words_dict:
        words_dict[word] = words_dict[word] + 1
    else:
        words_dict[word] = 0
    print(words_dict[word])