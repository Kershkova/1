text = input('input text: ') #ввели текст
list_text = set(text.split(' ')) #сет для унікальності слів
new_dict = {}
for uniqie in list_text:    new_dict[uniqie] = text.count(uniqie)
print(new_dict)