import random

name = ["Michael", "John", "Ali", "James", "Dan", "Liam", "Amy"]
when = ["Friday", "Monday", "Tuesday", "Wednesday", "Thursday", "Saturday", "Sunday"]
place = ["a house", "the school", "an abandon hospital", "the toilet"]
animal = ["a rabbit", "a frog", "a horse", "a cow", "a dog", "a cat", "a bird", "a mouse"]
happened = ["they bullied them", "got scolded by teacher", "he resigned", "went to the hospital", "injured badly"]

print(random.choice(name) + " went to " + random.choice(place) + " on " + random.choice(when) + " to see " + random.choice(animal) + " and " + random.choice(happened))