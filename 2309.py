import sys



input = sys.stdin.readline
dwarf = []
sum = 0
for i in range(9):
  a = int(input())
  dwarf.append(a)
  sum += a
mission = False

def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  lesser_arr, equal_arr, greater_arr = [], [], []
  for num in arr:
    if num < pivot:
      lesser_arr.append(num)
    elif num > pivot:
      greater_arr.append(num)
    else:
      equal_arr.append(num)
  return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)



dwarf = quick_sort(dwarf)


for i in range(8):
  for j in range(i,9):
    if sum - dwarf[i] - dwarf[j] == 100:
      for k in range(9):
        if k == i or k == j:
          continue
        else:
          sys.stdout.write("{} \n".format(dwarf[k]))
      mission = True
      break
  if mission :
    break


