import heapq
from typing import Dict, List
from collections import Counter

# numbers = [2, 1, 3, 4, 5, 9, 8, 7]

# heapq.heapify(numbers)
# print(numbers)


def top_n_ranling(words: List[str], n: int) -> List[str] :
    counter_word = Counter(words)
    # print(counter_word)
    
    data = [(-counter_word[word], word) for word in counter_word]
    # print(data)
    heapq.heapify(data)
    # print(data)
    return [heapq.heappop(data)[1] for _ in range(n)]

if __name__ == '__main__':
    w = ['python', 'c', 'java', 'go', 'python', 'c', 'go', 'python']
    print(top_n_ranling(w, 4))
