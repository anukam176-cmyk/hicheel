

# 1.
# nums = [3, 8,5, 2,1]
# for i in range(len(nums) -1): 
#     for j in range(len(nums)-1 -i): 
#         if nums[j] > nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(nums)


# 1. 
# numbers=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1 -i):
#         if numbers[j] > numbers[j+1]:
#             a = numbers[j]
#             numbers[j] = numbers[j+1]
#             numbers[j+1] = a
# print(numbers)



# 2.
# nums=list(map(int,input("toonuudaa ug: ").split(",")))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] < nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums)



# 3. 
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums)



# 4. 
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums)


# 5
# nums=list(map(int,input("TOONUUDAA UG: ").split()))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums)



# 6.
# names=list(map(str,input("NERSEE UG: ").split(",")))
# for i in range(len(names)-1):
#     for j in range(len(names)-1 -i):
#         if names[j] > names[j+1]:
#             a=names[j]
#             names[j] = names[j+1]
#             names[j+1] = a
# print(names)


# 7. 
# scores= list(map(int,input("ONOODUUDAA UG: ").split(",")))
# for i in range(len(scores)-1):
#     for j in range(len(scores)-1 -i):
#         if scores[j] > scores[j+1]:
#             a=scores[j]
#             scores[j] = scores[j+1]
#             scores[j+1] = a
# print(scores)



# 8.
# nums= list(map(int,input("TOONUUDAAA UG: ").split(",")))
# for i in range(len(nums)-1):
#         if nums[i] > nums[i+1]:
#             a=nums[i]
#             nums[i] = nums[i+1]
#             nums[i+1] = a
# print(nums)



# 9.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# count=0
# for i in range(len(nums)-1):
#     count += 1
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums,count)



# 10.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# count=0
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         count += 1
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums,count)



# 11.  
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] < nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums,nums[1])




# 12
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums)



# 13. 
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
#     print(nums)



# 14. 
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     count=False
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
#             count = True
#     if count == False:
#         break
#     else:
#         print("sort bollooo")
# print(nums)



# 15.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# total=0
# for i in range(len(nums)-1):
#     count=False
#     total+=1
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
#             count=True
#     if count == False:
#         break 
# print(count)
# print(nums)


# 16.
# n=int(input("HEDIIG ORUULAH VE: "))
# students=[]
# for i in range(n):
#     name=str(input("NEREE ORUUL: "))
#     score=int(input("ONOOG NI ORUUL: "))
#     students.append([name,score])
# for i in range(len(students)-1):
#     for j in range(len(students)-1 -i):
#         if students[j][1] > students[j+1][1]:
#             a=students[j]
#             students[j] = students[j+1]
#             students[j+1] = a
# print(students)



# 17.
# n=int(input("HEDEN HVN ORUULAH VE?: "))
# people=[]
# for i in range(n):
#     name=str(input("NEREE UG: "))
#     age=int(input("NASAA UG: "))
#     people.append([name,age])
# for i in range(len(people)-1):
#     for j in range(len(people)-1 -i):
#         if people[j][1] > people[j+1][1]:
#             a=people[j]
#             people[j] = people[j+1]
#             people[j+1] = a
# print(people)
# print(f"hamgiin zaluu : {people[0]}\nhamgiin hogshin : {people[-1]}")



# 18. 
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# count=0
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# for i in nums:
#     if i == 4:
#         count += 1
# print(nums)
# print(f"{count} bainaa")



# 19.
# n=int(input("HEDEN BARAA ORUULAH VE?: "))
# baraa=[]
# for i in range(n):
#     name=str(input("BARAANII NEREE UG: "))
#     une=int(input("UNEE UG: "))
#     baraa.append([name,une])
# for i in range(len(baraa)-1):
#     for j in range(len(baraa)-1 -i):
#         if baraa[j][1] < baraa[j+1][1]:
#             a=baraa[j]
#             baraa[j] = baraa[j+1]
#             baraa[j+1] = a
# print(baraa)
# print(f"HAMGIIN UNETEI 3 BARAA {baraa[0:3]} BNAAA")



# 20. Дараах бүх даалгаврыг гүйцэтгэ:
#     1. Bubble Sort ашиглан өсөх дарааллаар эрэмбэл.
#     2. Нийт харьцуулалтын тоог тоол.
#     3. Нийт солилцооны тоог тоол.
#     4. Гадна давталтын нийт тойргийг тоол.
#     5. Эцсийн жагсаалтыг хэвлэ.
#     6. `sort()` болон `sorted()` ашиглахгүй.

# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# count=0
# soliltsoo = 0
# haritsuulalt = 0
# for i in range(len(nums)-1):
#     count+=1
#     for j in range(len(nums)-1 -i):
#         soliltsoo += 1
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
#             haritsuulalt += 1

# print(f"GADNA DAVTALT: {count}")
# print(f"SOLILTSOO: {soliltsoo}")
# print(f"HARITSUULALT: {haritsuulalt}")
# print(nums)

