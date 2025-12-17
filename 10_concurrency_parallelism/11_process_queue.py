from multiprocessing import Process,Queue

def update_queue(queue):
    queue.put("Hi from Queue")

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=update_queue,args=(q,))
    p1.start()
    p1.join()
    print(q.get())