print('CAFEINE VALUES')
h=0
cafe1=130; cafe=130 # why i used cafe1=130 bc the person drinks coffee first time at 7 a.m.
sen=True
h1=1000000
while sen==True:
   h+=1
   cafe1=cafe1*0.87+130
   cafe=cafe*(0.87)
   if cafe <= 65 and h<h1:
      h1=h
      print('One cup:less than 65 mg. will after {0} hours'.format(h))
   if h>=24:
      print('One cup: {0:.2f} mg. will remain after 24 hours'.format(cafe))
      print('Hourly cups: {0:.2f} mg. will remain after 24 hours'
            .format(cafe1))
      sen=False
   
   
