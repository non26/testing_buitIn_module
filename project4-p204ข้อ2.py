def main():
   num=float(input('Enter a positive integer > 1:  '))
   minPrime,maxPrime=findPrime(num)
   print('Largest prime factor %d' % maxPrime)
   print('smallest prime factor %d' % minPrime)
def findPrime(num):
   fac=2
   listFac=[]
   while num>1:
      if num%fac==0:
         num=num/fac
         if fac not in listFac:
            listFac.append(fac)
      else:
         fac+=1
   return min(listFac), max(listFac)
main()
