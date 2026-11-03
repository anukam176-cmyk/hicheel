

# numbers = [5, 3, 2, 18]
# for i in range (len(numbers)-1) :
#     for j in range (len(numbers) -1 -i) :
#         if numbers[j] > numbers [j + 1] :
#              temp = numbers [j]
#              numbers[j] = numbers[j + 1]
#              numbers[j + 1] = temp
# print(numbers) 

# 1
# numbers = [5, 3, 8, 1, 2]
# for i in range (len(numbers) -1) :
#     for j in range (len(numbers)-1 -i) :
#         if numbers [j] > numbers [j +1] :
#             temp = numbers [j]
#             numbers[j] = numbers [j +1 ]
#             numbers [j +1 ] = temp 
# print(numbers)

# 2
# numbers = [4, 9, 2, 7, 1]
# for i in range (len(numbers) -1) :
#     for j in range (len(numbers)-1 -i) :
#         if numbers [j] < numbers [j +1] :
#             temp = numbers [j]
#             numbers[j] = numbers [j +1 ]
#             numbers [j +1 ] = temp 
# print(numbers) 

# 3
# numbers = [3, -2, 7, -5, 0, 1]
# for i in range (len(numbers) -1) :
#     for j in range (len(numbers)-1 -i) :
#         if numbers [j] > numbers [j +1] :
#             temp = numbers [j]
#             numbers[j] = numbers [j +1 ]
#             numbers [j +1 ] = temp 
# print(numbers) 

# 4
# numbers = [4, 2, 4, 1, 2, 3]
# for i in range (len(numbers) -1) :
#     for j in range (len(numbers)-1 -i) :
#         if numbers [j] > numbers [j +1] :
#             temp = numbers [j]
#             numbers[j] = numbers [j +1 ]
#             numbers [j +1 ] = temp 
# print(numbers) 

# 5
# numbers = list (map(int, input().split()))
# for i in range (len(numbers) -1) :
#     for j in range (len(numbers)-1 -i) :
#         if numbers [j] > numbers [j +1] :
#             temp = numbers [j]
#             numbers[j] = numbers [j +1 ]
#             numbers [j +1 ] = temp 
# print(numbers) 

# 6
# names = ["Saraa", "Bat", "Anu", "Bold"]
# for i in range (len(names) -1) :
#     for j in range (len(names)-1 -i) :
#         if names [j] > names [j +1]:
#             temp = names [j]
#             names [j] = names [j + 1]
#             names [j + 1] = temp
# print(names)

# 7
# scores = [75, 92, 60, 88, 70]
# for i in range (len(scores) -1) :
#     for j in range (len(scores)-1 -i) :
#         if scores [j] > scores [j +1] :
#             temp = scores [j]
#             scores[j] =  scores [j +1 ]
#             scores [j +1 ] = temp 
# print(scores)

# 8
# numbers = [6, 2, 9, 1, 5]
# for i in range (len(numbers) -1) :
#     for j in range (len(numbers)-1 -i) :
#         if numbers [j] > numbers [j +1] :
#             temp = numbers [j]
#             numbers[j] = numbers [j +1 ]
#             numbers [j +1 ] = temp 
#     print(numbers) 
#     break 

#9
# numbers = [5, 4, 3, 2, 1]
# count = 0
# for i in range(len(numbers)-1):
#     count += 1
#     for j in range(len(numbers)-1-i):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(count, "=",numbers)

####################################################################################################################


10# numbers = list(map(int, input().split()))
# count = 0
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1-i):
#         count += 1
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(count,"=",numbers)





11# numbers = list(map(int, input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1-i):
#         if numbers[j] < numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp

# print(numbers[j + 1])




12# numbers = list(map(int, input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1-i):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)




13# numbers = list(map(int, input().split()))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1-i):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#             print(numbers)





14# numbers = list(map(int, input().split()))
# for i in range(len(numbers)-1):
#     swapped = False
#     for j in range(len(numbers)-1-i):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#             if swapped == True:
#                 break
# print(numbers)





15# numbers = [1, 2, 3, 5, 4]
# count = 0
# for i in range(len(numbers)-1):
#     count += 1
#     swapped = False
#     for j in range(len(numbers)-1-i):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#             swapped = True
#     if swapped == False:
#         break
# print(count, numbers)







16# numbers = [
#     ["Bat", 75],
#     ["Saraa", 92],
#     ["Anu", 60],
#     ["Bold", 88]
# ]
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1-i):
#         if numbers[j][1] > numbers[j + 1][1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)






17# numbers = [
#     ["Bat", 19],
#     ["Anu", 17],
#     ["Bold", 21],
#     ["Saraa", 18]
# ]
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1-i):
#         if numbers[j][1] > numbers[j + 1][1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers[0], numbers[-1])



17# numbers = [
#     ["Bat", 19],
#     ["Anu", 17],
#     ["Bold", 21],
#     ["Saraa", 18]
# ]
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1-i):
#         if numbers[j][1] > numbers[j + 1][1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers[0], numbers[-1])


