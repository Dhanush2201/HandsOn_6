def partition(A, L, H):
    pivot = A[L]  
    i = L + 1
    j = H

    while True:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] > pivot:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
        else:
            break

    A[L], A[j] = A[j], A[L]
    return j

def non_random_quick(A, L, H):
    if L < H:
        mid = (L + H) // 2
        if A[H] < A[L]:
            A[L], A[H] = A[H], A[L]
        if A[mid] < A[L]:
            A[mid], A[L] = A[L], A[mid]
        if A[H] < A[mid]:
            A[H], A[mid] = A[mid], A[H]

        pivot_index = partition(A, L, H)
        non_random_quick(A, L, pivot_index - 1)
        non_random_quick(A, pivot_index + 1, H)

def random_quick(A, L, H):
    if L < H:
        pivot_index = random.randint(L, H)  
        A[pivot_index], A[H] = A[H], A[pivot_index]

        pivot_index = partition(A, L, H)
        random_quick(A, L, pivot_index - 1)
        random_quick(A, pivot_index + 1, H)

import random

A = random.sample(range(1, 100), 10) 
print("Original array:", A)

non_random_quick(A.copy(), 0, len(A) - 1)
print("Non-random quicksorted array:", A)

random_quick(A.copy(), 0, len(A) - 1)
print("Random quicksorted array:", A)
