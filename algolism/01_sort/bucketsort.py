import random
from typing import List, Sized

"""
bucketソート
リストをbucketsへ分割し、各々でinsertionソートし、最後に結合
"""

def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
                numbers[j+1] = numbers[j]
                j -= 1
        numbers[j+1] = temp
            
    return numbers

def bucket_sort(numbers:List[int]) -> List[int]:
    max_num = max(numbers)
    len_numbers = len(numbers)
    bucket_size = max_num // len_numbers
    
    buckets = [[] for _ in range(bucket_size)]
    # print(buckets)
    
    for num in numbers:
        i = num // bucket_size
        if i != bucket_size:
            buckets[i].append(num)
        else:
            buckets[bucket_size-1].append(num)
    
    # print(buckets)
    
    for i in range(bucket_size):
        insertion_sort(buckets[i])
        
    result = []
    
    for i in range(bucket_size):
        result += buckets[i]
    
    return result

if __name__ == '__main__':
    # nums = [random.randint(1, 1000) for _ in range(10)]
    nums = [1, 5, 28, 25, 100, 52, 27, 91, 22, 99]
    print(bucket_sort(nums))
    