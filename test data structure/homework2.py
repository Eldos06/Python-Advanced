#1
# quick sort TimeComx are three: best case O(log n), averange case O(nlog n), worst case O(n^2)
# def qsort(a):
#     if len(a) < 2:
#         return a
#     p = a[0]
#     left = [x for x in a [1:] if x <= p]
#     right = [x for x in a [:1] if x > p]
#     return qsort(left) + [p] + qsort(right)
#
# print(qsort(['4', '3', '3', '1', '2'])[-2])

#2

#
# def canPlace(stall, dist, k):
#     cntCow = 1
#     last = stall[0]
#
#     for i in range(1, len(stall)):
#         if stall[i] - last >= dist:
#             cntCow += 1
#             last = stall[i]
#         if cntCow >= k:
#             return True
#     return False
#
# def aggressiveCow(stall, k):
#     stall.sort()
#     low = 1
#     high = stall[-1] - stall[0]
#     ans = -1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if canPlace(stall, mid, k):
#             ans = mid
#             low = mid + 1
#         else:
#             high = mid - 1
#     return ans
#
#
# n, k = 6, 3
# stall = [2, 5, 7, 11, 15, 20]
# print(aggressiveCow(stall, k))

# import math
#
# C = float(input().strip())
#
# l, r = 0.0, math.sqrt(C) + 10
# for _ in range(100):
#     mid = (l + r) / 2
#     if mid**2 + math.sqrt(mid) < C:
#         l = mid
#     else:
#         r = mid
#
# print(f"{(l + r) / 2:.9f}")

########3
# taks 3
# import math
# C = 2.0_000_000_000
#
# l, r = 0.0, math.sqrt(C) + 10
# for i in range(100):
#     mid = (l + r) / 2
#     if mid**2 + math.sqrt(mid) < C:
#         l = mid
#     else:
#         r = mid
#
# print(f"{(l + r) / 2:.9f}")
#
#
#
# # #task 4
# def bush(n, b):
#     ans = 0
#     for i in range(1, n):
#         s = b[i - 1] + b[i] + b[(i+1)%n]
#         ans = max(ans, s)
#     return ans
#
# print(bush(4, [1, 2, 3, 4]))
# print(bush(3, [1, 2, 3]))
#
#
# #########################
# # task 5
# def searchStr(words: str, char: str) -> int:
#     return words.find(char)
#
# print(searchStr('hello world', 'o'))
# print(searchStr('mathematics', 't'))
#
# ############################################
# # task 6
# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = mergeSort(arr[:mid])
#     right = mergeSort(arr[mid:])
#     res = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     res.extend(left[i:])
#     res.extend(right[j:])
#     return res
#
# print(
#     mergeSort([3, 4, 5, 1, 2])[0]
# )

##################################
#task 7
def closest(myList: list, target: float):
    f = int(target // 1)
    if f in myList:
        currentIndex = myList.index(f)

        if currentIndex + 1 < len(myList):
            next_val = myList[currentIndex + 1]
            if abs(next_val - target) < abs(f - target):
                return next_val
        return f
    else:
        return min(myList, key = lambda x: abs(x - target))

print(closest( [1, 2, 3, 4, 5],3.7))
print(closest( [1, 2, 3, 4, 5],2.2))
print(closest( [1, 2, 3, 4, 5],4.5))




