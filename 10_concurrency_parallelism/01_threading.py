import threading
import time

def take_order():
    for i in range(3):
        print(f"Taking order for #{i+1}")
        time.sleep(1)

def brew_chai():
    for i in range(3):
        print(f"Brewing chai for #{i+1}")
        time.sleep(3)

order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

order_thread.join()
brew_thread.join()

print("All orders have been taken and brewed!")