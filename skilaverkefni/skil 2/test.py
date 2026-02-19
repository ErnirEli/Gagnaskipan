from sll import SLList
from dll import DLList
from deque import Deque


# A = SLList()

# A.push_front(13)
# A.push_back(99)
# A.push_back(10000)
# A.push_front(22)
# A.pop_back()

# for k in A:
#     print(k)
# print(A)



# B = DLList()
# B.push_front(55)
# B.push_back(11)
# B.push_back(99)
# B.push_front(-99)
# print(B)
# print('Front: ', B.front())
# print('Back: ', B.back())
# B.pop_front()
# B.pop_back()
# print(B)
# print('Front: ', B.front())
# print('Back: ', B.back())



C = SLList()
D = Deque(C)
D.appendleft(5)
D.appendleft(77)
D.append(69)
D.pop()
print(D)