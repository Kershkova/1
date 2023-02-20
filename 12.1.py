text = input('input text: ') #ввели текст
list_text = set(text.split(' '))
new_dict = {}
for uniqie in list_text:    new_dict[uniqie] = text.count(uniqie)
print(new_dict)