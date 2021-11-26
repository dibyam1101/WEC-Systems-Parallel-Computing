import multiprocessing as mp 

array = list(map(int, input().split()))     # input array


#Keep summing a certain number of array elements paralelly until you get to easily manageable numbers
while(len(array)>100):        
    cpu_count = mp.cpu_count()

    #Using a multiprocessing pool to sum the array elements
    pool = mp.Pool(processes=cpu_count)
    #Mapping every 'cpu_count' elements of to the sum of these 'cpu_count' elements and running multiple such 
    #processes in parallel. Untimately, we keep reducing the array size by a factor of 'cpu_count' untill it 
    #becomes manageable

    array = pool.map(sum, [array[i:i+cpu_count] for i in range(0, len(array), cpu_count)])
    pool.close()
    pool.join()
                       
print(sum(array))



