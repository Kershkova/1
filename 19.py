import  re
text = str(input("Введіть текст "))
if text == "" or text.isspace():
    raise Exception("Введіть текст, який бажаєте зробити хештегом")
text = re.sub(r'\W', '',text)
if text == "" or text.isspace():
    raise Exception("Введіть не пустий текст, який бажаєте зробити хештегом")
text = text.title()
e = "#"
text = e + text
if len(text) > 140:
    raise Exception("Занадто довгий хештег")
print(text)
