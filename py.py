import multiprocessing as mp 
import time as t



if __name__ == "__main__":
    st = t.time()
    array = [x for x in range (1, 1000000)]
    pool = mp.Pool(processes=mp.cpu_count())
    # result = pool.map(sum, [array[i:i+mp.cpu_count()] for i in range(0, len(array), mp.cpu_count())])
    # pool.close()
    # pool.join()
    ed = t.time()
    # print(sum(result), ed-st)
    print(sum(array), ed-st)
