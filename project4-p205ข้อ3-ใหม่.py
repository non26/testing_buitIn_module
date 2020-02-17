LENGTH=0 #test 123000004056777888999012345
def main():
   num=input('Enter a positive integer with at most 27 digits:  ')
   verbalizeNumber(BuildListNum(num))
   #BuildListNum(num)
def BuildListNum(num):
   ListNum=[]
   global LENGTH
   LENGTH=len(num)
   if LENGTH%3==0:
       for i in range((LENGTH//3) -1):
         ListNum.append(num[:3])
         num=num[3:]
   elif LENGTH%3==1:
         ListNum.append(num[0])
         num=num[1:]
         for i in range(LENGTH//3):
            ListNum.append(num[:3])
            num=num[3:]
   elif LENGTH%3==2:
               ListNum.append(num[0])
               num=num[1:]
               ListNum.append(num[0])
               num=num[1:]
               for i in range(LENGTH//3):
                     ListNum.append(num[:3])
                     num=num[3:]
   return ListNum
def verbalizeNumber(numL):
   listVerbal=['septillion', 'sextillion', 'quintillion', 'quadrillion', 'trilion', 'billion', 'million', 'thousand' ]

   if len(numL) != 1:
      remain=LENGTH%3
      newLENGTH=LENGTH+remain
      index_listVerbal=int((27-newLENGTH)/3) # if u need to see what index i is, i must be integer not floating point 
      new_listVerbal=listVerbal[index_listVerbal:]
      for item in numL:
          if item =='000':
             numL[numL.index(item)]='0'
          elif item[:2]=='00':
            numL[numL.index(item)]=item[2] # this for loop, i will get the new list without '000' as item
      print(numL)
##      print(index_listVerbal)
##      print(new_listVerbal)
##      for item in numL:
##         numL1.append(int(item))
##      print(numL1)
##      print('1234567890')
      for i in range( len(new_listVerbal)):
         for item in numL:
            if item==numL[i]:
               if len(item)==3:
                   print('{0:>4}  {1:<20}'.format(numL[i], new_listVerbal[i]))
               elif len(item)==2:
                     print('{0:>5}  {1:<20}'.format(numL[i], new_listVerbal[i]))
               elif len(item)==1:
                     print('{0:>6}  {1:<20}'.format(numL[i], new_listVerbal[i]))
      print('{0:>4}'.format(numL[len(numL)-1]))
   else:
      print(numL[0])
main()

      

