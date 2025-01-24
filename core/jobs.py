import threading, time

def timer(seconds):
    run_counter = 0
    
    while True:
        time.sleep(seconds)
        run_counter += 1
        print(f"I ran for {run_counter}")

def start_timer(seconds):
    thread = threading.Thread(target=timer, args=(seconds,))
    thread.start()