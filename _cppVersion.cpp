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
    int n = index;

    char evenOrOddIndex = pow(-1, index);
    
    for (n; n <= Z + numberOfThreads; n += numberOfThreads * 2) {
        sum += (1 / double(n + 1) - 1 / double(n + numberOfThreads + 1)) * evenOrOddIndex;
    }

    if (n <= Z) {
        sum += 1 / double(n + 1) * evenOrOddIndex;
    }

    return sum;
}

int main()
{
    const int numberOfThreads = 5;
    long double totalSum = 0;
    unsigned long long int numberOfIterations = pow(10, 5);

    std::future<long double> threads[numberOfThreads];

    int totalDuration = 0;
    unsigned char numberOfTests = 1000;


    for (unsigned char k = 0; k < numberOfTests; k++) {
        auto start = std::chrono::high_resolution_clock::now();

        for (int i = 0; i < numberOfThreads; i++) {
            threads[i] = std::async(calc, numberOfIterations, i, numberOfThreads);
        }

        for (int i = 0; i < numberOfThreads; i++) {
            totalSum += threads[i].get();
        }

        using namespace std::chrono;
        auto duration = duration_cast<microseconds>(high_resolution_clock::now() - start).count();
        totalDuration += duration;

        std::cout << "Duration: " << duration << " in milliseconds: " << duration / 1000 << std::endl;

        std::cout << std::setprecision(50) << "Output: " << totalSum << " Dif:" << totalSum - log (double(2)) << std::endl;
        totalSum = 0;
    }
    std::cout << std:: setprecision(5) << "Total time in microseconds: \t" << totalDuration               << " \t Average time in microseconds: \t" << totalDuration / numberOfTests               << std::endl
                                       << "Total time in milliseconds: \t" << totalDuration / 1000        << " \t Average time in milliseconds: \t" << totalDuration / numberOfTests / 1000        << std::endl
                                       << "Total time in seconds:      \t" << totalDuration / 1000 / 1000 << " \t Average time in seconds:      \t" << totalDuration / numberOfTests / 1000 / 1000 << std::endl;
    return 0;
}
