text_1 = input('input chusla: ')
text_2 = input('input chusla: ')

l_1 = set(text_1.split(' '))
l_2 = set(text_2.split(' '))

unique = set(l_1 ^ l_2)
print(unique)
print(len(unique))