##L1=[1,2,3,4]
##for i in L1:
##   print(i)
##iterator=iter(L1)
##print(iterator,'*') ## list object
##print(next(iterator))
##print(next(iterator))
##print(next(iterator))
##print(next(iterator))
##print(next(iterator))## Error appears
##########################################
##s1=set([1,2,3,4])
##print(s1)
##for i in s1:
##   print(i)
###########################################
##def city_generator():
##    yield"London"
##    yield("Hamburg")
##    yield("Konstanz")
##    yield("Amsterdam")
##    yield("Berlin")
##    yield("Zurich")
##    yield("Schaffhausen")
##    yield("Stuttgart")
##city=city_generator()
##print(next(city))
##print(next(city))
##print(next(city))
##print(next(city))
##print(next(city))
##print(next(city))
##print(next(city))
##print(next(city))
##print(city)
##x=city_generator()
##print(next(x))
##print(next(city))
############################################
##def fibonacci(n):
##    """ A generator for creating the Fibonacci numbers """
##    a, b, counter = 0, 1, 0
##    while True:
##        if (counter > n): 
##            return
##        yield a
##        a, b = b, a + b
##        counter += 1
##f = fibonacci(5)
##for x in f:
##    print(x, " ", end="") #
##x=fibonacci(5)
##for i in range(6):
##    print(next(x))
##print()
#####next example endlesscreturning
##def fibonacci():
##    """Generates an infinite sequence of Fibonacci numbers on demand"""
##    a, b = 0, 1
##    while True:
##        yield a
##        a, b = b, a + b
##f = fibonacci()
##counter = 0
##for x in f:
##    print(x, " ", end="")
##    counter += 1
##    if (counter > 10):  #t
##        break 
##print()
####################################Using a return statement in a Generator
##def gen():
##   yield 2
##   yield 3
##   return 42
##g=gen()
####print(next(g))
####print(next(g))
####print(next(g))
##for x in g:
##   print(x)
###################################Send method
##def simple_coroutine():
##   print("coroutine has been started!")
##   x = yield
##   print("coroutine received: ", x)
##cr = simple_coroutine()
##next(cr)
####print(next(cr))
##cr.send("Hi")
################ another example
##def infinite_looper(objects):
##    count = 0
##    while True:
##        if count >= len(objects):
##            count = 0
##        message = yield objects[count]
##        if message != None:
##            count = 0 if message < 0 else message
##        else:
##            count += 1
##x=infinite_looper("A string with some words")
##next(x)
##print(x.send(9)) #w #send method sends 9 to count
##c=x.send(9)
##print(c)#w
##########################################yield from
def cities():
    for city in ["Berlin", "Hamburg", "Munich", "Freiburg"]:
        yield city
def squares():
    for number in range(10):
        yield number ** 2
def generator_all_in_one():
    for city in cities():
        yield city
    for number in squares():
        yield number
def generator_splitted():
    yield from cities()
    yield from squares()
lst1 = [el for el in generator_all_in_one()]
lst2 = [el for el in generator_splitted()]
print(lst1 == lst2)
print(lst1)
print(lst2)












    
