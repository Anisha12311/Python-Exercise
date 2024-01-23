import functools

functions = [5,4,3,2,1]

result = functools.reduce(lambda x,y : x*y , functions)
print(result)

squares = [i * i for i in range(1,11)]
print(squares)

students = [100,90,80,70,60,50,40,30,20,10,0]
listf = list(filter(lambda x : x>= 50, students))
listc = [ i for i in students if i >= 50]
print(listc)
print(listf)

dict_f = {'Boston' : 32, 'Japan' : 89, 'Los Angeles' : 100}
dict_c = {key: round((value-32)* 5/9) for (key,value) in dict_f.items()}
dict_M = {key : value *2 for (key,value) in dict_f.items()}
dict_W = {key : ('Warm' if value >= 40 else 'Cold') for (key, value ) in dict_f.items()}
print(dict_c)
print(dict_f.items())
print(dict_M)
print(dict_W)