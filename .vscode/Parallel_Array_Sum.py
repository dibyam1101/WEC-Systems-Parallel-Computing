import multiprocessing as mp 
import time 
import random 


array = []
for i in range (0, 1000000):
    array.append(random.randint(0, 1000000))

if __name__ == "__main__":
    result = []
    while(len(array)>100):
        start_time = time.time()
        cpu_count = mp.cpu_count() 
        pool = mp.Pool(processes=cpu_count)
        result = pool.map(sum, [array[i:i+cpu_count] for i in range(0, len(array), cpu_count)])
        pool.close()
        pool.join()
        end_time = time.time()        
        array = result
print(sum(result), end_time - start_time)

print(mp.cpu_count())