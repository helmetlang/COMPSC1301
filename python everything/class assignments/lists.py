a = list(range(100))
b1 = [max (i*3-7, 50) for i in a]
b2 = [i+1 for i in a]
c = [i*2 for i in b2[:50]]
d = [i-1 for i in c]
e = [i for i in d if i%5==0]
mysquares = { i: i*i for i in range(10)}
mysquares[6] # prints 36 :)