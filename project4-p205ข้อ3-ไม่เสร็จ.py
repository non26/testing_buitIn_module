ListVerbalize=['septillion', 'sextillion', 'quintillion', 'quadrillion', 'trilion', 'billion', 'million', 'thousand' ]
def main():
   num=input('Enter a positive number with at most 27 digits:  ')
   verbalizeNumber(num)
def verbalizeNumber(num):
   ListNum=[]
   if len(num)<27:
      for i in range(27-len(num)):
         num='0'+num
   elif len(num)==27:
      pass
   for i in range(9):
      ListNum.append(num[:3])
      num=num[3:]
   print(ListNum)
main()
