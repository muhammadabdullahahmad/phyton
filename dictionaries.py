my_dict = {}
my_dict1 = {1: 'apple', 2: 'ball'}
my_dict ={ 1: [2,4,31]}
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict['name'])
print(my_dict.get('age'))
my_dict['age'] = 26
print (my_dict)
my_dict[ 'address'] = 'Downtown'
print(my_dict)
# remove particular element
my_dict.pop('age')
print(my_dict)
# access a particular element
print ("Address:", my_dict.get('address'))
# remove all the elements
my_dict. clear ()
print(my_dict)
