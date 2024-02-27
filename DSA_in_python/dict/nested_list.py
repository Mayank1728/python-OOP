data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
    False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

count = 0
for _, nest in enumerate(data):
    if nest["success"]:
        count += 1

print(count)
