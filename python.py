# 1
# nums = [7, 3, 9, 9, 2, 5, 7, 8]
# nums.sort()
# a = set(nums)
# b = list(a)
# print(b[-2]) 

# 2
# nums = [7, 3, 9, 9, 2, 5, 7, 8]
# nums.sort()
# a = set(nums)
# b = list(a)
# print(b[1])

# # 3
# nums = [2, 1, 3, 5, 4, 7, 9, 11, 6]
# a = 0
# b = 0
# for n in nums :
#     if n % 2 == 1 :
#         b += 1
#         a = max(a,b)  
#     else :
#        b = 0  
# print(a) 

# 4
# a = [1, 2, 4, 2, 3, 5, 7, 1]
# print(len(a))  hud2 
                                                               
# massive
# m =[[1, 2, 3] [4, 5, 6] [7, 8, 9]]
# for i in range (o, len(m)) 
#     for o in m [i]
#         print(o, end="")


# 1 Index ашиглах
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# a = nums[1]
# print(a[2]) 

#2. "Bold" нэрийг хэвлэ
# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ] 
# a = students [2]
# print(a[0])  

# 3. 2 дахь мөрийг хэвлэ
# nums = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
# a = nums [2]
# print(a[3]) 

# 4. 70 тоог хэвлэ
# nums = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ] 
# print()  hhhhhhhhh 

#  5. Хамгийн эхний утгыг хэвлэ
# nums = [
#     [5, 10],
#     [15, 20]
# ] 
# print(nums[0][0])

# 6. Хамгийн сүүлийн утгыг хэвлэ
# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# print(nums[-1][-1]) 

#  7. Бүх мөрийг хэвлэ
# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# for i in nums :
#     print(i)

#  8. Бүх тоог хэвлэ
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ] 
# for i in range (0, len (nums)) :
#     for o in nums [i] :
#         print(o) 

# 9. Бүх тоог нэг мөрөнд хэвлэ
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ] 
# for i in range (0, len (nums)) :
#     for o in nums [i] :
#         print(o, end= "") 

# 10. 10-аас их тоонуудыг хэвлэ
# nums = [
#     [3, 12, 5],
#     [20, 7, 15]
# ]
# for i in range (0, len (nums)) : 
#     for o in nums [i] : 
#         if o > 10 : 
#             print(o, end= " ") 

# 11. Нийт хэдэн тоо байгааг ол
# nums = [
#     [1, 2],
#     [3, 4, 5],
#     [6]
# ] 
# count = 0
# for i in range(0, len (nums)) :
#     for o in nums [i] :
#      count += 1
# print(count )  

# 12. Бүх тооны нийлбэрийг ол
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ] 
# total = 0 
# for i in range(0, len (nums)) :
#     for o in nums [i] :
#      total += o
# print(total )   

# 13. Тэгш тоонуудыг хэвлэ
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(0, len (nums)) :
#     for o in nums [i] :     
#             if o % 2== 0 :
#                 print(o, end= " ") 

# 14. Сондгой тоонуудын тоог ол
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ] 

# 15. Тэгш тоонуудын нийлбэрийг ол
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8]
# ] 
# total = 0
# for i in range(0, len (nums)) :
#     for o in nums [i] :     
#             if o % 2== 0 : 
#                 total += 1
# print(total) 

# 16. Эерэг тоонуудын тоог ол
# nums = [
#     [-3, 5, 0],
#     [7, -2, 8],
#     [-1, 4, 0]
# ] 
# for i in range (0, len (nums)) : 
#     for o in nums [i] : 
#         if o > 0 : 
#             print(o, end= " ") 

# 17. Сөрөг тоонуудын нийлбэрийг ол
# nums = [
#     [-2, 3, -5],
#     [4, -1, 6]
# ] 
# total = 0
# for i in range (0, len (nums)) : 
#     for o in nums [i] : 
#         if o < 0 :
#            total += o
# print(total)  zuw bodsn 

# 18. Хамгийн их тоог ол
# nums = [
#     [4, 8, 2],
#     [10, 3, 7],
#     [1, 6, 5]
# ] 
# a = []
# for i in nums : 
#     print(max(i)) bodh hrgtei 
 
