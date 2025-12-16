import threading
import time

def prepare_chai(type_,wait_time):
    print(f"{type_} chai is brewing...")
    time.sleep(wait_time)
    print(f"{type_} chai is ready...")

masala = threading.Thread(target=prepare_chai,args=("Masala",4))
ginger = threading.Thread(target=prepare_chai,args=('Ginger',10))

start = time.time()
masala.start()
ginger.start()
masala.join()
ginger.join()
end = time.time()
print(f"Chai brewing is completed: {end-start:.2f}")