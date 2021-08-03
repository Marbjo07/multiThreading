import math
from threading import Thread
import time

numberOfThreads = 500

numberOfIterations = int(1 * 10 ** 10)

writeTime = 0.01

output = 0

start = time.time()

def work(index):
    calc = 0
    global output 
    k = index + 1
    while k + numberOfThreads <= numberOfIterations / numberOfThreads:
        calc += ((-1) ** (k - 1)) * (1 / (k)) 
        k += numberOfThreads

    waitTime = writeTime * index - (time.time() - start)

    if waitTime > 0:
        time.sleep(waitTime)
   
    output += calc

    print(f'Thread {index} is done!')
    return None


threads = [None] * (numberOfThreads)

for i in range(numberOfThreads):    
    threads[i] = Thread(target=work, args=[i])
    threads[i].start()

for i in range(numberOfThreads):
    threads[i].join()

print("Math.log(2):", math.log(2))
print("Output:     ", output)
print("Dif:        ", math.log(2) - output)
print("Time:       ", time.time() - start)