# 20. Мөр бүрийн нийлбэрийг ол 
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ] 
# for i in nums :
#     print(sum(i)) 



# 21. Мөр бүрийн хамгийн их тоог ол
# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]
# for i in nums :
#     print(max(i)) 

# 22. Мөр бүрийн хамгийн бага тоог ол
# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ] 
# for i in nums :
#     print(min(i)) 

# 23. 7 тоо байгаа эсэхийг шалга
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in nums :
#     if 7 in i :
#         print("yes") 
#     else :
#         print("no")  
        
#24. Өгөгдсөн тоо хэдэн удаа байгааг ол
# nums = [
#     [1, 2, 3],
#     [2, 4, 2],
#     [5, 2, 6]
# ]

# target = 2 
# count = 0
# for i in nums :
#     for j in i :
#         if j==2 :
#             count += 1 
# print(count) 

# 25. 5-аас их тоонуудын нийлбэрийг ол
# nums = [
#     [1, 7, 3],
#     [9, 2, 6],
#     [4, 8, 5]
# ] 
# count = 0
# for i in nums :
#     for j in i :
#         if j >5 :
#            count += j
# print(count) 

# 26. Хамгийн их нийлбэртэй мөрийг ол
# nums = [
#     [1, 2, 3],
#     [10, 20, 30],
#     [4, 5, 6]
# ] 
# for i in nums :
#     b = max(nums) 
# print(b) 

# 27. Сурагч бүрийн нэр ба насыг хэвлэ
# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ] 
# for i in range(0, len (students)) :
#     for o in students[i] : 
#         print(o, end= " ") 
#     print() 

# 28. 18-аас дээш настай сурагчдыг хэвлэ
# students = [
#     ["Bat", 17],
#     ["Sara", 19],
#     ["Bold", 20],
#     ["Anu", 16]
# ] 
# for ner, nas in students :
#     if nas >18 :
#         print(ner) 

# 29. Сурагч бүрийн дундаж оноог ол
# students = [
#     ["Bat", 80, 90, 70],
#     ["Sara", 100, 90, 95],
#     ["Bold", 60, 70, 80]
# ] 
# for ner, * onoo in students :
#     b = len(onoo)
#     niit = (sum(onoo)) 
#     a = niit / b 
#     print(ner, a)                             

# 30. Хамгийн өндөр дундажтай сурагчийг ол
# students = int(input( ))
# h = [] 
# for i in range (students) :
#     j = int(input("too"))
#     a = int(input("too"))
#     b = int(input("too"))
#     l = input("ner") 
#     m = [l, j, b, a]
#     h.append(m)
# best_name = h[0][0]
# best_avg = 0
# for noo in h :
#     total =noo[1] + noo [2] + noo [3] 
#     avg = total /3
#     if avg > best_avg :
#         best_avg = avg 
#         bestname = noo[0]
# print(best_avg, best_name)           









# def find_highest_average_student(students):
#     best_name = students[0][0]
#     best_avg = 0
#     for student in students:
#         total = sum(student[1:])  # Sum the scores
#         avg = total / (len(student) - 1)  # Calculate average
#         if avg > best_avg:
#             best_avg = avg
#             best_name = student[0]
#     return best_name, best_avg 

# def main():
#     students = int(input("Enter number of students: "))
#     student_data = []
#     for _ in range(students):
#         name = input("Enter student name: ")
#         scores = [int(input(f"Enter score {_+1}: ")) for _ in range(3)]
#         student_data.append([name] + scores)

#     best_name, best_avg = find_highest_average_student(student_data)
#     print(f"Highest average: {best_avg}, Student: {best_name}") 

# def love(x):
#     print("I love you", x)  
# love("altka")  

# def avg():
#     nums = list(map(int, input().split()))
#     return sum(nums) / len(nums) 
# a = avg()
# print(a) 

# def love(name="hun bish"):
#     print("i love you", name)
# love("altka")  

# def love(*name):
#     print(name) olon utga awah ogoh 

# def love (**name): 2 od awbal olon utga awnaaa
#     print(name)
# love(name= "altka", age=18, name2= "sara",age2=19) 

# 1
# def love (name ):
#     print("hello") 
# love("hello")

