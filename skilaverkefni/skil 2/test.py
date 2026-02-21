from deque import Deque
from stack import Stack
from queue import Queue
from sll import SLList
from dll import DLList

#######################################################################################
#
# SLL test
#
#######################################################################################
def sll_test():
    A = SLList()
    try:
        A.pop_back()
        raise IndexError('Pop á að raisa IndexError ef listinn er tómur')
    except IndexError:
        pass        
    try:
        A.pop_front()
        raise IndexError('Pop á að raisa IndexError ef listinn er tómur')
    except IndexError:
        pass
    A.push_front(10)
    A.push_back(20)
    A.push_front(5)
    A.push_back(25)

    if str(A) != '[5, 10, 20, 25]':
        raise ValueError(f'Listinn á að vera [5, 10, 20, 25] en er {A}')
    

    if len(A) != 4:
        raise ValueError(f'Lengdin á listanum á að vera 4 en er {len(A)}')
    

    if A.is_empty():
        raise ValueError(f'Is empty er True en á að vera False')
    

    for k in range(4):
        A.pop_back()

    if not A.is_empty():
        raise ValueError(f'Is empty er True en á að vera False')
    
    A.push_front(10)
    A.push_back(20)
    A.push_front(5)
    A.push_back(25)
    for k in range(4):
        A.pop_front()

    A.push_front(10)
    A.push_back(20)
    A.push_front(5)
    A.push_back(25)

    a = A.front()
    b = A.back()

    if a != 5:
        raise ValueError(f'front virkar ekki, á að vera 5 en er {a}')
    
    if b != 25:
        raise ValueError(f'back virkar ekki, á að vera 25 en er {b}')
    print(A)

    for k in range(4):
        A.pop_front()

    A.push_back(10)
    A.push_back(20)
    A.push_back(30)
    return A


#######################################################################################
#
#
#
#######################################################################################
def dll_test():
    A = DLList()
    try:
        A.pop_back()
        raise IndexError('Pop á að raisa IndexError ef listinn er tómur')
    except IndexError:
        pass        
    try:
        A.pop_front()
        raise IndexError('Pop á að raisa IndexError ef listinn er tómur')
    except IndexError:
        pass
    A.push_front(10)
    A.push_back(20)
    A.push_front(5)
    A.push_back(25)

    if str(A) != '[5, 10, 20, 25]':
        raise ValueError(f'Listinn á að vera [5, 10, 20, 25] en er {A}')
    

    if len(A) != 4:
        raise ValueError(f'Lengdin á listanum á að vera 4 en er {len(A)}')
    

    if A.is_empty():
        raise ValueError(f'Is empty er True en á að vera False')
    

    for k in range(4):
        A.pop_back()

    if not A.is_empty():
        raise ValueError(f'Is empty er True en á að vera False')
    
    A.push_front(10)
    A.push_back(20)
    A.push_front(5)
    A.push_back(25)
    for k in range(4):
        A.pop_front()

    A.push_front(10)
    A.push_back(20)
    A.push_front(5)
    A.push_back(25)

    a = A.front()
    b = A.back()

    if a != 5:
        raise ValueError(f'front virkar ekki, á að vera 5 en er {a}')
    
    if b != 25:
        raise ValueError(f'back virkar ekki, á að vera 25 en er {b}')
    

    k = A.front_pos()
    k = A.next_pos(k)
    A.get_at(k)
    A.remove(k)
    n = A.back_pos()
    A.replace(n, 69)
    n = A.prev_pos(n)
    h = A.front_pos()
    A.replace(n, 67)
    A.replace(h, 14)

    A.insert_after(n, 68)
    h = A.insert_before(h, 9)
    A.get_at(h)
    h = A.prev_pos(h)
    if str(A) != '[9, 14, 67, 68, 69]':
        raise ValueError(f'listi á að vera [9, 14, 67, 68, 69] ern er {A}')
    print(A)

    for k in range(5):
        A.pop_front()

    A.push_back(10)
    A.push_back(20)
    A.push_back(30)
    return A


#######################################################################################
#
# Stack - DLL
#
#######################################################################################
def stack_dll():
    S = DLList()
    A = Stack(S)

    if A.is_empty():
        print('is_empty virkar þegar listi er tómur')
    try:
        A.top()
        raise ValueError('top() á að raisa error ef listi er tómur')
    except:
        pass
    try:
        A.pop()
        raise InterruptedError('Pop raisaði ekki error á tóman lista')
    except:
        pass

    A.push(5)
    A.push(10)
    A.push(15)
    A.push(20)
    A.push(25)
    print(A)
    print(len(A))
    print(A.top())
    for k in range(3):
        A.pop()
    print(A.top())
    print(A)
    print(len(A))
    A.pop()
    A.pop()
    print(A)
    print(len(A))

    A.push(30)
    A.push(20)
    A.push(10)
    return A


