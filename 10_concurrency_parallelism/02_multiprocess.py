from multiprocessing import Process
import time

def take_order(i):
    print(f"Start of chai #{i}")
    print(f"Taking order for #{i}")
    time.sleep(2)
    print(f"End of chai #{i}")

# def brew_order(i):
#     print(f"Brewing chai for #{i}")
#     time.sleep(3)

if __name__ == '__main__':
    order_process = [Process(target=take_order,args=(f"Chai maker #{i+1}",)) for i in range(3)]
    # brew_process = [Process(target=brew_order,args=(i+1,)) for i in range(3)]

    for i in order_process:
        i.start()

    for i in order_process:
        i.join()
