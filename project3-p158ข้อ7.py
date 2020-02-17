credit=input('Enter a credit card number: ') #58667936100244
Even=[]
Odd=[] #stating Even=Odd=[].If Even is altered, Odd is altred as well
       # that why you got Odd=[5,6,7,3,1,0,8,6,9,6,0,2,4]
       # Don't for List can change in place.
sumOfE=sumOfO=0
if len(credit)==14:
   creditL=list(credit)
   for i in range(0,14,2):
      Even.extend(creditL[i])
      Even=Even
   print(Even)
   for i in range(1,14,2):
      Odd.extend(creditL[i])
      Odd=Odd
   print(Odd)
   Evenstr=''.join(Even)
   Oddstr=''.join(Odd)
   for i in range(7): #Even
      x=Evenstr[i]
      x=int(x)
      y=x*2
      if y>=10:
         y=y-9
         sumOfE+=y
      else:
         sumOfE+=y
   print(sumOfE)
   for i in range(7): #Odd
      x=Oddstr[i]
      x=int(x)
      sumOfO=sumOfO+x
   print(sumOfO)
   result=sumOfE+sumOfO
   if result%10==0:
      print('The number is valid')
   else:
      print('The number is invalid')
else:
   print('Credit card number must have 14-digit')
