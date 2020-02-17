n=int(input('Enter amount of change(0-99 cent(s))): '))
Q=n//25
D1=n%25
D=D1//10
N1=D1%10
N=N1//5
P=N1%5
print("Quarters :{0:<5d}Dimes :{1:<d}".format(Q,D))
print("Nickels :{0:<5d} Cents :{1:<d}".format(N,P))
print('\n')
print('******Or print*********')
print('\n')
print('Quarters :',Q,end='\t'.expandtabs(5))
print('Dimes :',D)
print('Nickels :',N,end='\t'.expandtabs(6))
print('Cents :',P)


