# For, if, where loops
my_list = [2, 4, 5, 1, 6, 8]
my_dictionary = {"Mike" : 35, "Dave" : 28, "Matt" : 30}

# For loop syntax - for (some variable, can be whatever you want) in (a list that exists):

# Useful to loop through the list, but it's not possible to modify the list this way.
for numbers in my_list:
    print (numbers ** 2) # squares each number in the list and prints them on new line

# Uses indexes to loop through the list, making it possible to also modify the list if needed.
for i in range(len(my_list)):
  print (my_list[i])

# Can loop through keys in a dictionary to get the values
for key in my_dictionary:
    print (my_dictionary[key])

# Can loop through two lists together up to the index of the shortest list
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  if a > b:
    print (a)
  else: 
    print (b)  # prints highest of the two list 3 9 17 15 30
  