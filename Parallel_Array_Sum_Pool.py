import multiprocessing as mp 
import time 
import random 

array = list(map(int, input().split()))     # input array

#Using a multiprocessing pool to sum the array
start_time = time.time()
#Keep summing a certain number of array elements paralelly until you get to easily manageable numbers
while(len(array)>100):        
    cpu_count = mp.cpu_count()

    pool = mp.Pool(processes=cpu_count)
    #Mapping every 12 elements of to the sum of these 12 elements and running multiple such 
    #processes in parallel. Untimately, we keep reducing the array size by a factor of 12 untill it 
    #becomes manageable
    array = pool.map(sum, [array[i:i+cpu_count] for i in range(0, len(array), cpu_count)])
    pool.close()
    pool.join()
          
end_time = time.time()              
print(sum(array))



