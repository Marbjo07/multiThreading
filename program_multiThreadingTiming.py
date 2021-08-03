import math
from threading import Thread
import time

numberOfThreads = 500
n = int(1 * 10 ** 10)
writeTime = 0.01
prevWriteTime = writeTime

writeTimeUpdates = 0


output = 0

start = time.time()

def work(index):
    calc = 0
    global output 
    global prevWriteTime
    k = index + 1
    while k + numberOfThreads <= n / numberOfThreads:
        calc += ((-1) ** (k - 1)) * (1 / (k)) 
        k += numberOfThreads

    waitTime = writeTime * index - (time.time() - start)

    if waitTime > 0:
        time.sleep(waitTime)
    

    #if index % (numberOfThreads / writeTimeUpdates) == 1:
    #    f = (time.time() - start) 
#
    #    output += sum(calcArr)
#
    #    w = ((time.time() - start) - f)
    #    d = prevWriteTime -  w
    #    
    #    print(prevWriteTime, end= " => ")
#
    #    if not (prevWriteTime - d/11 <= 0):
    #        prevWriteTime -= d / 11
    #    else:
    #        prevWriteTime += d / 10
#
    #    
    #    print(prevWriteTime, w)

    #f = time.time()
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
print("Dif:        ",math.log(2) - output)
print("Time:       ", time.time() - start)