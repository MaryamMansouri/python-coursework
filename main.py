#عملگر هاي رياضي
a = 5
b = 3
result = a + b
print("جمع:", result)

x = 10
y = 7
result = x - y
print("تفريق:", result)


num1 = 4
num2 = 6
result = num1 * num2
print("ضرب:", result)

numerator = 8
denominator = 2
result = numerator / denominator
print("تقسيم:", result)

base = 2
exponent = 3
result = base ** exponent
print("توان:", result)

# عملگر مقايسه اي اعداد

x = 9
y = 7

print(x == y)  # False
print(x != y)  # True
print(x < y)   # False
print(x > y)   # True
print(x <= y)  # False
print(x >= y)  # True

# مثال 2
a = 3.14
b = 2.5

print(a == b)  # False
print(a != b)  # True
print(a < b)   # False
print(a > b)   # True
print(a <= b)  # False
print(a >= b)  # True

# عملگر مقايسه اي رشته ها و ليست ها
string1 = "Hello"
string2 = "World"

print(string1 == string2)  # False
print(string1 != string2)  # True

# مثال 2: مقايسه ليست‌ها
list1 = [1, 2, 3]
list2 = [1, 2, 4]

print(list1 == list2)  # False
print(list1 != list2)  # True

# مثال 3: مقايسه بولي‌ها
bool1 = True
bool2 = False

print(bool1 == bool2)  # False
print(bool1 != bool2)  # True


#عملگر (Slice)


text = "Maryam, Mansouri!"

substring = text[7:12]
print(substring)  # خروجي: Mansouri



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# انتخاب بخشي از ليست
sublist = numbers[2:5]
print(sublist)  # خروجي: [3, 4, 5]
