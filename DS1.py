'''
Задача: есть список пользователей и второй список с дружескими отношениями (кортеж 0, 1) означает, что исследователь
с id 0 и исследователь с id 1 являются друзьями. Необходимо создать словарь, в котором ключи- id пользователя, а
значения-списки id друзей (число друзей)
'''

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# добавляем графу 'friends' для каждого пользователя в users
for user in users:
    user['friends'] = []

# заполняем друзей из списка кортежей в friendship_pairs
for i in friendship_pairs:
    users[i[0]]['friends'].append(users[i[1]]['name'])
    users[i[1]]['friends'].append(users[i[0]]['name'])

for user in users:
    print(user)

# метод, возращающий число друзей пользователя user
def GetCountOfFriends(user):
    return len(user['friends'])

for user in users:
    print(user['name'], ':', GetCountOfFriends(user))

# список из кортежей, где каждый кортеж состоит из id пользователя и его количества друзей
user_and_friends = []
for user in users:
    user_and_friends.append((user['id'], GetCountOfFriends(user)))
print('\nСписок из кортежей (id, число друзей):\n', user_and_friends)

# функция для сортировки списка из кортежей по второму элементу каждого из кортежа
def GetCount(user):
    return user[1] # возвращает второй параметр каждого из кортежей в списке кортежей user_and_freinds

user_and_friends_sorted = sorted(user_and_friends, key = GetCount, reverse = True)

print('\nОтсортированный список из кортежей (id, число друзей):\n', user_and_friends_sorted)