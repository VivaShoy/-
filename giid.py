#
# string = input("введите числа через пробел и знак")
# print(eval(string))

string = input().split(" ")
number1 = float(string[0])
znak = string[1]
if znak == "m":
    result = (number1 * 0.000621).__format__("5f")
    print("mile", result)
elif znak == "d":
    result = (number1 * 39.3701).__format__("5f")
    print("dyim", result)
elif znak == "y":
    result = (number1 * 1.09361).__format__(".5f")
    print("yards", result)
else:
    print("некоректные данные")



# string = input("введите три числа").split(" ")
# number = []
# for i in string:
#     number.append(float(i))
# print(max(number))
# print(min(number))
# print(sum(number) / len(number))