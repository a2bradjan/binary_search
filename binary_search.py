#!/bin/python3

def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT: 
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    mid = len(xs)//2
    if len(xs)==0:
        return None
    elif xs[mid]==0:
        return mid+1
    elif 0>xs[mid]:
        leng = len(xs) 
        if leng==1:
            return None
        else:
            x = mid+1
            count = find_smallest_positive(xs[x:])
            if count == None:
                return None
            else:
                return mid+1+count
    else:
        if len(xs)==1:
            return 0
        else:
            if find_smallest_positive(xs[:mid])==None:
                return mid
            else:
                return find_smallest_positive(xs[:mid])

def binary_search_1(xs, x):
    """
    Returns lowest index with a value >= x
    """
    l=len(xs)
    mid = l//2
    if l==0:
        return None
    elif xs[0]==x and l==1:
        return 0
    elif xs[mid]==x:
        if xs[mid-1]!=x:
            return mid
        else:
            return binary_search_1(xs[:mid],x)
    elif x<xs[mid]:
        count = binary_search_1(xs[mid+1:],x)
        if count == None:
            return None
        else:
            return count+mid+1
    #elif len(xs)==1 and xs[0]==x:
    #    return 0
    else:
        return binary_search_1(xs[:mid],x)
        

def binary_search_2(xs, x):
    """
    Returns lowest index with a value < x
    """
    l=len(xs)
    mid = l//2
    if l==0:
        return 0
    elif xs[0]==x and l==1:
        return 1
    elif xs[mid]==x:
        if mid==l-1:
            return mid
        elif xs[mid+1]!=x:
            return mid
        else:
            count=binary_search_2(xs[mid+1:],x)
            if count==None:
                return None
            else:
                return mid+1+count
    elif xs[mid]>x:
        count = binary_search_2(xs[mid+1:],x)
        if count == None:
            return None
        else:
            return mid+1+count
    else:
        return binary_search_2(xs[:mid],x)

def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT: 
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2

    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([1, 2, 3], 4)
    0
    '''
    search1=binary_search_1(xs,x)
    search2=binary_search_2(xs,x)
    if search1==None or search2==None:
        return 0
    else:
        result=search2-search1
        if search1!=search2:
            return result
        else:
            return result+1
    if search1!=search2:
         return search2-search1 
    else:
         return search2-search1+1

def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    m1=(hi-lo)/4+lo
    m2=(hi-((hi-lo)/4))
    hifun=f(hi)
    lofun=f(lo)
    m2fun=f(m2)
    m1fun=f(m1)
    minimum=min(lofun,m1fun,m2fun,hifun)
    if (hi-lo)<epsilon:
        if hifun==min(lofun,hifun):
            return hi
        elif lofun==min(lofun,hifun):
            return lo
    elif m1fun==minimum or lofun==minimum:
        return argmin(f,lo,m2,epsilon=epsilon)
    else:
        #m1 = ((hi-lo)*.25)+lo
        #m2 = ((hi-lo)*.75)+lo
        return argmin(f,m1,hi,epsilon=epsilon)
