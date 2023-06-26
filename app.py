from random import *

# w = randint(10,20)
# h = randint(10,20)

w = int(input('digite a largura do labirinto'))
h = int(input('digite a altura do labirinto'))

labirinto = []

labirinto.append([1,randint(2, w-2)])
labirinto.append([2,labirinto[-1][-1]])
while labirinto[-1][0] != h:
     
     n = randint(1,10)
     
     if n >= 1 and n < 4:
          x = [labirinto[-1][0],labirinto[-1][-1]+1]
     elif n >= 4 and n < 8:
          x = [labirinto[-1][0],labirinto[-1][-1]-1] 
     elif n >=8 and n <= 10:
          x = [labirinto[-1][0]+1,labirinto[-1][-1]]
     if x[-1] <= w-2 and x[-1] >= 2 and x not in labirinto:
          labirinto.append(x)

x = []
for item in labirinto:
     x.append((w*(item[0]-1))+item[1])

x.sort()

for i in range(0,((w)*(h-1))+1):
     if i%(w) == 0:
          print('')
     elif i in x:
          print(' ', end='')
     else:
          print(u"\u2588", end='')
     