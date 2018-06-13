"""choose 3 ---> set of all subsets of length 3 from arr
s - sum(3_num) is present in arr
if it is return all 4 nums
"""
from collections import Counter
from itertools import combinations
def find_array_quadruplet(arr, s):
  count = Counter(arr)
  three_combinations = combinations(arr,3)
  for combination in three_combinations:
    for x in combination:
      count[x]-=1
    fourth = s - sum(combination)
    if fourth in count and count[fourth]>0:
      return list(combination) + [fourth]
    for x in combination:
      count[x]+=1
  return []

print find_array_quadruplet([2, 7, 4, 0, 9, 5, 1, 3], 20 )