#Program to take input and sum an array serially

def serial_sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

arr = list(map(int, input().split()))
print(serial_sum(arr))
