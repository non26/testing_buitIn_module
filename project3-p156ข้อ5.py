print('AMOUNTS DEPOSITED'.center(51))
print('Earl: $75,000.00'.ljust(17),'Larry: $165,000.00'.center(51),sep='')
print('AMOUNTS IN IRA UPON RETIREMENT'.center(51))
earl=larry=0 # At first year, Amount starts at 0 .
for y in range(1,49):
   if y<=15:
      earl=earl*1.04+5000
   else:
      earl=earl*1.04
      larry=larry*1.04+5000
print('Earl: ${0:<27,.2f}'.format(earl),'{0:<}: ${1:,.2f}'
      .format('Larry',larry),sep='')

   
