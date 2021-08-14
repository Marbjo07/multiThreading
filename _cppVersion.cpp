#include <iostream>
#include <thread>
#include <string>
#include <future>
#include <cmath>
#include <chrono>
#include <iomanip>
#include <math.h>

long double calc(int Z, int index, int numberOfThreads)
{
    long double sum = 0;
    for (int n = index; n <= Z; n += numberOfThreads) {
        
        sum += (std::pow((-1), n)) * (1 / double(n + 1));
    }

    return sum;
}



int main()
{
    const int numberOfThreads = 10;
    long double totalSum = 0;
    unsigned long long int numberOfIterations = 10000000000;

    std::future<long double> threads[numberOfThreads];

    auto start = std::chrono::high_resolution_clock::now();

    std::cout << "Starting threads" << std::endl;

    for (int i = 0; i < numberOfThreads; i++) {
        threads[i] = std::async(calc, numberOfIterations, i, numberOfThreads);
    }

    for (int i = 0; i < numberOfThreads; i++) {
        //std::cout << "Thread " << i << " is done!" << std::endl;
        totalSum += threads[i].get();
    }

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::high_resolution_clock::now() - start).count();


    std::cout << "Duration: " << duration << " in milliseconds: " << duration / 1000 << std::endl;

    
    std::cout << std::setprecision(50) << "Output: " << totalSum << " \n \\
        Dif:" << totalSum - log (double(2)) << std::endl;

    return 0;
}
