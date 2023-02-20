d = {
  'apple': ['malum1', 'pomum', 'popula'],
  'fruit': ['baca', 'bacca', 'popum'],
  'punishment': ['malum', 'multa']
}
new_d = {}
for name, items in d.items():
    for item in items:
        new_item = {item: name}
        new_d.update(new_item)
print(new_d)