#######################################################################################
#
# Stack - SLL
#
#######################################################################################
def stack_sll():
    S = SLList()
    A = Stack(S)

    if A.is_empty():
        print('is_empty virkar þegar listi er tómur')
    try:
        A.top()
        raise ValueError('top() á að raisa error ef listi er tómur')
    except:
        pass
    try:
        A.pop()
        raise InterruptedError('Pop raisaði ekki error á tóman lista')
    except:
        pass

    A.push(5)
    A.push(10)
    A.push(15)
    A.push(20)
    A.push(25)
    print(A)
    print(len(A))
    print(A.top())
    for k in range(3):
        A.pop()
    print(A.top())
    print(A)
    len(A)
    A.pop()
    A.pop()
    len(A)

    A.push(30)
    A.push(20)
    A.push(10)
    return A




#######################################################################################
#
# Queue - DLL
#
#######################################################################################
def queue_dll():
    S = DLList()
    A = Queue(S)

    if A.is_empty():
        print('is_empty virkar þegar listi er tómur')
    try:
        A.front()
        raise ValueError('top() á að raisa error ef listi er tómur')
    except:
        pass
    try:
        A.pop()
        raise InterruptedError('Pop raisaði ekki error á tóman lista')
    except:
        pass

    A.enqueue(5)
    A.enqueue(10)
    A.enqueue(15)
    A.enqueue(20)
    A.enqueue(25)
    print(A)
    print(len(A))
    print(A.front())
    for k in range(3):
        A.dequeue()
    print(A.front())
    print(A)
    print(len(A))
    A.dequeue()
    A.dequeue()
    print(A)
    print(len(A))

    A.enqueue(10)
    A.enqueue(20)
    A.enqueue(30)
    return A


#######################################################################################
#
# Queue - Sll
#
#######################################################################################
def queue_sll():
    S = SLList()
    A = Queue(S)

    if A.is_empty():
        print('is_empty virkar þegar listi er tómur')
    try:
        A.front()
        raise ValueError('top() á að raisa error ef listi er tómur')
    except:
        pass
    try:
        A.pop()
        raise InterruptedError('Pop raisaði ekki error á tóman lista')
    except:
        pass

    A.enqueue(5)
    A.enqueue(10)
    A.enqueue(15)
    A.enqueue(20)
    A.enqueue(25)
    print(A)
    print(len(A))
    print(A.front())
    for k in range(3):
        A.dequeue()
    print(A.front())
    print(A)
    print(len(A))
    A.dequeue()
    A.dequeue()
    print(A)
    print(len(A))

    A.enqueue(10)
    A.enqueue(20)
    A.enqueue(30)
    return A


#######################################################################################
#
# Deque - DLL
#
#######################################################################################
def deque_dll():
    S = DLList()
    A = Deque(S)

    if A.is_empty():
        print('is_empty virkar þegar listi er tómur')
    try:
        A.front()
        raise ValueError('top() á að raisa error ef listi er tómur')
    except:
        pass
    try:
        A.pop()
        raise InterruptedError('Pop raisaði ekki error á tóman lista')
    except:
        pass

    A.appendleft(5)
    A.append(10)
    A.appendleft(15)
    A.append(20)
    A.appendleft(25)
    print(A)
    print(len(A))
    print(A.front())
    print(A.back())
    for k in range(3):
        A.popleft()
    print(A.front())
    print(A)
    print(len(A))
    A.popleft()
    A.popleft()
    print(A)
    print(len(A))

    A.append(10)
    A.append(20)
    A.append(30)
    return A


#######################################################################################
#
# Deque - SLL
#
#######################################################################################
def deque_sll():
    S = SLList()
    A = Deque(S)

    if A.is_empty():
        print('is_empty virkar þegar listi er tómur')
    try:
        A.front()
        raise ValueError('top() á að raisa error ef listi er tómur')
    except:
        pass
    try:
        A.pop()
        raise InterruptedError('Pop raisaði ekki error á tóman lista')
    except:
        pass

    A.appendleft(5)
    A.append(10)
    A.appendleft(15)
    A.append(20)
    A.appendleft(25)
    print(A)
    print(len(A))
    print(A.front())
    print(A.back())
    for k in range(3):
        A.popleft()
    print(A.front())
    print(A)
    print(len(A))
    A.popleft()
    A.popleft()
    print(A)
    print(len(A))

    A.append(10)
    A.append(20)
    A.append(30)
    return A




#######################################################################################
#
#
#
#######################################################################################


A = sll_test()
B = dll_test()
C = stack_dll()
D = stack_sll()
E = queue_dll()
F = queue_sll()
G = deque_dll()
H = deque_sll()

if str(A) == str(B) and str(A) == str(C) and str(A) == str(D) and str(A) == str(E) and str(A) == str(F) and str(A) == str(G) and str(A) == str(H):
    print(A, B, C, D, E, F, G, H)


A = SLList()
B = A.push_front(50)
A.pop_front()
print(A)
print(len(A))
print(A._tail)
A.push_back(14)
A.push_back(15)
print(A._tail)
print(A._head.next)

