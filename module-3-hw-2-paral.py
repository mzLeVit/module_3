import time
from concurrent.futures import ProcessPoolExecutor
import os

def factorize_number(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def factorize(numbers):
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        results = list(executor.map(factorize_number, numbers))
    return results

def main():
    # Тест
    numbers = [128, 255, 99999, 10651060]

    start_time_parallel = time.time()
    results_parallel = factorize(numbers)
    end_time_parallel = time.time()

    print("Results (parallel):", results_parallel)
    print("Execution time (parallel):", end_time_parallel - start_time_parallel)

if __name__ == "__main__":
    main()
