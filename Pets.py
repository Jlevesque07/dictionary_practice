# 1. PETS: Make 3 dictionaries where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner's name. 
Tomdict = { 'name' : 'Tom', 'owner' : 'Bob', 'animal' : 'cat'}
Berrydict = {'name' : 'Berry', 'owner' : 'Carry', 'animal' : 'hampster'}
Golemdict = {'name' : 'Golem', 'owner' : 'Hulk', 'animal' : 'rock'}
# Store these dictionaries in a list called "pets". 
pets = []
pets.append(Tomdict)
pets.append(Berrydict)
pets.append(Golemdict)
# Next, loop through your list and as you do, print everything you know about each pet. 
for dictionary in pets:
    for key, value in dictionary.items():
        print(f"{key}: {value}")
    print()
# Make sure the final output is nicely formatted and neat.