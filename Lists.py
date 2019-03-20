# Lists and what can be done with them
# - Lists are mutable, meaning they can be changed after they are created

my_list = ['item1', 'item2', 'item3']

# Can search through lists to find index
print (my_list.index('item2')) # would print 1

# Can insert item at a specific index which alters original list - list.insert(index, 'item')
my_list.insert(1, 'item4') # inserts 'item4' at index 1

# Can sort lists alphabetically with list.sort()
my_list.sort()

# Can remove items from a list
my_list.remove('item3') # removes item3 from list

# Ways to remove items from a list 
n = [1, 3, 5]

n.pop(1) # Returns 3 (the item at index 1)
print (n) # prints [1, 5]

n.remove(1) # Removes 1 from the list, NOT the item at index 1
print (n) # prints [3, 5]

del(n[1]) # Doesn't return anything
print (n) # prints [1, 5]

# Range funciton returns a list of numbers from start up to (not including) stop
range(6) # => [0, 1, 2, 3, 4, 5] range(stop)
range(1, 6) # => [1, 2, 3, 4, 5] range(start,stop)
range(1, 6, 3) # => [1, 4] range(start, stop, step)

# Can add together lists
a = [1, 2, 3]
b = [4, 5, 6]
print (a + b) # prints [1, 2, 3, 4, 5, 6]

# Join lists "join method".join(list)
a = ["a", "b", "c"]
" ".join(a) # would give "a b c" 

# Sort lists with sorted([list])
lst = [4, 2, 5, 7]
n_lst = sorted(lst) # sorts alphabetically or numbers 0-N

# List Comprehension
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print (evens_to_50) # prints[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0] # [function for X - for-loop to loop through the range - if condition to limit output]

# List slicing - [start index:end index:stride/step] start index exclusive, end index inclusive
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print (l[2:9:2]) # prints [9, 25, 49, 81]

to_five = ['A', 'B', 'C', 'D', 'E']

print (to_five[3:])
# prints ['D', 'E'] 

print (to_five[:2])
# prints ['A', 'B']

print (to_five[::2])
# print ['A', 'C', 'E']

print (to_five[::-1])
# print ['E', 'D', 'C', 'B', 'A']