18# numbers = list(map(int, input("Өгөх тоонууд : ").split()))
# find = int(input("Хайх тоо : "))
# count = 0
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1-i):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# for i in numbers :
#     if find == i :
#         count += 1
# print(find,"тоо", count, "удаа байна.")




19# a = []
# n = int(input("heden hun avah too : "))
# for i in range(n):
#     numbers = input()
#     dun = int(input())
#     a.append([numbers, dun])
# for i in range(len(a)-1):
#     for j in range(len(a)-1-i):
#         if a[j][1] < a[j + 1][1]:
#             temp = a[j]
#             a[j] = a[j + 1]
#             a[j + 1] = temp
# print(a[0:3])




20# numbers = [7, 3, 5, 1, 6, 2, 4]
# count2 = 0
# count1 = 0
# count = 0
# for i in range(len(numbers)-1):
#     count += 1
#     for j in range(len(numbers)-1-i):
#         count2 += 1
#         if numbers[j] > numbers[j + 1]:
#             count1 += 1
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)
# print("Нийт солилцооны тоо : ",count)
# print("Гадна давталтын нийт тойрог : ",count1)
# print("Нийт харьцуулалтын тоо : ",count2)


21# numbers = list(map(int, input().split()))

# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1-i):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)




22# numbers = list(input().split())
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1-i):
#         if len(numbers[j]) > len(numbers[j + 1]):
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)






23# numbers = [14, 6, 11, 3, 9, 2]

# count = 0
# for i in range(len(numbers)):
#     count +=1 
#     for j in range(len(numbers) - 1, 0, -1):
#         if numbers[j] < numbers[j - 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j - 1]
#             numbers[j - 1] = temp
#     if count == 1:
#         print(numbers)
#         break




24# numbers = [7, 4, 9, 2, 5, 8, 1, 6]
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1-i):
#         if numbers[j] % 2 != 0 and numbers[j + 1] % 2 == 0 :
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)





25# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# numbers = a + b
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1-i):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers) 

# SELECTION SORT 
# numbers = [5, 4, 3, 2, 1] 
# for i in range(len(numbers)-1) :
#     min_index = i

#     for j in range(i + 1, len(numbers)) :
#         if numbers[j] < numbers[min_index] :
#             min_index = j

#     temp = numbers[i]
#     numbers[i] = numbers[min_index]
#     numbers[min_index] = temp

# print(numbers) 

# 1
# arr = [5, 2, 8, 1, 4]
# for i in range(len(arr)-1) :
#     min_index = i
    
#     for j in range(i + 1, len(arr)) :
#         if arr [j] < arr [min_index] :
#             min_index = j

#     temp = arr[i]
#     arr [i] = arr[min_index]
#     arr[min_index] = temp 

# print(arr)

# 2
# arr = [8, 3, 6, 1, 7, 2]
# for i in range(len(arr)-3) :
#     min_index = i
    
#     for j in range(i + 1, len(arr)) :
#         if arr [j] < arr [min_index] :
#             min_index = j

#     temp = arr[i]
#     arr [i] = arr[min_index]
#     arr[min_index] = temp 

# print(arr) 

# 3
# arr = [4, 9, 1, 7, 3]
# for i in range(len(arr)-1) :
#     min_index = i
    
#     for j in range(i + 1, len(arr)) :
#         if arr [j] > arr [min_index] :
#             min_index = j

#     temp = arr[i]
#     arr [i] = arr[min_index]
#     arr[min_index] = temp 

# print(arr)

# 4
# arr = [3, -2, 7, -5, 1]
# for i in range (len(arr) -1) :
#     for j in range (len(arr)-1 -i) :
#         if arr[j] > arr [j +1] :
#             temp = arr [j]
#             arr[j] = arr [j +1 ]
#             arr [j +1 ] = temp 
# print(arr) 

# 5
# numbers = [4, 2, 4, 1, 2, 3]
# for i in range (len(numbers) -1) :
#     for j in range (len(numbers)-1 -i) :
#         if numbers [j] > numbers [j +1] :
#             temp = numbers [j]
#             numbers[j] = numbers [j +1 ]
#             numbers [j +1 ] = temp 
#             a = set(numbers)
# print(list(a)) 

# 6
# arr = [8, 5, 3, 9, 2]
# swapped = False
# for i in range(len(arr)-1) :
#     min_index = i
    
#     for j in range(i + 1, len(arr)) :
#         if arr [j] < arr [min_index] :
#             min_index = j

#     temp = arr[i]
#     arr [i] = arr[min_index]
#     arr[min_index] = temp 
#     swapped = True
#     break
# print(arr) 

# 7
# arr = [7, 4, 9, 2, 5]
# swapped = False
# for i in range(len(arr)-1) :
#     min_index = i
    
#     for j in range(i + 1, len(arr)) :
#         if arr [j] < arr [min_index] :
#             min_index = j

#     temp = arr[i]
#     arr [i] = arr[min_index]
#     arr[min_index] = temp 
#     swapped = True
#     break
# print(arr) 

# 8
# arr = [6, 3, 2, 1, 5]
# count = 0
# for i in range(len(arr)-1) :
#     min_index = i
#     count += 1
    
