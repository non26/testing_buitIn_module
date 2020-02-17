############################## Global variable
##def f():
##   print(x)
####x=2
##f()
##x=2
############################## Function as Parameter.
##def g():
##    print("Hi, it's me 'g'")
##    print("Thanks for calling me")
##def f(func):
##    print("Hi, it's me 'f'")
##    print("I will call 'func' now")
##    func
##f(g())
##print('################################################################################')
##def g():
##    print("Hi, it's me 'g'")
##    print("Thanks for calling me")  
##def f(func):
##    print("Hi, it's me 'f'")
##    print("I will call 'func' now")
##    func()          
##f(g)
##print('################################################################################')
##def g():
##    print("Hi, it's me 'g'")
##    print("Thanks for calling me")
##    return 5
##def f(func):
##    print("Hi, it's me 'f'")
##    print("I will call 'func' now")
##    print(func )     
##f(g())
############################## Function returning Function
##def polynomial_creator(*coefficients):
##    """ coefficients are in the form a_0, a_1, ... a_n 
##    """
##    def polynomial(x):
##        res = 0
##        for index, coeff in enumerate(coefficients):
##            res += coeff * x** index
##        return res
##    return polynomial
##p1 = polynomial_creator(4)
##p2 = polynomial_creator(2, 4)
##p3 = polynomial_creator(2, 3, -1, 8, 1)
##p4  = polynomial_creator(-1, 2, 1)
####print(p3)
##for x in range(-2, 2, 1):
##    print(x, p1(x), p2(x), p3(x), p4(x))
##############################  A simple Decorator
##def our_decorator(func):
##    def function_wrapper(x):
##        print("Before calling " + func.__name__)
##        func(x)
##        print("After calling " + func.__name__)
##    return function_wrapper
##def foo(x):
##    print("Hi, foo has been called with " + str(x))
##print("We call foo before decoration:")
##foo("Hi")    
##print("We now decorate foo with f:")
##A= our_decorator(foo)
##print("We call foo after decoration:")
##A(42)
#########################################
##def our_decorator(func):
##    def function_wrapper(x):
##        print("Before calling " + func.__name__)
##        func(x)
##        print("After calling " + func.__name__)
##    return function_wrapper
##@our_decorator
##def foo(x):
##    print("Hi, foo has been called with " + str(x))
##foo("Hi")
##del our_decorator
##foo(20)
#########################################
##def evening_greeting(func):
##    def function_wrapper(x):
##        print("Good evening, " + func.__name__ + " returns:")
##        func(x)
##    return function_wrapper
##def morning_greeting(func):
##    def function_wrapper(x):
##        print("Good morning, " + func.__name__ + " returns:")
##        func(x)
##    return function_wrapper
##@evening_greeting
##def foo(x):
##    print(42)
##foo("Hi")
#########################################
def foo(a, b, c):
  print (a)
  print (b)
  print (c)
kwargs = {'a':1,'b':2,'c':3}
foo(**kwargs)







    
