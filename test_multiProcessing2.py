import time
import multiprocessing
def summing(number):
    s = 0
    for i in range(number):
        s = i*i
    return s
def summing_with_serial():
    numbers = 10000
    start = time.time()
    for i in range(numbers):
        summing(i)
    print(time.time() - start)
def summing_with_multiProcessing():
    numbers = range(10000)
    start = time.time()
    p = multiprocessing.Pool()
    p.map(summing, numbers)
    print(time.time() - start)

if __name__ == "__main__":
    summing_with_multiProcessing()
    summing_with_serial()
