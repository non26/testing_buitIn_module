n = int(input ('Input an integer: '))

if (n > 0):
    print ('x is positive number')
    print ('Show number from 0 to %d' % (n - 1))

else:
    print ('x isn\'t positive number')

for i in range(1,n+1):
    while i<=5:
          print(i, end='   ')
    while i<=10:
         print(i, end='   ')


