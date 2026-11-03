#1
# nums = list(map(int, input().split()))
# nums.sort()
# print(nums[-1]) 

#2
# nums = list(map(int, input().split()))
# result = []

# for i in nums:
#     if i not in result:

#         result.append(i)

# print(result)  

# 3
# text = input()

# reverse = " "

# for i in range(len(text)):
#     reverse += text[i]

# if text == reverse:
#     print("YES")
# else:
#     print("NO")  

# 4
# words = input().split()

# longest = words[0]

# for word in words:
#       if len(word) > len(longest):
#         longest = word 
# print(longest) 

# 5
# text = input().lower()
# vowels = "аэиоуөү"
# count = 0

# for ch in text: 
#     if ch not in vowels:
#         count += 1
# print(count)

# 6
# n = int(input())
# total = 0

# for i in range(1, n + 1):
#     if i % 2 != 0: 
#         total += i
# print(total) 

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack хоосон")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("stack хоосон")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0