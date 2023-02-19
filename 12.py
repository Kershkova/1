from collections import defaultdict
text = input('input text: ') #ввели текст
kilkist_sliv = len(text.split(" ")) #кількіть слів у тексті
list_text = text.split(' ') #створили список зі слів тексу
new_list = [] #створили ще один список, елементи якого будуть ключами
for n in range(0, kilkist_sliv):
    new_list.append(n)
new_dict = dict(zip(new_list, list_text)) #створили словник з двох списків

word_count_dict = defaultdict(int) #створюємо "словник множини"
for word in list_text: #рахуємо скільки разів зустрічається слово через словник
    print(word, word_count_dict[word])
    word_count_dict[word] += 1