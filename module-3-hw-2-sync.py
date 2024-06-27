import time

def factorize_number(n):
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def main():
    # Тест
    numbers = [128, 255, 99999, 10651060]
    start_time = time.time()

  
    results_sync = [factorize_number(n) for n in numbers]
    end_time_sync = time.time()

    print("Results (synchronous):", results_sync)
    print("Execution time (synchronous):", end_time_sync - start_time)

if __name__ == "__main__":
    main()
