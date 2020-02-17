def main(): #0-13-030657-6
   isbn=input('Enter a ISBN with hypens: ')
   x,y=check(isbn)
   validator(x,y)
def check(isbn):
   listBlock=[]
   for i in range(4):
      index=isbn.find('-')
      if index==-1:
         listBlock.append(isbn)
         break
      num=isbn[:index]
      value=True
      for j in num:
         if j in '0123456789Xx':
            listBlock.append(j)
         else:
            value=False
            break
      isbn=isbn[index+1:]
   print(value, listBlock)
   return value,listBlock
def validator(value,listBlock):
   if value==True:
      sum1=0
      if listBlock[9]==('X','x'):
         listBlock[9]='10'
         for n in range(1,11):
            multi=n*int(listBlock[10-n])
            sum1=sum1+multi    
      else:
         for n in range(1,11):
            multi=n*int(listBlock[10-n])
            sum1=sum1+multi
      if sum1%11==0:
            print('The number is valid.')
      else:
            print('The number is\'t valid.')
   else:
      print('first nine digits is not all number.')
main()         
         
      
         
      











   
