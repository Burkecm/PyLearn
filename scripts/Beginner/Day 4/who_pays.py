import random as rand
friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel", "Frank", "Gerald"]
randFriend = rand.randint(0, len(friends))
print(friends[randFriend])
print(rand.choice(friends))