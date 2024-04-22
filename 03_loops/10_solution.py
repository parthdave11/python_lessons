import time

wait_time = 1
max_retries = 5
attampts = 0

while attampts < max_retries:
    print("Attampts:",attampts + 1, "- wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attampts = attampts +1