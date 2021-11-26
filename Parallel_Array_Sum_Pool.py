import multiprocessing as mp 
import time 
import random 


array = []
for i in range (0, 10000):
    array.append(random.randint(0, 10000000))

if __name__ == "__main__":
    result = []
    start_time = time.time()
    while(len(array)>1000):        
        cpu_count = 16
        pool = mp.Pool(processes=cpu_count)
        array = pool.map(sum, [array[i:i+cpu_count] for i in range(0, len(array), cpu_count)])
        pool.close()
        pool.join()
          
end_time = time.time()              
print(sum(array), end_time - start_time , len(result))

print(mp.cpu_count())