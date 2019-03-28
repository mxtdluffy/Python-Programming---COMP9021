import sys

def f(n):
    '''
    A pair of natural numbers (m, n) is a Betrothed pair if:
    - the sum of the proper divisors of n is one more than m;
    - the sum of the proper divisors of m is one more than n.
    For instance, (48, 75) is a Betrothed pair since
    - the proper divisors of 48 are 1, 2, 3, 4, 6, 8, 12, 16 and 24
    - the proper divisors of 75 are 1, 3, 5, 15 and 25
    - 1 + 2 + 3 + 4 + 6 + 8 + 12 + 16 + 24 = 76
    - 1 + 3 + 5 + 15 + 25 = 49
    
    >>> f(0)
    The least number >= 0 that is the first member of a Betrothed pair is 48
    The Betrothed itself is (48, 75)
    >>> f(50)
    The least number >= 50 that is the first member of a Betrothed pair is 75
    The Betrothed itself is (75, 48)
    >>> f(100)
    The least number >= 100 that is the first member of a Betrothed pair is 140
    The Betrothed itself is (140, 195)
    '''
    if n < 0:
        sys.exit()
    i = n
    while True:
        m = sum_of_divisors(n) - 1
        if sum_of_divisors(m) - 1 == n:
            print('The least number >=',i,'that is the first member of a Betrothed pair is',n)
            print(('The Betrothed itself is ({}, {})').format(n,m))
            break
        n += 1

def sum_of_divisors(n):
    divisors = [i for i in range(1,n//2+1) if not n%i]
    return sum(divisors)
     


if __name__ == '__main__':
    import doctest
    doctest.testmod()
