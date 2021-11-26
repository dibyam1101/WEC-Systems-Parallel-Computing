# WEC-Systems-Parallel-Computing

## Basic Task - Sum of an array

I started off with using multiprocessing.Value() objects and multiprocessing Processes to compute the array sum paralelly. After some fiddling around with different methods, using a multiprocessing Pool seemed to be the most concise way. So I ended up  implementing both the tasks with the help of a Multiprocessing pool. Also unlike multiprocessing.Process() which allocated memory to all the processes, multiprocessing.Pool() allocates memory to only the executing processes, thus giving a major performance boost. 

The idea is simple. Reduce the array to a manageable size and compute the sum of the resulting array serially. (Creating parallel processes comes with heavy overheads and below a certain threshold, usually parallel computing to process data is overkill and would take more time than if done serially).

In my implementation, every group of a certain size is mapped to a single value corresponding to the sum of this group. For example, for a small data set [1, 2, 3, 4] with a group size 2, the following process is carried out : [(1, 2)->3 ,  (3, 4) -> 7] === [3, 7]. [(3,7) - > 10] === [10] The pool.map() function  can handle an enormous number of processes due to its ability to queue the jobs. 

The pool.Map() takes the function that we want to parallelize and an iterable as the arguments. Using the contents of the iterable as arguments (You have to pass multiple argument for which you want the functions to run parallelly). After that , depending on the return type of the function that you are calling, it returns a structure that you can use for whatever purpose you want. For this task , I repeteadly do this same process on the input list until its size becomes less than 1000. After that, I calculate the sum serially and print the sum 


This way, we end up paralellizing the array sum

The programs accetps a <b>single</b> line of the numbers you want to sum separated by line spaces (without any line breaks). It then prints the sum of the input array using an algorithm that makes use of parallel computing. 


## Second  Task - Shortest distance for all nodes from a given node

From the problem statement, it was evident that some modified form of BFS was to be used. I tried parallelizing the original BFS algorithm directly but wasn't able to get anywhere. The problem was making sure that a level gets processed first before moving on to the next level. I got the hint for the solution from the way the map function works. Essentially, if I could replace every node in the current level with its <b>unvisited neighbours</b>, then after we are done with every node, the current level would have been replace with the next level. 


         
                                   1
                                /     \
                               2       3 
                              / \     / \
                             4   5   6    7
                
                First Level -> [1]
                Repace 1 with (2, 3)
                Second Level -> [2, 3]
                Replace 2 with (4, 5) and Replace 3 with (6, 7)
                Third Level -> [(4, 5), (6, 7)] -> [4, 5, 6, 7]
                After this, nothing gets replaced since no unvisited 
                node remains. So, we get a empty level and then we
                stop(Because there are no new levels in the list)

    
The pool.map() is exactly the function for this job. In simple words, For every level, I create a nextLevel such that this nextLevel contains a list for every node in the level or simply, every node of the current level level is mapped to a a list containing <b> unvisited connected nodes </b> of that node. Finally, I flatten this new obtained level into a single list and then assign the current level to this new level. If this new level is empty, I stop. The map.Pool() takes care of paralellizing the process of finding the next level. 

In regular BFS, we process every element of the queue sequentially. In this altered algorithm, we harness the power of the map.Pool() to process all the elements in the queue at a time parallely (Note that there is no real queue in this implementation, since we simply generate the next level from the current level parallely). 

The distance from the source was computed easily using the standard BFS way ( for every node in graph[parent] if not visited, distance[node] = distance[parent] + 1.). Ultimately, I print the distances.



