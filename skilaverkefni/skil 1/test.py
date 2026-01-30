from dalist import DAList

def header(header):
    print()
    print()
    print('﹎'*20)
    print('│', f'{header:^36}', '│')
    print('﹊'*20)

##############################################################################################################
# __init__ Test
##############################################################################################################
header('Creation Test')

A = DAList(4)
B = DAList(4)
C = DAList(4)
D = DAList(4)

print('Create A, B, C, D\n'
'A = ', A, '\n'
'B = ', B, '\n'
'C = ', C, '\n'
'D = ', D)

##############################################################################################################
# Append Test
##############################################################################################################
header('Append Test')

print("Append")
for k in range(2):
    A.append(k)
for k in 'abcd':
    B.append(k)
if str(A) == '[0, 1]' and str(B) == '[a, b, c, d]':
    print(
    'A = ', A, '\n'
    'B = ', B, '\n'
    'C = ', C, '\n'
    'D = ', D)
else:
    raise IndexError('YO það er einhver villa í append hjá þér')

##############################################################################################################
# insert Test
##############################################################################################################
header('Insert Test')

C.insert(len(C), 1)
C.insert(len(C), 2)
if str(C) != '[1, 2]':
    raise IndexError('YO það er villa þegar þú insertar í aftasta stakið')
C.insert(1, 3)
C.insert(1, 4)
if str(C) != '[1, 4, 3, 2]':
    raise IndexError('YO það er villa þegar þú insertar í miðjuna')
D.insert(-1, 5)
if str(D) != '[5]':
    raise IndexError('YO það er villa þegar þú insertar í -1')
D.insert(99, 6)
if str(D) != '[5, 6]':
    raise IndexError('YO það er villa þegar þú insertar í 99')
D.insert(-99, 4)
if str(D) != '[4, 5, 6]':
    raise IndexError('YO það er villa þegar þú insertar í -99')


print('C =', C)
print('D =', D)


##############################################################################################################
# __len__ Test
##############################################################################################################
header('Len Test')

if len(A) == 2:
    print(
    'A = ', A, len(A), '\n'
    'B = ', B, len(B),'\n'
    'C = ', C, len(C),'\n'
    'D = ', D, len(D))
else:
    raise IndexError('YO það er villa í __len__ hjá þér')

##############################################################################################################
# __getitem__/__setitem__ Test
##############################################################################################################
header('Get/Set item Test')

print("Get 'A[1]' and 'A[2]'")
if A[0] == 0 and A[1] == 1:
    print(
    'A[0] = ', A[0], '\n'
    'A[1] = ', A[1], '\n')
else:
    raise IndexError('YO það er villa í __getitem__ hjá þér')

print("Set 'A[1] = 2'")
A[1] = 2
if A[0] == 0 and A[1] == 2:
    print(
    'A[0] = ', A[0], '\n'
    'A[1] = ', A[1])
else:
    raise IndexError('YO það er villa í __setitem__ hjá þér')

##############################################################################################################
# __delitem__ Test
##############################################################################################################
header('__delitem__ Test')

del A[1]
if A[0] == 0 and len(A) == 1:
    print(
    'A: ', A, '\n'
    'A[0] = ', A[0])

##############################################################################################################
# __iter__ Test
##############################################################################################################
header('__iter__ Test')

print('B iteration: ', B)
for k in B:
    print(k)

print()
print('A iteration:', A)
for k in A:
    print(k)

##############################################################################################################
# Clear Test
##############################################################################################################
header('Clear Test')

A.clear()
B.clear()
C.clear()
D.clear()

if str(A) == '[]' and str(B) == '[]' and str(C) == '[]' and str(D) == '[]':
    print(
    'A = ', A, '\n'
    'B = ', B, '\n'
    'C = ', C, '\n'
    'D = ', D)
else:
    raise IndexError('YO það er einhver villa í clear hjá þér')

