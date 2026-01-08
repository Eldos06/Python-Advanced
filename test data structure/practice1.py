# file.txt => 5 2 3 -> 60 (edit_file.txt)
from math import remainder


# def task_1(n, b, a):
#   return n * b * a * 2
#
# print(task_1(5, 2, 3))
# print(task_1(14, 23, 5))

# def task2(n):
#   return f"""The next number for the number {n} is {n+1}.
# The previous number for the number {n} is {n-1}"""
#
# print(task2(13))

#
# def task3(g, l):
#     all_bank = g + l - 1
#     g_lost = l - 1
#     l_lost = g - 1
#     return g_lost, l_lost
#
# print(task3(4, 7))


# from math import ceil
# def task4(n):
#     result  = n / 10
#     result = ceil(result)
#     return result
#
# print(task4(200))
# print(task4(203))
#
# n = 50
# for i in range(0, n):
#     while pow(2, i) < n:
#         print(pow(2, i), end=' ')
#         i += 1
#     break

# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#
# print(fib(7))

# task 9

# def task(x, y):
#   count = 1
#   for i in range(y+1):
#     x = x * 115 / 100
#     count += 1
#     if x > y:
#       return f"first solution is {count}     with FOR"
#
# print(task(10, 20))
# print(task(1, 1000))
#
# print("===================================================")
#
# def task(x, y):
#     count = 1
#     while x < y:
#         x = x * 1.15
#         count += 1
#     return f"second solution is  {count}     with WHILE"
#
#
# print(task(10, 20))
# print(task(1, 1000))

# def money(n):
#     for count_5 in range(n // 5, -1, -1):
#         remainder = n - count_5 * 5
#         if remainder % 3 == 0:
#             count_3 = remainder // 3
#             return f"{count_5} {count_3}"
#     return "No solution"
#
# print(money(8))
# print(money(11))
# print(money(15))


# def cookie(k, m, n):
#     firstPart = n // k
#     secondPart = n % k
#     result = firstPart * m * 2
#     if secondPart == 0:
#         return result
#     else:
#         return result + (2 * m)
#
# print(cookie(1, 1, 1))
# print(cookie(2, 2, 1))

# def last_task(x1, y1, x2, y2):
#     result = (  (x2 - x1)**2 + (y2 - y1)**2  )**0.5
#     return int(result)
#
# print(last_task(3, 4, 8, 4))






# def createDesk(name: str):
#     name = name.title()

# n = 543210
# n = n - 200
# count = 0
# for i in range(n+1):
#     if n % 2 == 0:
#         count += 1
# print(count)

# def merge(a, b):
#     i = j = 0
#     out = []
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             out.append(a[i]); i += 1
#         else:
#             out.append(b[j]); j += 1
#     out.extend(a[i:]); out.extend(b[j:])
#     return out
#
# def mergesort(arr):
#     if len(arr) <= 1:
#         return arr
#     m = len(arr) // 2
#     return merge(mergesort(arr[:m]), mergesort(arr[m:]))
#
# def unique(n):
#     result = []
#     for i in n:
#         if i not in result:
#             result.append(i)
#     return(result)
#
#
# lenOFn = 5
# n = [4, 3, 3, 1, 2]
# n = mergesort(n)
# n = unique(n)
# print(n[-2])
#
# lenOFn = 8
# n = [1, 2, 5, 3, 5, 6, 6, 5]
# n = mergesort(n)
# n = unique(n)
# print(n[-2])

# task 2
# coords = 6
# cow = 2
# arr = [1, 500_000_000, 1_000_000_000]
# def task2(arr):
#     first_cow = arr[0]
#     second_cow = arr[len(arr) // 2]
#     third_cow = arr[-1]
#
#     if  second_cow - first_cow < third_cow - second_cow:
#         return second_cow - first_cow
#     else:
#         return third_cow - second_cow
# print(task2(arr))


# # function to check if we can place k cows
# # with at least dist distance apart
# def check(stalls, k, dist):
#     # Place first cow at 0th index
#     cnt = 1
#     prev = stalls[0]
#     for i in range(1, len(stalls)):
#
#         # If the current stall is at least dist away
#         # from the previous one place the cow here
#         if stalls[i] - prev >= dist:
#             prev = stalls[i]
#             cnt += 1
#
#     # Return true if we are able to place all 'k' cows
#     return cnt >= k
#
#
# def aggressiveCows(stalls, k):
#     # sorting the array to ensure stalls in sequence
#     stalls.sort()
#     res = 0
#
#     # Minimum and maximum possible minimum distance
#     # between two stalls
#     minDist = 1
#     maxDist = stalls[-1] - stalls[0]
#
#     # Iterating through all possible distances
#     for i in range(minDist, maxDist + 1):
#
#         # If we can place k cows with the
#         # current distance i, update the res
#         if check(stalls, k, i):
#             res = i
#
#     return res
#
#
# if __name__ == "__main__":
#     stalls = [1, 500000000, 1000000000]
#     k = 2
#     ans = aggressiveCows(stalls, k)
#     print(ans)

