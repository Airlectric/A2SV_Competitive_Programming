from functools import lru_cache

@lru_cache(maxsize=None)
def equivalent(a,b):
    if a == b:
        return True
    
    if len(a) % 2 == 1:
        return False
    
    mid = len(a) // 2

    a1, a2 = a[:mid], a[mid:]
    b1, b2 = b[:mid], b[mid:]

    return ((equivalent(a1,b1) and equivalent(a2,b2)) or (equivalent(a1,b2) and equivalent(a2,b1)))




a = str(input())
b = str(input())
print('YES' if equivalent(a,b) else 'NO')

