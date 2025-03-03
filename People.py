# 2. PEOPLE: Make 3 dictionaries representing different people (their firstname, lastname, and phone number) and store all three dictionaries in a list called "people". 
Bobdict = {'name' : 'Bob', 'lname' : 'Marley','number' : '762-7246-7986'}
Jerrydict = {'name' : 'Jerry', 'lname' : 'Monk','number' : '123-7466-9999'}
Robdict = {'name' : 'Rob', 'lname' : 'Fiddle','number' : '433-666-6666'}

# Loop through your list of people, printing everything you know about each person. 
people = []
people.append(Bobdict)
people.append(Jerrydict)
people.append(Robdict)

for dictionary in people:
    for item, value in dictionary.items():
        print(f"{item}: {value}")
    print()

# Make sure the final output is nicely formatted and neat.