##############################################################################################################
# Capacity Test
##############################################################################################################
header('Capacity Test')

for k in range(1, 5):
    A.append(k)
for k in 'abcde':
    B.append(k)
for k in 'UBIF':
    C.append(k)
for k in (1, 2, 3, 4, 1, 4, 1, 1):
    D.append(k)
C.insert(3, 'I')
D.insert(4, 4)

if A.capacity != 4 and B.capacity != 8:
    raise IndexError('YO það er villa í capacity þegar þú appendar')

if  C.capacity != 8 and D.capacity != 16:
    raise IndexError('YO það er villa í capacity þegar þú insertar')
else:
    print(A)
    print('Capacity:', A.capacity)
    print(B)
    print('Capacity:', B.capacity)
    print(C)
    print('Capacity:', C.capacity)
    print(D)
    print('Capacity:', D.capacity)

##############################################################################################################
# Count & Index Test
##############################################################################################################
header('Count & Index Test')

print('C:', C, 'D:', D)
print()
k = C.count('I')
n = D.count(1)
if k == 2 and n == 4:
    print("'I' in C =", k)
    print("'1' in D =", n)

else:
    raise IndexError('YO það er villa í Count hjá þér')

k = C.index('I')
n = D.index(1)
if k == 2 and n == 0:
    print("First 'I' in C =", k)
    print("First '1' in D =", n)

else:
    raise IndexError('YO það er villa í Index hjá þér')

##############################################################################################################
# Reverse Test
##############################################################################################################
header('Count & Index Test')

print('A:', A, 'B:', B)
print()

A.reverse()
B.reverse()

if str(A) != '[4, 3, 2, 1]':
    raise IndexError('YO það er villa í reverse þegar len er slétt tala')

elif str(B) != '[e, d, c, b, a]':
    raise IndexError('YO það er villa í reverse þegar len er odda tala')

else:
    print('A:', A, 'B:', B)

A.reverse()
B.reverse()

##############################################################################################################
# Extend Test
##############################################################################################################
header('Extend Test')

print('A:', A, 'B:', B, 'C:', C, 'D:', D)
print()

listi = ['a', 'b', 'c']
tupla = (1, 2, 3)
settið = set([1, 2, 3])

A.extend(listi)
if str(A) != '[1, 2, 3, 4, a, b, c]':
    raise IndexError('Virkar ekki með lista')

B.extend(tupla)
if str(B) != '[a, b, c, d, e, 1, 2, 3]':
    raise IndexError('Virkar ekki með tuplu')

C.extend(settið)
if str(C) != '[U, B, I, I, F, 1, 2, 3]':
    raise IndexError('Virkar ekki með sett')

D.extend(A)
if str(D) != '[1, 2, 3, 4, 4, 1, 4, 1, 1, 1, 2, 3, 4, a, b, c]':
    raise IndexError('Virkar ekki með DAList')

print('Virkar með lista, tuplu, setti og DAList')
print()

print('A:', A, '\nB:', B, '\nC:', C, '\nD:', D)


##############################################################################################################
# Remove Test
##############################################################################################################
header('Remove Test')

print('A:', A, '\nD:', D)
print()
print("Tökum 'a' úr A og Öll '1' úr D")
print()
A.remove('a')
n = D.count(1)

for k in range(n):
    D.remove(1)

if str(A) != '[1, 2, 3, 4, b, c]':
    raise IndexError('YO það er villa í remove hjá þér þegar ég ryni að taka "a" úr A')

elif str(D) != '[2, 3, 4, 4, 4, 2, 3, 4, a, b, c]':
    raise IndexError('YO það er villa í remove hjá þér þegar ég ryni að taka "1" úr D')

else:
    print('A:', A, 'D:', D)


##############################################################################################################
# Reset
##############################################################################################################
header('Reset')

A.clear()
B.clear()
C.clear()
D.clear()

