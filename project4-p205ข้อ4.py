def main():
   name=input('Enter  name of item purchased: ')
   year=int(input('Enter year purchased: '))
   cost=float(input('Enter cost of item: '))
   life=int(input('Enter estimated life of item (in year): '))
   method=input('Entr method of depreciation (SL or DDB): ')
   firstOutput(name,year,cost,life,method)
   secondOutput()
##   secondOutput()
   calculate(year,cost,life,method)
def firstOutput(name,year,cost,life,method):
   print('Description: ',name)
   print('Year of purchase: ',year)
   print('Cost: ${0:,.2f}'.format(cost))
   if life==1:
      print('Estimated life:',life,'year')
   else:
      print('Estimated life:',life,'years')
   if method=='SL':
      print('Method of depreciation: Straigth-Line Method')
   else:
      print('Method of depreciation: Double-Declining Balance Method')
def secondOutput():
   print('{0:>30}{1:>30}{2:>40}'.format('Value at', 'Amount Deprec', 'Total Depreciation'))
   print('{0:>30}{1:>34}{2:>43}'.format('Beg of Yr.', 'During Year', 'to End of Year'))
def calculate(initial_year,cost,life,method):
   total=0
   for i in range(initial_year,initial_year+life):
      if method=='SL':
         if i==initial_year+life-1:
            year=i
            value=cost
            amount=value
            total=total+amount
            print('{0:<5}{1:>25,.2f}{2:>38,.2f}{3:>45,.2f}'.format(year,value, amount, total))
         else:
            year=i
            value=cost
            amount=value*(1/life)
            total=total+amount
            print('{0:<5}{1:>25,.2f}{2:>38,.2f}{3:>45,.2f}'.format(year,value, amount, total))
            cost=value*(1-1/life)
      elif method=='DDB':
         if i==initial_year+life-1:
            year=i
            value=cost
            amount=value
            total=total+amount
            print('{0:<5}{1:>25,.2f}{2:>38,.2f}{3:>45,.2f}'.format(year,value, amount, total))
         else:
            year=i
            value=cost
            amount=value*(2/life)
            total=total+amount
            print('{0:<5}{1:>25,.2f}{2:>38,.2f}{3:>45,.2f}'.format(year,value, amount, total))
            cost=value*(1-2/life)
main()












   
