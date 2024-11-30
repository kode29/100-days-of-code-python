import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# random_number = random.randint(0, len(friends)-1)
random_person = random.choice(friends)

print(f"{random_person} is paying the bill!")
