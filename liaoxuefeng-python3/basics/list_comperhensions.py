print (list(range(1,11)))

L = []
for x in range(1,11):
    L.append(x * x)
print(L)

import os

print([d for d in os.listdir()])

L = ['Hello', 'World', 18, 'Apple', None]

print([s.lower() for s in L if isinstance(s,str)])



