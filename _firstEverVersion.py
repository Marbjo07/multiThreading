import math
from threading import Thread
import time
from queue import Queue
numberOfThreads = 500
queues = [Queue() for n in range(numberOfThreads)]

start = time.time()

n = int(1 * 10 ** 7)

def work(startIndex, endIndex, que, name):
    output = [0] * (endIndex - startIndex)
    for k in range(startIndex, endIndex):
        output[k - startIndex] = ((-1) ** (k - 1)) * 1 / k
    
    print(f'Thread {name} is done!')
    que.put(output)
    return None


threads = [None] * numberOfThreads
for i in range(numberOfThreads):
    startIndex = int(n / numberOfThreads * (i)) + 1
    endIndex = int(n / numberOfThreads * (i + 1))
    q = queues[i]

    print(f'Thread {i} has started!')

    threads[i] = Thread(target=work, args=[startIndex, endIndex, q, i])
    threads[i].start()


for i in range(numberOfThreads):
    threads[i].join()

output = 0
for i in range(numberOfThreads):
    result = sum(queues[i].get())    
    if result < 0:
        print('Thread ', i,':   ', result, sep="")
    else:
        print('Thread ', i,':    ', result, sep="")
    output += result


print("Math.log(2):", math.log(2))
print("Output:     ", output)
print("Dif:        ", math.log(2) - output)
print("Time:       ", time.time() - start)