# 2
# def greet(name):
#     print("hello", name) 
# greet("bat") 

# 3
# def love(name, age):
#     print("hello", name, age)
# love("bat", 18) 

# 4
# def add(a,b): 
#     return a + b 
# print(add(10, 20)) 

# 5
# def square(num):
#     return num ** 5 
#     print(square(5)) bodno 

# 6
# def max_num(a, b):
#     a = int(a)
#     b = int(b)
#     if a > b:
#         return a
#     else:
#         return b 
# print(max_num(10, 20)) 

# 7
# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd" 
# print(check_even_odd(7)) 

# 8
# def check_age(age):
#     if age >= 18:
#         return "Adult"
#     else:
#         return "Minor" 
# print(check_age(20)) 

# 9 100gaas ih tegees baga garwal buruu hariu garh ystoishdeee lalraaa
# def get_grade(score): 
#         return "zail buruuu"
#     if 90 < score >= 100: 
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "F" 
# score = int(input("too ogooocdeeeee:"))
# if 0 > score > 100 :
#     print("zailllll")
# a = input()
# print(get_grade(score))   



# 10
# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i) 

# print_numbers(5) 

# 11
# def sum_numbers(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total

# print(sum_numbers(5))  

# 12
# def count_even(n):
#     count = 0
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             count += 1
#     return count
# print(count_even(10))  

# 13
# def count_digits(nums):
#     count = 0
#     for num in nums :
#         count += len(str(num)) 
#         return count
# print(count_digits([12345])) 

# 14
# def find_max(nums):
#     max_num = nums[0]
#     for num in nums:
#         if num > max_num:
#             max_num = num
#     return max_num  
# print(find_max([4, 8, 2, 15, 6])) 

# 15
# def find_min(nums):
#     min_num = nums[0]
#     for num in nums:
#         if num < min_num:
#             min_num = num
#     return min_num
# print(find_min([7, 3, 9, 1, 5])) 

# 16
# def count_even(nums):
#     count = 0
#     for num in nums:
#         if num % 2 == 0:
#             count += 1
#         return count 
# print(count_even([1, 2, 4, 7, 8, 10]))  hariu buruu

# 17
# def list_sum(nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# print(list_sum([10, 20, 30, 40])) 

# 18
# def get_age(students, name):  
# b = {
#     "Bat": 18,
#     "Sara": 19,
#     "Bold": 20
# }
# print(get_age(b, "Sara")) udku bodcinoo bi 



# 18
# def get_age(students, name):
#     return student [name]
# students = {
#     "Bat": 18,
#     "Sara": 19,
#     "Bold": 20
# }
# n = int(input())
# for i in range(n) : 
#         name = input()
#         age = int(input( ))
#         students[name] = age
# m = input()
# print(get_age(students, m))      





# 20
# def average_score(students):
#     total_score = 0
#     for student in students:
#         total_score += student[1]
#         return total_score / len(students)
# print(average_score([["Bat", 80], ["Sara", 90], ["Bold", 70]])) 

# 21 
# def unique_count(nums):
#     unique_nums = set(nums)
#     return len(unique_nums)
# print(unique_count([1, 2, 2, 3, 3, 3, 4]))

# 22. Function + set
# unique_numbers(nums) function бич. List-ээс давхардлыг арилгаад set буцаа.
# def unique_numbers(nums):
#     return set(nums)
# print(unique_numbers([1, 2, 2, 3, 3, 3, 4]))

# 23. Default parameter
# def greet(name="Guest"):
#     print(f"Hello, {name}!") 

# greet() 

# 24. Default parameter
# def power(num,exponet=2):
#     return num ** exponet
# print(power(2,3)) 



# 25. Default parameter + if 
# def discount(price, percent=10):
#     if percent < 0 or percent > 100 :
#         return "Invalid discount percentage"
#     discount_amount = price * (percent / 100)
#     return discount_amount 
# print(discount(10000, 20)) 


# 26
# def sum_all(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# print(sum_all(10, 20, 30, 40)) 

# 27
# def find_max(*args):
#     if not args:
#         return None
#     max_num = args[0]
#     for num in args:
#         if num > max_num:
#             max_num = num
#     return max_num
# print(find_max(5, 8, 2, 10, 3))  

