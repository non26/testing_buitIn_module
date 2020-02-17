def main():
   getInput()
   calculateH(h0,v0)
   calculateT(Hafter_max)
def getInput():
   h=float(input('Enter the initial height of the ball:  '))
   v=float(input('Enter the initial velocity of the ball:  '))
   isValid(h,v)
   global h0
   h0=h
   global v0
   v0=v
def isValid(h0,v0):
   if h0>0 and v0>0:
      pass
   else:
      print('ERROR')
def calculateH(h0,v0):
   h_max=h0+(v0**2)/32-16*(v0/32)**2
   global Hafter_max
   Hafter_max=h_max
   print('The maximum height of the ball is {0:,.2f} feet'.format(h_max))
def calculateT(Hafter_max):
   t=((4*16*Hafter_max)**0.5)/32
   print('The ball will hit the ground after approximately {0:,.2f} secounds'.format(t))
main()
   
   
   
   
   
