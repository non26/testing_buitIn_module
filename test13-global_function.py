##x = 3
##def f():
##    #x = 42
##    def g():
##        global x
##        x = 43
##    print("Before calling g: " + str(x))
##    print("Calling g now:")
##    g()
##    print("After calling g: " + str(x))
##    
####x = 3
##f()
##print("x in main: " + str(x))
#######################################################################
##def f():
##    x = 42
##    def g():
##        global x
##        x = 43
##    print("Before calling g: " + str(x))
##    print("Calling g now:")
##    g()
##    print("After calling g: " + str(x))
##    
##f()
##print("x in main: " + str(x))
###########################################################################
##def f():
##    x = 42
##    def g():
##        nonlocal x
##        x = 43
##    print("Before calling g: " + str(x))
##    print("Calling g now:")
##    g()
##    print("After calling g: " + str(x))
##    
##x = 3
##f()
##print("x in main: " + str(x))
#############################################################################
##def f():
##    #x = 42
##    def g():
##        global x
##        x = 43
##    print("Before calling g: " + str(x))
##    print("Calling g now:")
##    g()
##    print("After calling g: " + str(x))
##    
##x = 3
##f()
##print("x in main: " + str(x))
########################################################################
###def main():
##   def f():
##      global x
##      print(x)
##   x = 3
##   f()
###main()
##def f():
##   global x
##   print(x)
##x = 3
##f()
####################################################################
##def main():
##   def f():
##      nonlocal x
##      print(x)
##   x = 3
##   f()
##main()
##def f(): ### Traceback Error
##    nonlocal x
##    print(x)
##    
##x = 3
##f()
###########################################################################
####x=5
##def f1(): #outer function
##    x = 1 # variable defined in the outer function
##    def f2(a): #inner function
##       #will create a new variable in the inner function
##       #instead of changing the value of x of outer function
##        x = 4
##        print (a+x)
##    print (x) # prints the value of x of outer function
##    f2(2)
##f1()
################################################################
##a=5
##def f1(): #outer function
##    a = 1
##    def f2(): #outer function
####        nonlocal a
##        global a
##        a = 2
##        print (a) #prints 2
##    f2()
##    print (a) #prints 2
##f1()
##print(a)
########################################################################
##l1 = ["a","b","c"]
##l2 = [1,2,3]
##c = zip(l1, l2)
##print(list(c))
##print(list(c))
#######################################################################3



























