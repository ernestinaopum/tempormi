import concurrent.futures

def task1(x):
    print(f"Task 1: {x}")
    return x**2

def task2(x):
    print(f"Task 2: {x}")
    return x**3

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for i in range(5):
        futures.append(executor.submit(task1, i))
        futures.append(executor.submit(task2, i))

    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()
            print(result)
        except Exception as e:
            print(f"Error: {e}")
