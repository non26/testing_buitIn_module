print('CAFEINE VALUES')
cafe1=130
cafe3=130 #start cafe3=130 bc h start at 1
h1=1000000000
for h in range(1,25):
   cafe1=cafe1*0.87
   cafe3=cafe3*0.87+130
   if cafe1 <= 65 and h1>h:
      h1=h
      print('One cup:less than 65 mg. will after {0} hours'.format(h1))
   if h==24:
      print('One cup: {0:.2f} mg. will remain after 24 hours'.format(cafe1))
      print('Hourly cups: {0:.2f} mg. will remain after 24 hours'
            .format(cafe3))
      break
   
