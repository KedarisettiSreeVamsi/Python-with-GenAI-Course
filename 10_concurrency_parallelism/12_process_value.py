from multiprocessing import Process,Value

def increment(value):
    for _ in range(10**6):
        with value.get_lock():
            value.value += 1

if __name__ == '__main__':
    v = Value('i',0)
    processes = [Process(target=increment,args=(v,)) for _ in range(10)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(v.value)