word=input('Enter a word to code(Must have vowel(s)): ') 
word=list(word)
word0=word[0]
word0=''.join(word0)#
word0=word0.upper()
wordRe=word[1:]
worRe=''.join(wordRe)#
cut='aeiouhyw'
num1='bfpv'
num2='cgjkqsxz'
num3='dt'
num4='l'
num5='mn'
num6='r'
newword=digit=''
for lit in wordRe:
   if lit not in cut:
      newword=newword+lit
   else:
      continue
#print(newword,word0)
if len(newword)>=3:
   newword1=newword[:3]
   for i in range(3):
      if newword1[i] in num1:
         digit=digit+'1'
      elif newword1[i] in num2:
         digit=digit+'2'
      elif newword1[i] in num3:
         digit=digit+'3'
      elif newword1[i] in num4:
         digit=digit+'4'
      elif newword1[i] in num5:
         digit=digit+'5'
      elif newword1[i] in num6:
         digit=digit+'6'
   show=digit
   showList=list(show)
   for k in range(3):
     for j in range(3):
        if k==j+1 and showList[k]==showList[j]:
              del showList[j]
        else:
            pass
   show1=''.join(showList)
   show2=word0+show1
   print('The code word is {0}'.format(show2))
elif len(newword)==2:
   for i in range(2):
      if newword1[i] in num1:
         digit=digit+'1'
      elif newword1[i] in num2:
         digit=digit+'2'
      elif newword1[i] in num3:
         digit=digit+'3'
      elif newword1[i] in num4:
         digit=digit+'4'
      elif newword1[i] in num5:
         digit=digit+'5'
      elif newword1[i] in num6:
         digit=digit+'6'
   show=digit
   showList=list(show)
   for k in range(2):
     for j in range(2):
        if k==j+1 and showList[k]==showList[j] :
            del showList[j]
        else:
            pass
   show1=''.join(showList)
   show2=word0+show1
   print('The code word is {0}0'.format(show2))
elif len(newword)==1:
   for i in range(1):
      if newword1[i] in num1:
         digit=digit+'1'
      elif newword1[i] in num2:
         digit=digit+'2'
      elif newword1[i] in num3:
         digit=digit+'3'
      elif newword1[i] in num4:
         digit=digit+'4'
      elif newword1[i] in num5:
         digit=digit+'5'
      elif newword1[i] in num6:
         digit=digit+'6'
   show=word0+digit
   print('The code word is {0}00'.format(show))
elif len(newword)==0:
   print('The code word is {0}000'.format(word0))
      
      

 