for k in range(1, 5):
    A.append(k)
for k in 'abcd':
    B.append(k)
B.append(A)

print('A:', A, 'B:', B)


##############################################################################################################
# Copy Test
##############################################################################################################
header('Copy Test')

D = B.copy()

print('A:', A, '\nB:', B, '\nD:', D)
print()

print('Breytum B[0] í "A"\n')
B[0] = 'A'
if str(B) == str(D):
    raise IndexError('Þetta er ekki shallow copy')
else:
    print('A:', A, '\nB:', B, '\nD:', D)

print('\nBreytum A[3] í "9"\n')
A[3] = 9
if str(B[-1]) != str(D[-1]):
    raise IndexError('Þetta er ekki shallow copy')
else:
    print('A:', A, '\nB:', B, '\nD:', D)


##############################################################################################################
# Pop Test
##############################################################################################################
header('Pop Test')

print("D:", D)
print()
print('Pop -1 frá D')
k = D.pop(-1)

if str(k) != '[1, 2, 3, 9]':
    raise IndexError('YO það er eitthvað að Index hjá þér')
else:
    print('k:', k)
    print("D:", D)


##############################################################################################################
# Annað
##############################################################################################################
header('Annað')

N = DAList()
N.append(None)
N.append(1)
N.append(None)
N.append("R")
N.append(None)
N.append(")")

for n in N:
    print(n)

##############################################################################################################
# EXTRA / TORTURE TESTS (Add this to the bottom of your test.py)
##############################################################################################################
header('Extra / Torture Tests')

def expect_index_error(fn, msg):
    try:
        fn()
    except IndexError:
        print('✅', msg)
        return
    raise IndexError('YO átti að kasta IndexError: ' + msg)

##############################################################################################################
# __str__ should include falsy values + None (None is a valid element)
##############################################################################################################
header('__str__ with falsy + None')

E = DAList(4)
E.append(0)
E.append(False)
E.append('')
E.append(None)

print('E =', E)
# Should show ALL 4 items (including None). Python list prints None, so your DAList should too.
if str(E) not in ('[0, False, , None]', '[0, False, "", None]'):
    # Some implementations show empty string without quotes -> okay
    # But the key is: it must include 0, False, empty string position, and None.
    # We'll check the important parts:
    s = str(E)
    if '0' not in s or 'False' not in s or 'None' not in s:
        raise IndexError('YO __str__ er að sleppa gildum gildum (0/False/None)')

##############################################################################################################
# __getitem__ bounds (should raise when index == len or out of range)
##############################################################################################################
header('__getitem__ bounds')

F = DAList(4)
F.append('a')
F.append('b')
print('F =', F, 'len =', len(F), 'cap =', F.capacity)

expect_index_error(lambda: F[2], 'F[2] á að vera IndexError (index == len)')
expect_index_error(lambda: F[999], 'F[999] á að vera IndexError')
expect_index_error(lambda: F[-3], 'F[-3] á að vera IndexError (of neikvætt)')

##############################################################################################################
# __setitem__ bounds (should not allow "holes" beyond len)
##############################################################################################################
header('__setitem__ bounds / holes')

G = DAList(8)
G.append(1)
G.append(2)
G.append(3)
print('G =', G, 'len =', len(G), 'cap =', G.capacity)

expect_index_error(lambda: (G.__setitem__(5, 99)), 'G[5] = 99 á að vera IndexError (holur)')
# index == len is sometimes treated as append in assignments; if yours does, comment this out.
expect_index_error(lambda: (G.__setitem__(len(G)+1, 7)), 'G[len+1] á að vera IndexError')

##############################################################################################################
# __delitem__ stress: delete from middle, front, back + repeated deletes
##############################################################################################################
header('__delitem__ stress')

H = DAList(4)
for x in [1, 2, 3, 4, 5, 6]:
    H.append(x)
print('H before:', H, 'len =', len(H), 'cap =', H.capacity)

