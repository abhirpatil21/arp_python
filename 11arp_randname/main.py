import random

names = ["Abhi", "Shree", "Shreya", "Swara"]

print(f"names : {names}")
name_count = len(names)
print(f"Count of names : {name_count}")

random_num = random.randint(0, name_count - 1)

print(f"Name selected : {names[random_num]}")

