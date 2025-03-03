# 3. CITIES: Make a dictionary called "cities". 
# Use the names of three cities as keys in your dictionary.
cities = ['Alhaio', 'Applecity', 'Digwoid']
weathers = ["sunny", "rainy", "cloudy"]
stuff = []
# Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. 
for key in cities:
    key = {}
    print()
    key['country'] = input("What country is this city in? ").strip().title
    key['population'] = int(input("What is the population of this city? "))
    key['funfact'] = input("What is a fun fact about the city?" ).strip().title()
    stuff.append(key)
# The keys for each city's dictionary should be something like "country, population, and fact". Print the name of each city and all of the information you have stored about it. 
# Make sure the final output is nicely formatted and neat

print(stuff)