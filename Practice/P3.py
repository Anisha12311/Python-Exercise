

# list

list1 = [1,2,2,2,3,4]
# list1.append(5)
# print(list1)
# list1.extend([6,7,8])
# print(list1)
# list1.insert(0,0)
# print(list1)
# list1.remove(5)
# print(list)
# list1.pop(2)
# print(list1)
# list1.index(3)
test = list1.count(2)
print(test)

#using list  as Queues

from collections import deque

queue = deque(["Eries","Jhon", "Michael"])
queue.append('Alice')
queue.popleft()
print(queue)

squares = list(map(lambda x:x**2,range(10)))
arr = [x**2 for x in range(10)]
print(squares)
print(arr)

list_format = [(x,y) for x in [1,2,3] for y in [4,5,6]]

print(list_format)

vec = [[1,[2],3],[4,5,6],[7,8,9]]
single_elm = [num for elm in vec for more in elm if isinstance(more,(list,tuple)) for num in more]
print(single_elm)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

value = [row[i] for row in matrix for i in range(4)]
print(value)

# tuple

t = 12345, 54321, 'hello!'
print(t)

# Set

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
unique = set('asdfafaasdfsdfsdf')
print(unique)

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 3434
del tel['jack']
print(list(tel))
print(sorted(tel))

dict_tel = dict([('jack',4564),('sape',4565)])
print(dict_tel)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
    print("What your {0}? Its {1}".format(q,a))