# 28
# def count_even(*args):
#     count = 0
#     for num in args:
#         if num % 2 == 0:
#             count += 1
#     return count
# print(count_even(1, 2, 4, 7, 8, 10))

# 29
# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")  
# show_info(name="Bat", age=18, city="Ulaanbaatar")
# print() 

# 30
# def calculate_total(**kwargs):
#     total = 0
#     for key, value in kwargs.items():
#         total += value
#     return total
# print(calculate_total(item1=2000, item2=3000, item3=2500)) 

# 31
# def analyze_numbers(nums):
#     total = sum(nums)
#     average = total / len(nums) if len(nums) > 0 else 0
#     max_num = max(nums) if nums else None
#     min_num = min(nums) if nums else None
#     return {
#         "total": total,
#         "average": average,
#         "max": max_num,
#         "min": min_num
#     }
# print(analyze_numbers(max_num)) 
# bodj cddgueeeeeeeeeeee 

#32. Function + dict + list
# def student_average(students):
#     averages = {}
#     for student in students:
#         name = student[0]
#         scores = student[1:]
#         average = sum(scores) / len(scores) if scores else 0
#         averages[name]= average
#     return averages
# print(student_average([["Bat" , 80, 90, 70]]))  
# buruu bodsn  

# 33
# def best_student(students):
#     best_name = None
#     best_avg = 0
#     for student in students:
#         name = student[0]
#         scores = student[1:]
#         average = sum(scores) / len(scores) if scores else 0
#         if average > best_avg:
#             best_avg = average 
#             best_name = name
#         return best_name, best_avg
# print(best_student([["Bat", 80, 90, 70] , ["Sara" , 100, 90, 95] , ["Bold " , 60, 70, 80]])) 

# 34 
# def calculate(*args, **kwargs):
#     total = sum(args) + sum(kwargs.values())
#     return total 
# print(calculate(10, 20, 30, bonus=100, tax=20)) 


# def greet(name = "Guest"):
#     print("Hello " + name)

# n = input("ner ug : ") or null
# greet(n)

# a = [1, 2, 3, 5, 7]
# a[0] 
# for i in a :
#     for y in a : 
#         print(i, y) 



# binary search 
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

# 1 

# def binary_search(items, target):
#     lo, hi = 0, len(items) - 1          
#     while lo <= hi:                    
#         mid = (lo + hi) // 2            
#         if items[mid] == target:       
#             return mid
#         elif items[mid] < target:      
#             lo = mid + 1
#             hi = mid - 1
#     return -1                
# numbers = [3, 7, 12, 18, 25, 31, 40]
# print(binary_search(numbers, 18)   






















#  prices = {"талх": 2500, "сүү": 3200, "өндөг": 450, "ус": 1000, "алим": 1800}
# shaalguulalt
# prices = {"талх": 2500, "сүү": 3200, "өндөг": 450, "ус": 1000, "алим": 1800}
# def delguur():
#     cart = {}
#     while true :
#         ner = input("baraanii ner:") 
#         if ner == "toloh" : 
#             break 
#         if ner not in prices :
#             print(ner, "mnai delguurt bhq")
#             too = int(input("too shirheg:"))   
#         if too <= 0 :
#             print("too shirheg buruu")

# lst = []
# while true :
#     ner = input("baraanii ner:")
#     if ner in prices :
#         print(f"{prices [ner]} unetei baraa {stosck ner}")
#         lst.append 

#     cart[ner] = cart.get(ner, 0 ) + too
# print("\n === barimt ===")
# niit = 0 
# hamgiin_ih=""
# ih_une= 0 

# for ner, too in cart.items():
#     dun = prices[ner] * too
#     niit += dun

#     print(f"{ner}x{too} = {dun}")

#     if dun > ih_une :
#         ih_dun = dun
#         hamgiin_ih = ner

# hongololt = 0 

# if niit >= 20000:
#     hongololt = niit*0.1

#     tuluh_dun = niit - hongololt

# print("niit")
# print("hongololt") 
# print("toloh dun")

# if hamgiin_ih :
#     print("hamgiin ih mongo tolson baraa:", hamgiin_ih, f"({ih-une})")

# delguur()

# 2

        
