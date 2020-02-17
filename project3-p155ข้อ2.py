print('Quadratic Equation is ax^2 + bx + c')
a=float(input('Enter a: '))
b=float(input('Enter b: '))
c=float(input('Enter c: '))
if a != 0:
   value1=(-b+(b**2-4*a*c)**0.5)/2
   value2=(-b-(b**2-4*a*c)**0.5)/2
   print('solutions: {0:,.2f} and {1:,.2f}'.format(value1,value2))
else:
   print('This isn\'t a Quadratic Equation.')
