
# 1.colors` нэртэй tuple-д дараах 3 өнгийг хадгалаад бүтнээр нь хэвлэ.
# colors=('ulaan','nogoon','tsenher')
# print(colors)



# 2.Дараах амьтдаар tuple үүсгэ.
# animals=("nohoi","muur","tuulai","mori")
# print(f"{animals[0]}\n{animals[2]}\n{animals[-1]}")


# 3. 100 гэсэн ганц утгатай tuple үүсгээд төрлийг нь хэвлэ.
# a=(100,)
# print(type(a))


# 4.утгуудыг индекс ашиглан хэвлэ:
# subjects=("math","mongol hel","angli hel","python")
# print(f"{subjects[0]}\n{subjects[2]}\n{subjects[-1]}")


# 5. Эхний гурван тоо
# numbers=tuple(map(int,input().split()))
# print(numbers[0:3])


# 6.Сүүлийн гурван тоо
# numbers=tuple(map(int,input().split()))
# print(numbers[-1:-4:-1])


# 7.len()` ашиглан хэдэн жимс байгааг хэвлэ.
# jims=tuple(input().split(","))
# print(len(jims))


# 8.Хамгийн их ба хамгийн бага
# too=tuple(map(int,input().split()))
# print(f"hamgiin ih: {max(too)}\nhamgiin baga: {min(too)}")


# 9.Нийлбэр ба дундаж
# onoo=tuple(map(int,input().split()))
# print(sum(onoo))
# print(sum(onoo)/len(onoo))


# 10.Эрэмбэлэх
# too=tuple(map(int,input().split()))
# print(sorted(too))


# 11. 10-iin Тоо хэдэн удаа байна вэ?
# too=tuple(map(int,input().split()))
# print(too.count(10))


# 12.index()` ашиглан `"жүрж"`-ийн индексийг ол.
# jims=tuple(input().split(","))
# ol=input()
# print(jims.index(ol))


# 13.Хэрэглэгчээс амьтны нэр ав. 
# animals=tuple(input().split(","))
# aw=input()
# if aw in animals:
#         print("bnaaa")
# else:
#     print("bhgueenaaa")


# 14. Сурагчийн мэдээлэл
# student=tuple(map(str,input().split()))
# name,age,angi=student
# print(f"Name:{name}\nAge:{age}\nAngi:{angi}")


# 15.Утгуудыг `x`, `y` хувьсагчдад unpacking хийгээд хэвлэ.
# coordinate=tuple(map(int,input().split(",")))
# x,y=coordinate
# print(f"x={x}\ny={y}")


# 16.Утгуудыг `title`, `author`, `pages` хувьсагчдад задлаад хэвлэ.
# a=tuple(map(str,input().split(",")))
# nom, zohiolch, huudas = a  
# print(f"Nom:{nom}\nZohiolch:{zohiolch}\nHuudas:{huudas}")


# 17.Tuple unpacking ашиглан `a`, `b` хоёрын утгыг соль.
# too=tuple(map(int,input().split()))
# a,b=too
# print(f"a={b},b={a}")


# 18.Эхний утга ба үлдсэн утгууд
# numbers=list(map(int,input("TOON UNTGUUDAA UG: ").split()))
# print(f"EHNII UTGA: {numbers[0]}\nULDSEN UTGUUD: {numbers[1:]}")


# 19. Эхний, дундах, сүүлийн утга ол.
# numbers = list(map(int,input("TOONUUD UG: ").split()))
# first,*middle,last = numbers
# print(f"FIRST: {first}\nMIDDLE: {middle}\nLAST: {last}")


# 20. Сурагчийн олон хичээл
# student = ("Тэмүүлэн", "Математик", "Python", "Англи хэл")
# name, *subjects = student
# print(f"SURAGCHIIN NER: {name}\nHICHEELUUD: {subjects}")


# 21.  Барааны нийт үнэ
# product = ("devter", 3500, 4)
# name,price,quantity = product
# print(f"NER: {name}\nUNE: {price}\nSHIRHEG: {quantity}")
# print(f"NIIT UNE: {price*quantity}")


# 22. for` болон unpacking ашиглан сурагч бүрийн нэр, оноог хэвлэ.
# students = []
# n = int(input("Heden suragch baina ve?: "))
# for i in range(n):
#     name = input("Ner: ")
#     score = int(input("Onoo: "))
#     students.append((name, score))
# for name, score in students:
#     print(f"Ner: {name}, Onoo: {score}")


# 23.  Өмнөх `students` tuple-ийг ашигла. Оноо нь `80` буюу 
#      түүнээс их сурагчдын нэрийг хэвлэ.
# students = []
# n = int(input("Heden suragch baina ve?: "))
# for i in range(n):
#     name = input("Ner: ")
#     score = int(input("Onoo: "))
#     students.append((name, score))
# print("80-aas deesh onootoi suragchid:")
# for name, score in students:
#     if score >= 80:
#         print(name)


# 23. PRINT NI ARAI UURUUR.
# students = []
# n = int(input("Heden suragch baina ve?: "))
# for i in range(n):
#     name = input("Ner: ")
#     score = int(input("Onoo: "))
#     students.append((name, score))
# for name, score in students:
#     if score >= 80:
#         print(f"80-AAS DEESH ONOOTOI SURAGCHID: {name}")


# 24. Tuple-ийг түр өөрчлөх
# colors = ("ulaan", "nogoon", "tsenher")
# new_list = list(colors)
# print(new_list)
# new_list.append("shar")
# next_tuple = tuple(new_list)
# print(next_tuple)