#     for j in range(i + 1, len(arr)) :
#         if arr [j] < arr [min_index] :
#             min_index = j

#     temp = arr[i] 
#     arr [i] = arr[min_index]
#     arr[min_index] = temp 
#     if count == 2 :
#         print(arr) 
#         break 

# 9
# arr = [4, 1, 3, 2]
# count = 0
# for i in range(len(arr)) :
#     min_index = i
#     for j in range(i + 1, len(arr)) :
#         if arr [j] < arr [min_index] :
#             min_index = j
#     if min_index != i :
#         temp = arr[i] 
#         arr [i] = arr[min_index]
#         arr[min_index] = temp 
#         count += 1
# print(count) 

# 10
# def is_sorted(arr):
#     for i in range(len(arr)-1):
#         if arr [i] > arr[i + 1]:
#             return False 
#     return True 

# a = [2, 4, 1, 5, 3]
# b = [1, 2, 3, 4, 5]
# c = [3, 1, 2, 5, 4]

# # print("a:", is_sorted(a))
# print("b:", is_sorted(b))
# # print("c:", is_sorted(c)) 
# if a == sorted(a):
#     print("a")
# if b == sorted(b):
#     print("b")
# if c == sorted(c):
#     print("c")


# # 11
# def selection_sort(arr) :
#     n = len(arr)
#     for i in range(n-1) :
#         min_index = i
    
#         for j in range(i + 1, n) :
#             if arr [j] < arr [min_index] :
#                 min_index = j

#         temp = arr[i] 
#         arr [i] = arr[min_index]
#         arr[min_index] = temp
#     return arr
# print(selection_sort([1, 5, 7, 2, 4])) 

# 12
# def selection_sort_decs(arr) :
#     n = len(arr)
#     for i in range(n-1) :
#         min_index = i
    
#         for j in range(i + 1, n) :
#             if arr [j] > arr [min_index] :
#                 min_index = j

#         temp = arr[i] 
#         arr [i] = arr[min_index]
#         arr[min_index] = temp
#     return arr
# print(selection_sort_decs([1, 5, 7, 2, 4])) 

# 13
# # arr = [8, 6, 3, 9, 4]
# def selection_sort(a):
#     b = len(a)
#     for i in range (b-1) :
#         min_index = i
#         for j in range(i + 1, b) :
#             if a [j] < a [min_index] :
#                 min_index = j
#         return min_index 
# n = list(map(int,input(":").split()))
# print(selection_sort(n))

# 14
# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min_index = i 

#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index] :
#                 min_index = j

#         temp = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = temp

#     print(arr)

# arr = [5, 3, 4, 1, 2]
# selection_sort(arr) 

# 15
# def bubble_sort():
#   for i in range(len(numbers) -1):
#     for j in range(len(numbers)-1-i):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers [j]
#             numbers[j] = numbers[j + 1]
#             numbers[j+ 1] = temp
#   return numbers
# numbers = list(map(int, input().split()))
# def selection_sort():   
#     for i in range(len(numbers1)-1):
#         min_index = i
#         for j in range(i + 1, len(numbers1)) :
#             if numbers1[j] < numbers1[min_index]:
#                 min_index = j
#         temp = numbers1[i]
#         numbers1[i] = numbers1[min_index]
#         numbers1[min_index] = temp
#     return numbers1
# numbers1 = list(map(int, input().split()))
# if numbers == numbers1 :
#     print("ijil")
# else:
#     print("uur")

# MERGE_SORT 
# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2

#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# numbers = [38, 27, 43, 3, 9, 82, 10]


# print(merge_sort(numbers)) 

# 2
# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2

#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] >= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# numbers = [38, 27, 43, 3, 9, 82, 10]


# print(merge_sort(numbers)) 

# 3
# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2

#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# numbers = [38, 27, 43, 3, 9, 82, 10, 10, 9]


# print(merge_sort(numbers))  

# 4
# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2

#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# numbers = [3, -2, 0, -7, 5, -1]


# print(merge_sort(numbers)) 

# 7
# def merge_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers

# .0    mid = len(numbers) // 2

#     left = numbers[:mid]
#     right = numbers[mid:]






#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []
#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result


# numbers = [38, 27, 43, 3, 9, 82, 10]


# print(merge_sort(numbers)) 


# 1-b
# 2-a 
# 3-c
# 4-d 
# 5-a 
# 6-b 
# 7-d 
# 8-c 
# 9-b 
# 10-d 
# 11-a 
# 12-c
# 13-b
# 14-d
# 15-a
# 16-c
# 17-d
# 18-
# 19-a
# 20-b
# 21-d
# 22-a
# 23-d
# 24-d
# 25-d
# 26-a
# 27-c
# 28-d
# 29-b
# 30-c

# 1-
# 2-b 
# 3-d
# 4-c
# 5-a
# 6-
# 7-a
# 8-c
# 9-b
# 10-a
# 11-
from collections import deque



printer = deque()
printer.append("homework.pdf")
printer.append("photo.png")
printer.append("report.docx")

while len(printer) > 0:
    doc = printer.popleft()
    print("Хэвлэж байна:", doc)










    
    


