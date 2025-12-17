from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some heavy numbers...")
    total = 0
    for _ in range(10**7):
        total += 1
    print("Done✅")
if __name__ == "__main__":
    start = time.time()
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]
    print(f"Total time taken: {time.time() - start:.2f}")