x='hello world'
# x.split()
print('this is a string {} {} {}'.format('inserted','string',x))
print(f"string test {x}")

L = x[::-1]
L


# Lists

my_list = ["toto",1,2323]
another_list = ["soso","lolo"]
len(my_list)
new_lest = my_list + another_list
new_lest.append("3")
poped_item = new_lest.pop()
num_list = [6,4,8,3]
char_list = ['a','h','r','d','v']
num_list.sort()
char_list.reverse()
num_list
char_list

# Dictionaries

my_dict = {"toto":"val1","soso":"val2"}
my_dict["toto"]
my_dict.keys()
my_dict["lolo"] = "val3"
my_dict
my_dict.items()

# sets
myset = set()
myset.add(3)
myset.add(2)
myset

# Files I/O

myfile = open("test.txt")
%pwd
myfile.read()
myfile.seek(0)
myfile.readlines()
myfile.close()

with open('test.txt') as my_new_file:
    content = my_new_file.read()

content

with open('tests.txt',mode='w') as testfile:
    testfile.write("FOUR ON FORTH")
