sen=input('Enter a word or phase: ')
sen0=sen.upper() #let sen0 points to the uppercase of sen
sen1=''
sen3=''
sen5=''
space=sen.count(' ')
alpha='abcdefghijklmnopqrstuvwxyz'
for i in range(space):
   x=sen.find(' ')
   sen1=sen1+sen[:x]
   sen=sen[x+1:]
   if i==(space-1):
      sen1=sen1+sen
   else:
      continue
   #print(sen,'*')
#print(sen,'**')
#print(sen1)------------------
sen2=sen1.lower()
for lit in sen2:
   if lit in alpha:
      sen3=sen3+lit
   else:
      continue
#print(sen3)------------------
x=len(sen3)
for i in range(1,x+1):
   sen4=sen3[x-i]
   sen5=sen5+sen4
if sen3==sen5:
   print('{0}. is a palindrome.'.format(sen0))
else:
   print('{0}. is a palindrome.'.format(sen0))
   
   
  
   
