p=input('Enter the amount of the loan: ')
r=input('Enter the amount of interest rate: ')
n=input('Enter the duration in months: ')
if '.' in p or p.isdigit():
   if '.' in p or p.isdigit():
      if n.isdigit():
         p=float(p)
         r=float(r)/(12*100)
         n=float(n)
         monthlypay=(p*r)/(1-(1+r)**(-n))
         totalinter=n*( monthlypay)-p
         print('Monthly payment: ${0:,.2f}'.format(monthlypay))
         print('Toatl Interest paid: ${0:,.2f}'.format(totalinter))
      else:
         print('Error')         
   else:
      print('Error:the interest rate isn\'t the number')  
else:
   print('Error:the loan isn\'t only the number')  
            
