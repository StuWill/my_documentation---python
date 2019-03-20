# Dictionaries and what can be done with them
# - Dictionaries are mutable, meaning they can be changed after they are created
# - Length of a dictionary is how many key:value pairs it has


# A dictionary consists of a key and value pair - dictionary = {key1 : value1, key2 : value2, key3 : value3}
my_dictionary = {"Jason" : 41, "Mike" : 35, }

# Can print values
print (my_dictionary["Jason"]) # would print 41

# Add key:value pairs to a dictionary - dictionary[new key] = value
my_dictionary["Simon"] = 30 # adds "Simon" : 30 to the dictionary

# Can delete key:value pairs from a dictionary - del dictionary[key]
del my_dictionary["Mike"]

# A new value can be associated with a key - dictionary[key] = new value
my_dictionary["Simon"] = 35

# Return an array of tuples
my_dict = {
  "Name": "Griffin",
  "State": "Washington",
  "Age": 24
}

print (my_dict.items()) # prints [('Age', 24), ('State', 'Washington'), ('Name', 'Griffin')] - an immutable list/ tuple.
print (my_dict.keys()) # print ['Age', 'State', 'Name']
print (my_dict.values()) #print [24, 'Washington', 'Griffin']


