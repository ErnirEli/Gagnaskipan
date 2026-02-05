from stack import Stack
from myqueue import Queue


b = Stack()
b.push(1)
b.push(2)
b.push(3)
print(b)
print(b.is_empty())
print(b.top())
print(b.pop())
print(b)
b.pop()
b.pop()
print(b)
print(b.is_empty())







# a = Queue(4)

# a.enqueue(1)
# a.dequeue()
# a.enqueue(1)
# a.enqueue(2)
# a.enqueue(3)
# a.enqueue(4)
# a.enqueue(5)

# print(a)

# a.dequeue()
# a.dequeue()
# a.dequeue()
# print(a)

# a.enqueue(1)
# a.dequeue()
# print('sigma: ', a)
# a.enqueue(2)
# a.enqueue(3)
# a.enqueue(4)
# print(a)
# print(a.is_full())

# a.enqueue(5)
# print(a)
# a.enqueue(6)
# a.enqueue(7)


# print(a.front())
# print(a.is_full())

# a.enqueue(8)
# print(a)