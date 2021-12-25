from collections import deque

if __name__ == '__main__':
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    print(q.pop())
    print(q)
    print(q.popleft())