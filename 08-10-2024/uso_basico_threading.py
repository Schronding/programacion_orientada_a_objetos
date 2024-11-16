import numpy
import threading
import time

total_numbers_A = [int for int in range(90000000)]


total_numbers_B = [int for int in range(90000000, 180000000)]


print(len(total_numbers_A), len(total_numbers_B))

list_of_AB = [0] * len(total_numbers_A)

def sum_up_to_a_point(list1, list2, list3, start, finish, step):
    for index in range(start, finish, step):
        list3[index] =  list1[index] +  list2[index]

start_serial = time.time()
sum_up_to_a_point(total_numbers_A, total_numbers_B, list_of_AB, 0, max(len(total_numbers_A), len(total_numbers_B)), 1)
finish_serial = time.time()
delta_of_serial = finish_serial - start_serial
print(f"Ts:     {delta_of_serial}s")

list_of_BA = [0] * len(total_numbers_A)

start_parallel = time.time()

first_half = threading.Thread(target = sum_up_to_a_point(total_numbers_A, total_numbers_B, list_of_BA, 0, int(  len(total_numbers_A) / 2), 1))
second_half = threading.Thread(target = sum_up_to_a_point(total_numbers_A, total_numbers_B, list_of_BA, int(    len(total_numbers_A) / 2    ), len(total_numbers_A), 1))

first_half.start()
second_half.start()

finish_parallel = time.time()

first_half.join()
second_half.join()
delta_of_parallel = finish_parallel - start_parallel

#print(AB_on1st_thread[:100])
#print(AB_on2nd_thread[:100])
print(f"Tp: {delta_of_parallel}s")

speed_up = delta_of_serial / delta_of_parallel
print(f"Speedup:    {speed_up}")

def is_equal(list1, list2):
    it_is = True
    index = 0
    max_index = max(len(list1), len(list2))
    while list1[index] == list2[index] and index < max_index - 1:
        index += 1
    if index != max_index - 1:
        it_is = False
    return it_is

print(is_equal(list_of_AB, list_of_BA))