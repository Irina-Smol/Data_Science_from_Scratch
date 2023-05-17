users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    {"id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

# And loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j

def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user)
                        for user in users)  # 24

assert total_connections == 24
num_users = len(users)
# length of the users list
avg_connections = total_connections / num_users   # 24 / 10 == 2.4

assert num_users == 10
assert avg_connections == 2.4

# Create a list (user_id, number_of_friends).
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1],reverse=True)   # by num_friends                                                               reverse=True)   # largest to smallest  # Each pair is (user_id, num_friends): # [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), #  (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]  assert num_friends_by_id[0][1] == 3  # several people have 3 friends assert num_friends_by_id[-1] == (9, 1)  # user 9 has only 1 friend  def foaf_ids_bad(user):     """foaf is short for "friend of a friend" """     return [foaf_id             for friend_id in friendships[user["id"]]             for foaf_id in friendships[friend_id]]  #[0, 2, 3, 0, 1, 3] assert foaf_ids_bad(users[0]) == [0, 2, 3, 0, 1, 3]  print(friendships[0])  # [1, 2] print(friendships[1])  # [0, 2, 3] print(friendships[2])  # [0, 1, 3]  assert friendships[0] == [1, 2] assert friendships[1] == [0, 2, 3] assert friendships[2] == [0, 1, 3]  from collections import Counter   # not loaded by default  def friends_of_friends(user):     user_id = user["id"]     return Counter(         foaf_id         for friend_id in friendships[user_id]     # For each of my friends,         for foaf_id in friendships[friend_id]     # find their friends         if foaf_id != user_id                     # who aren't me         and foaf_id not in friendships[user_id]   # and aren't my friends.     ) print(friends_of_friends(users[3]))               # Counter({0: 2, 5: 1})  assert friends_of_friends(users[3]) == Counter({0: 2, 5: 1})

# Each pair is (user_id, num_friends):
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
#  (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]

assert num_friends_by_id[0][1] == 3
# several people have 3 friends assert
num_friends_by_id[-1] == (9, 1)
# user 9 has only 1 friend

def foaf_ids_bad(user):
    """foaf is short for "friend of a friend" """
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

#[0, 2, 3, 0, 1, 3]

assert foaf_ids_bad(users[0]) == [0, 2, 3, 0, 1, 3]
print(friendships[0])  # [1, 2]
print(friendships[1])  # [0, 2, 3]
print(friendships[2])  # [0, 1, 3]

assert friendships[0] == [1, 2]
assert friendships[1] == [0, 2, 3]
assert friendships[2] == [0, 1, 3]

from collections import Counter   # not loaded by default
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]    # For each of my friends,
        for foaf_id in friendships[friend_id]     # find their friends
        if foaf_id != user_id                     # who aren't me
        and foaf_id not in friendships[user_id]   # and aren't my friends.
        )

print(friends_of_friends(users[3]))

# Counter({0: 2, 5: 1})
assert friends_of_friends(users[3]) == Counter({0: 2, 5: 1})


'''
Функция, которая отыскивает пользователей, интересующихся определенной темой
'''

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
    """найти id всех пользователей, которым интересна целевая тема"""
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

# создадим индекс плользователей, сгрупированный по интересу
from collections import defaultdict, Counter

# идентификаторы пользователей по идентификатору темы, ключи - интересующие темы, значения - списки тем
# для конкретного идентификатора
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# индекс тем, сгрупированный по пользователям

# идентификаторы тем по идентификатору пользователя, ключи - идентификаторы пользователей,
# значения - списки тем для конкретного идентификатора
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

'''
легко найти лицо, у которого больше всего общих интересов с заданными пользователем
1) выполнить обход интересющих пользователя тем
2) по каждой теме выполнить обход других пользователей, интересующихся той же самой темой
3) подсчитать, сколько раз встретятся другие пользователи
'''

# наиболее общие интересы с пользователем user
def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"])
