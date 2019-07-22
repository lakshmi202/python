'''
1. List is used to store multiple values and we can do operation on each value based on index.
2. Using square brackets "[]" we can create a list
3. List is a mutable object
'''
# To create a list
names = ['sri','kumar','balu','ram', 567, 99.9]

# To update a particular value
names[0] = 'sri kumar'

# To append 
names[1] += ' Babu'

# To delete particular value in list
del names[2]

# To delete a total list
del names

# To print particular value based on index
print(names[4])
print(names[-2])


