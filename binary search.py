# binary(1).py 

# list = [5, 10, 15, 20, 25, 30]
# target = int(input()) 
# left = 0 
# rigth = len (list)-1
# while left <= rigth :
#     mid = (rigth + left) // 2
#     if list [mid]== target :
#               print ("olloo")
#               break
#     elif list [mid] < target : 
#         left = mid + 1
#     else : 
#         rigth = mid - 1 


# class player :
#     def __init__(self, name, skins) :
#         self.name = name
#         self.skins = skins

# player1 = player("tsedo", 1)
# player2 = player("fenrir", 2)

# print(player1.name)
# print(player1.skins)

# print(player2.name)
# print(player2.skins)


# class Student  :
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age 

# player1 = Student("Naraa",17)
# player2 = Student("Temuulen", 19)

# print(player1.name)
# print(player1.age)

# print(player2.name)
# print(player2.age)

# 3
# class Student :
#     def __init__(self, name, age, grade) :
#         self.name = name 
#         self.age = age
#         self.grade = grade 

# player1 = Student("bat", 18, "12A" )

# print(player1.name)
# print(player1.age)
# print(player1.grade) 

# 4
# class Student :
#     def __init__(self, name, score) :
#         self.name = name
#         self.score = score

# player1 = Student("bat", "saraa")
# onoo = Student(85, 85)

# print(player1.name, onoo.name)
# print(player1.score, onoo.name )

# 5
# class Student :
#     def __init__(self, name, score) :
#         self.name = name
#         self.score = score 

#     def add_score(self) :
#         self.score += 5

# player1 = Student("bat",80) 
# player1.add_score()

# print(player1.score)

# 8
# class Student :
#     def __init__(self, name, score) :
#         self.name = name
#         self.score = score 

#     def add_score(self) :
#         self.score += 5

# player1 = Student("bat",80) 
# player1.add_score()
# print(player1.score)

# 9
# class Student :
#     def __init__(self, name, age, birthday) :
#         self.name = name 
#         self.age = age 

#     def add_birthday(self):
#         self.birthday += 1

# player1 = Student("saraa",18)
# player1.add_birthday()

# print(player1.birthday) 


# Quick Sort — Python
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = [8, 3, 1, 7, 0, 10, 2]

# print(quick_sort(numbers))

# 1
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = [8, 3, 1, 7, 4]

# print(quick_sort(numbers))

# 2
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num > pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = [5, 2, 9, 1, 7]

# print(quick_sort(numbers))

# 3
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = [4, 2, 4, 1, 2, 3, 1]

# print(quick_sort(numbers)) 

# 4
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = [3, -5, 0, 8, -2, 1]

# print(quick_sort(numbers))

# 5
# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = [9, 2, 7, 1, 5, 3]

# print(quick_sort(numbers)[:3])

# 6
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num > pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = [4, 9, 1, 7, 3, 8]

# print(quick_sort(numbers)[:2]) 

# 7
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers = [("Bat", 85), ("Bold", 70), ("Saraa", 95), ("Anu", 60)]

# print(quick_sort(numbers))

# 8
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]

#     left = []
#     middle = []
#     right = []

#     for num in arr:
#         if num > pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)

#     return quick_sort(left) + middle + quick_sort(right)


# numbers =["banana", "cat", "apple", "hi", "dog"]

# print(quick_sort(numbers))

# 9
# def quick_sort(arr):
#     if len(arr) <= 1: 
#        return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
# arr = [7, 1, 5, 3, 9]
# sorted_arr = quick_sort(arr)
# if len(sorted_arr) % 2 == 1:
#     median = sorted_arr[len(sorted_arr) // 2]
# else:
#    mid1 = sorted_arr[len(sorted_arr) // 2 - 1]
#    mid2 = sorted_arr[len(sorted_arr) // 2]
#    median = (mid1 + mid2) / 2
# print("Sorted array:", sorted_arr)
# print("Median:", median)

# 10
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            right.append(num)

    return quick_sort(left) + middle + quick_sort(right)


numbers = [8, 3, 5]
b = [2, 9, 1]
print(quick_sort(numbers,b))







