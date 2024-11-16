import seaborn as sb
import threading
import random
import queue

threads = queue.Queue(4)
inversed_threads = queue.Queue(4)
local_buckets = queue.Queue(10)

data = []
for _ in range(100):
    data.append(random.randrange(0, 99))

def bucket_numbers(start, end):
    dL = threading.local()
    dL.buckets = {}
    for index in range(11):
        dL.buckets[index] = 0
    for number in data[start : end]:
        bucket = number // 10
        dL.buckets[bucket] += 1
    local_buckets.put(dL.buckets)
    print(dL.buckets)

for index in range(4):
    start = 25 * index
    end = 25 * (index + 1)
    threads.put(threading.Thread(target = bucket_numbers, args = (start, end), name = 'hilo' + str(index)))

for _ in range(threads.qsize()):
    current_thread = threads.get()
    print(current_thread)
    current_thread.start()
    inversed_threads.put(current_thread)

for _ in range(threads.qsize()):
    inv_current_thread = inversed_threads.get()
    inv_current_thread.join()

