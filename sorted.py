numbers = [1, 5, 8, 4, 6, 2]

users = [
    {'name': 'Ava', 'family': 'Mohseni', 'age': 23},
    {'name': 'taha', 'family': 'Mohseni', 'age': 40},
    {'name': 'ali', 'family': 'Mohseni', 'age': 30},
    {'name': 'sara', 'family': 'Mohseni', 'age': 80}
]


print(sorted(users, key=lambda user: user['age'], reverse=True))

# print(numbers)

# numbers.sort()

# print(numbers)


# result = sorted(numbers, reverse=True)

# print(result)

# print(numbers)
