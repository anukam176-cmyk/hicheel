# O(1)
# O(n)
# O(1) 
# O(n2)
# O(n)
# O(n2)
# O(n2)
# O(n2)
# O(n)
# O(2n)
# O(log n)
# O(log n)
#    anuka g nydalj ovoliin ideshee bolgnoo HAHAHAHAHAHAHAHA 
#    bi owliin idesh ni dee chmg moljij idn shuu gahai mni 
# import time

# # O(1)
# print("----- O(1) -----")

# for n in [1000]:

#     start = time.perf_counter()

#     x = n

#     end = time.perf_counter()

#     print(f"n = {n:<10} | time = {(end - start) * 1000:.2f} ms")


# # O(n)
# print("\n----- O(n) -----")

# for n in [1000]:

#     start = time.perf_counter()

#     total = 0

#     for i in range(n):
#         total += i

#     end = time.perf_counter()

#     print(f"n = {n:<10} | time = {(end - start) * 1000:.2f} ms")


# # O(n²)
# print("\n----- O(n²) -----")

# for n in [1000]:

#     start = time.perf_counter()

#     count = 0

#     for i in range(n):
#         for j in range(n):
#             count += 1

#     end = time.perf_counter()

#     print(f"n = {n:<10} | time = {(end - start) * 1000:.2f} ms")


# # O(log n)
# print("\n----- O(log n) -----")

# for n in [1000]:

#     start = time.perf_counter()

#     x = n

#     while x > 1:
#         x //= 2

#     end = time.perf_counter()

#     print(f"n = {n:<10} | time = {(end - start) * 1000:.2f} ms")


# 1.1
# age = int(input()) 
# if age > 0 : 
#     if age >= 18 :
#         print("orooroi ")    
# else :
#      print("orj bolohguie") 

# 1.2
# n = int(input("too ogooroi"))
# if n > 0 :
#     if n % 2 == 0 :
#         print("tegsh too")
#     else :
#         print("sondgoi too") 

# # 1.3
# a = int(input())
# b = int(input())
# if a == b :
#     print("tentsuu")
# elif a > b :
#     print(a, "ih")
# else :
#     print(b, "baga")  

# 1.4
# n = int(input())
# if n > 7 :
#     print("buruu udur")
# elif n == 1:
#     print("monday")
# elif n == 2:
#     print("tuesday")
# elif n == 3:
#     print("wednesday") 
# elif n == 4:
#     print("thursday")
# elif n == 5:
#     print("friday")
# elif n == 6:
#     print("saturday, amraltin udur")
# elif n == 7:
#     print("sunday, amraltin udur") 


# 1.5
# km = int(input())
# km_une = int(input())
# hour = int(input())
# if km >=1 and 0 < hour < 21 :
#     print(km * km_une)
# elif 22 <= hour <= 24 or 1 <= hour >= 6 :
#     print(km*km_une*1.2) 

# 1.6
# kut=int(input("kwt oruul: "))
# if kwt<=150:
#     tolbor=100 * kwt 
# elif kwt<=300:
#     tolbor=(150*100)+(kwt-150) "150) 
# else:
#     tolbor=150"100+150"150+(kwt-300) "200)
# print(tolbor) 

# 1.7




# shine hiceel
# linear_search 
# def linear_search(items, target):
#     for i in range(len(items)):     
#         if items[i] == target:      
#             return i                
#     return -1                       
# items = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(linear_search(items, target)) 

# students = [
#     {"name": "Бат", "score": 88},
#     {"name": "Сараа", "score": 95},
#     {"name": "Тэмүүлэн", "score": 72},
# ]
# def find_student(students, name):
#     for s in students:
#         if s["name"] == name:       # ← зөвхөн нэрээр нь харьцуулна
#             return s                # индекс биш, объектыг өөрийг нь буцаалаа
#     return None                     # олдоогүй: объект буцаадаг үед None нь тохиромжтой
# find_student(students, "Сараа")   

# 1
# numbers = [10, 25, 7, 40, 15]
# def linear_search(items, target):
#     for i in range(len(items)):     
#         if items[i] == target:      
#             return i                
#     return -1                       
# items = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(linear_search(items, target)) 

# turshilt uidd bnnnn 
# n = 10 
# if n > 5:
#     print(1)
#     if n < 11 :
#         print(2)
#         if n != 10 :
#             print(3)
#         else :
#             if n // 2 == 0 :
#                 print(4)
#             else :
#                 print(5) 

# 2
# def linear_search(items, target):
#     for i in range(len(items)):     
#         if items[i] == target:      
#             return i                
#     return -1                       
# items = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(linear_search(items, target)) 

# 3
# def linear_search(items, target):
#     for i in range(len(items)):     
#         if items[i] == target:      
#             return i                
#     return -1                       
# items = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(linear_search(items, target)) 

# 4
# def linear_search(items, target):
#     count = 0
#     for i in items :
#         if i == target :
#             count += 1
#             return count
#     return -1
# items = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(linear_search(items, target)) 


# def fun(x):
#     return x + x

# print(fun("5"))  


# def fun(x):
#     print(x == 10)

# fun(10)+5


# 5
# items = [10, 20, 30, 20, 40, 20]
# def linear_search(items, target):
# items = list(map(int, input("Toonuud: ").split()))
# target = int(input("target: "))
# print(linear_search(items, target)) 



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



