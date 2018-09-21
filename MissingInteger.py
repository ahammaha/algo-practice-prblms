def solution(A):	# O(n)
    arr=set(A)
    res=1
    while res in arr:
        res+=1
    return res

 # https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

 '''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.
'''