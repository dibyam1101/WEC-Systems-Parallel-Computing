import multiprocessing as mp
import math

def thread_sum(arr, shared_mp_sum_value):
    shared_mp_sum_value.value += sum(arr)

if __name__ == '__main__':
    arr = [x for x in range(101)]
    n = len(arr)
    processes = []
    process_count = 4
    m = n
    total_sum = mp.Value("d", 0, lock=False)    
    n = math.ceil(n/process_count)*process_count
    slice_size  = n//process_count 

    for i in range(process_count):
       
        p = mp.Process(target = thread_sum, args = [arr[i*slice_size: min(m, (i+1)*slice_size)], total_sum])
        processes.append(p)

       
        p.start()

    for p in processes:
        
        p.join()

print(total_sum.value)