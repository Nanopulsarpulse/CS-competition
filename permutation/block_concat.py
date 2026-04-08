import sys
from itertools import permutations

def rotate(block):
    x, y, c = block
    yield(x, y, c)
    if x != y:
        yield(y, x, c)

def check(a, b, c, n): # this function receive a, b, c three block that has been permuted, and n is the sidelength of square
    if a[0] == n and b[0] == n and c[0] == n: # this is the first case, which three blocks have a same sidelength that equals n
        if a[1] + b[1] + c[1] == n:
            return 1 # the first type concat
    
    if a[0] == n: #in the second case, the rest of two blocks align vertically
        require = n - a[1]
        if b[0] == require and c[0] == require and b[1] + c[1] == n:
            return 2
    return -1

def solve():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data: return
    
    rect = []
    area = 0 #area stores the area of the square
    for i in range(0, 6, 2):
        x, y = input_data[i], input_data[i+1]
        rect.append((x, y, chr(ord('A') + i//2))) # now rect becomes: [(x1, y1, A), (x2, y2, B), (x3, y3, C)]
        area += x*y

    l = int(area**0.5)
    if l*l != area:
        return "-1"
    
    n = max(input_data)
    
    for perm in permutations(rect):
        a, b, c = perm
        for a in rotate(a):
            for b in rotate(b):
                for c in rotate(c):
                    canva = []
                    if check(a, b, c, n) == 1: # type 1 concat
                        for _ in range(a[1]):
                            canva.append(a[2] * n)
                        for _ in range(b[1]):
                            canva.append(b[2] * n)
                        for _ in range(c[1]):
                            canva.append(c[2] * n)
                        return n, canva
                    elif check(a, b, c, n) == 2: # type 2 concat
                        for _ in range(a[1]):
                            canva.append(a[2] * n)
                        for _ in range(b[0]): # since b[0] == c[0], use any of them have no difference
                            canva.append(b[2] * b[1] + c[2] * c[1])
                        return n, canva
    print("-1")
    return None

if __name__ == "__main__":
    result = solve()
    if result:
        size, pattern = result
        print(size)
        for row in pattern:
            print(row)

