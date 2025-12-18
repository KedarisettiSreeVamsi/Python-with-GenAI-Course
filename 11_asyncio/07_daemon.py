import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2)

thread = threading.Thread(target=monitor_tea_temp,daemon=True)
thread.start()
time.sleep(4)
print("Main program done")