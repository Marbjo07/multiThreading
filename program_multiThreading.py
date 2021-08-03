import math
from threading import Thread
import time

numberOfThreads = 500

start = time.time()

tempsum = [0] * 50

n = int(1 * 10 ** 10)

output = 0

def work(index):
    calc = 0
    
    k = index + 1 
    while k + numberOfThreads <= n / numberOfThreads:
        calc += ((-1) ** (k - 1)) * (1 / (k))
        k += numberOfThreads

    tempsum[index % len(tempsum)] += calc
    print(f'Thread {index} {index % len(tempsum)} is done!')
    return None

threads = [None] * numberOfThreads

for i in range(numberOfThreads):
    

    #print(f'Thread {i} has started!')

    threads[i] = Thread(target=work, args=[i])
    threads[i].start()

for i in range(numberOfThreads):
    threads[i].join()


output = sum(tempsum)

print("Math.log(2):", math.log(2))
print("Output:     ", output)
print("Dif:        ",math.log(2) - output)

print("Time:       ", time.time() - start)





{
#import math
#from threading import Thread
#import time
#from queue import Queue
#from termcolor import colored
#numberOfThreads = 5
#queues = [Queue() for n in range(numberOfThreads)]
#
#start = time.time()
#
#
#n = int(1 * 10 ** 5)
#
##x1 = [0] * int(n / 2)
##def work1():
##    for k in range(1, len(x1)):
##        x1[k] = ((-1) ** (k - 1)) * 1 / k
#
#
#
#def work(startIndex, endIndex, que, name):
#    output = [0] * (endIndex - startIndex)
#    for k in range(startIndex, endIndex):
#        output[k - startIndex] = ((-1) ** (k - 1)) * 1 / k
#    
#    print(f'Thread {name} is done!')
#    que.put(output)
#    return None
#
#
#
#
#threads = [None] * numberOfThreads
#for i in range(numberOfThreads):
#    startIndex = int(n / numberOfThreads * (i)) + 1
#    endIndex = int(n / numberOfThreads * (i + 1))
#    q = queues[i]
#
#    print(f'Thread {i} has started!')
#
#    threads[i] = Thread(target=work, args=[startIndex, endIndex, q, i])
#    #t2 = threading.Thread(target=work2, args=[])
#    threads[i].start()
#
#    #t2.start()
#
#for i in range(numberOfThreads):
#    threads[i].join()
#
#output = 0
#for i in range(numberOfThreads):
#    result = sum(queues[i].get())    
#    if result < 0:
#        print('Thread ', i,':   ', result, sep="")
#    else:
#        print('Thread ', i,':    ', result, sep="")
#    output += result
#
#
#print("Math.log(2):", math.log(2))
#print("Output:     ", output)
#print("Dif:        ",math.log(2) - output)
#
#print("Time:       ", time.time() - start)
#
#
}