del H[2]   # remove 3
if str(H) != '[1, 2, 4, 5, 6]':
    raise IndexError('YO del í miðju virkar ekki (átti [1, 2, 4, 5, 6])')

del H[0]   # remove 1
if str(H) != '[2, 4, 5, 6]':
    raise IndexError('YO del fremst virkar ekki (átti [2, 4, 5, 6])')

del H[-1]  # remove 6
if str(H) != '[2, 4, 5]':
    raise IndexError('YO del aftast virkar ekki (átti [2, 4, 5])')

print('H after deletes:', H)


##############################################################################################################
# pop bounds + pop correctness
##############################################################################################################
header('Pop bounds + correctness')

I = DAList(4)
for x in [10, 20, 30]:
    I.append(x)
print('I before:', I)

k = I.pop(-1)
if k != 30 or str(I) != '[10, 20]':
    raise IndexError('YO pop(-1) er að gera vitleysu')

expect_index_error(lambda: I.pop(2), 'pop(index==len) á að vera IndexError')
expect_index_error(lambda: I.pop(999), 'pop(999) á að vera IndexError')
expect_index_error(lambda: I.pop(-99), 'pop(-99) á að vera IndexError')

print('I after pops:', I)

##############################################################################################################
# insert negative index behavior (non-empty)
##############################################################################################################
header('Insert negative index semantics')

J = DAList(4)
for x in [1, 2, 3, 4]:
    J.append(x)

print('J before:', J)
J.insert(-1, 99)
print('J after insert(-1, 99):', J)

# Python list: [1,2,3,99,4] for insert(-1, 99)
# If your spec differs, adjust expected accordingly.
if str(J) not in ('[1, 2, 3, 99, 4]', '[1, 2, 99, 3, 4]'):
    # Allowing slight spec differences, but it must not crash and must have 99 inserted somewhere sensible.
    if '99' not in str(J):
        raise IndexError('YO insert(-1, 99) virðist ekki setja inn 99')

##############################################################################################################
# Nested iteration (breaks if DAList returns itself as iterator)
##############################################################################################################
# header('Nested iteration test')

# K = DAList(4)
# for ch in 'abc':
#     K.append(ch)

# pairs = 0
# for x in K:
#     for y in K:
#         pairs += 1

# print('K =', K, 'pairs =', pairs)
# if pairs != 9:
#     raise IndexError('YO nested iteration er bilað (átti 9 pör)')

##############################################################################################################
# count(None) should only count None elements actually in the list, not unused capacity
##############################################################################################################
header('count(None) sanity')

L = DAList(10)
L.append(None)
L.append(1)
L.append(None)
print('L =', L, 'len =', len(L), 'cap =', L.capacity)

c = L.count(None)
print('count(None) =', c)
if c != 2:
    raise IndexError('YO count(None) er að telja ónotuð hólf í capacity (átti 2)')

##############################################################################################################
# index() should raise ValueError when not found
##############################################################################################################
header('index() not found should ValueError')

M = DAList(4)
for x in [1, 2, 3]:
    M.append(x)

print('M =', M)
try:
    M.index(999)
    raise IndexError('YO index(999) á að kasta ValueError þegar ekki finnst')
except ValueError:
    print('✅ index(999) kastar ValueError eins og á að gera')

##############################################################################################################
# Capacity should NOT increase on delete (common design expectation)
##############################################################################################################
header('Capacity should not increase on delete')

N = DAList(1)
N.append(123)  # full
cap_before = N.capacity
del N[0]
cap_after = N.capacity
print('cap before =', cap_before, 'cap after =', cap_after, 'N =', N)

if cap_after != cap_before:
    raise IndexError('YO capacity er að breytast á delete (átti að vera óbreytt)')

print('\n✅ All extra tests passed (ef þú sérð þetta þá ertu líklega í góðum málum)\n')


























