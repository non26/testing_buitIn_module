print('{0:^50s}'.format('Rule of 72'))
print('Interest'.ljust(20),'{0:<20s}'.format('Doubling Time'),'{0:<10s}'
      .format('Actual Doubling'),sep='')
print('Rate'.ljust(20),'{0:<20s}'.format('(in years)'),'{0:<10s}'
      .format('Time (in years)'),sep='')
for n in range(1,21):
   if 72%n==0:
      if n<=9:
         about=int(72/n)
         print('{0:d}{1:<19s}'.format(n,'%'),'{0:<20d}'.format(about),'{0:<10d}'
            .format(about),sep='')
      else:
         about=int(72/n)
         print('{0:d}{1:<18s}'.format(n,'%'),'{0:<20d}'.format(about),'{0:<10d}'
            .format(about),sep='')
         
   elif n<=9:
         about=72/n
         print('{0:d}{1:<19s}'.format(n,'%'),'{0:<20d}'.format(round(about))
            ,'{0:<10d}'.format(round(about)+1),sep='')
   else:
      about=72/n
      print('{0:d}{1:<18s}'.format(n,'%'),'{0:<20d}'.format(round(about))
            ,'{0:<10d}'.format(round(about)+1),sep='')
