# n1 = int(input("num1 : "))
# n2 = int(input("num2 : "))
# n3 = int(input("num3 : "))
# n4 = int(input("num4 : "))
#
# if n1 > n2:
#     if n1 > n3:
#         if n1 > n4:
#             print(f"{n1} is Greatest !")
#         else:
#             print(f"{n4} is Greatest !")
#     elif n3>n4:
#         print(f"{n3} is Greatest !")
#     else:
#         print(f"{n4} is Greatest !")
# else:
#     if n2>n3:
#         if n2>n4:
#             print(f"{n2} is Greatest !")
#         else:
#             print(f"{n4} is Greatest !")
#     elif n3>n4:
#         print(f"{n3} is Greatest !")
#     else:
#         print(f"{n4} is Greatest !")

# print("\\\"\t\\n\t\\t\t\\\'\t\\\\")

# a = int(input("Enter A : "))
# b = int(input("Enter B : "))
# print("Sum : "+str(a+b))

# a = int(input("Enter A : "))
# b = int(input("Enter B : "))
# a,b = b,a
# print(f"After Swapping : \n A = {a} & B = {b}")

# print('start')
# j=7
# while j:
# 	print('processing')
# 	j=j-3
# print('end')

# choice='yes'
# while choice=='yes':
# 	print('processing')
# 	choice='no'
# print('end')

# for i in range(5):
#     print("Kuldeep Modh")

# n = int(input("Enter Number : "))
# for i in range(n,-1,-1):
#     print(i)

# start = int(input("Enter start Number : "))
# end = int(input("enter End Number : "))
# for i in range(start,end+1 if (start<end) else end-1, 1 if (start<end) else -1):
#     print(i)

# number = int(input("Enter Number : "))
# for i in range(1,11):
#     print(f"{number} X {i} = {number*i}")

# a=b=1
# for i in range (8):
#     if i<2:
#         print(1,end=" ")
#     else:
#         c = a + b
#         print(c, end=" ")
#         a = b
#         b = c
# while True:
#     name = input("Enter a Name : ")
#     response = input("Continue Y or N ? ")
#     if response == 'N':
#         print("Thanks For Using My App !")
#         break
#     else:
#         continue


# sum = 0
# while True:
#     number = int(input("Enter a Number : "))
#     sum += number
#     response = input("Continue Y or N ? ")
#     if response == 'N':
#         print(f"Sum = {sum}")
#         break
#     else:
#         continue


# while True:
#     a = int(input("A : "))
#     b = int(input("B : "))
#     print("1. Addition\n2. Multiplication\n3. Division\n4. Subtraction")
#     choice = int(input("Choice ? "))
#     if choice==1:
#         result = a+b
#     elif choice==2:
#         result = a*b
#     elif choice==3:
#         result = a/b
#     elif choice==4:
#         result = a-b
#     else:
#         print("Incorrect Choice !")
#     print("Result =",result if choice in [1,2,3,4] else "")
#     continuation = (input("Do You Want to Continue ? ")).lower()
#     if continuation == "n":
#         break
#     else:
#         continue

# l1 = ['Java','Python','Php','C']
# print(l1)
#
# l2 = ['Metazone',243,'Sector',7,'Faridabad']
# print(l2)
#
# l3 = list(range(1,101))
# print(l3)
#
#
# numbers=[1,2,3,4,5,6]
# for i in range(len(numbers)-1,-1,-1):
#     print(numbers[i], end=" ")


# mobile_nums = []
# num = int(input())
# for i in range(num):
#     mobile_nums.append(input())
#
# for i in mobile_nums:
#     if len(i) != 10:
#         print("No")
#     elif not (i.startswith(("7","8","9"))):
#         print("No")
#     else:
#         print("YES")


# import re
# import email.utils
#
# n = int(input())
# email_list, emails = [],[]
# for _ in range(n):
#     email_list.append(input())
# for i in email_list:
#     emails.append(i.split(" ")[1])
#
# for i in emails:
#     if re.match(r"[^@]+@[^@]+\.[^@]+", i):
#       print(email.utils.formataddr(email_list[emails.index(i)]))

# list1 = []
# for _ in range(5):
#     name, *line = input().split(",")
#     list1.append(name)
#     print(line)
#
# print(list1)

# print(*[1,2,3,4,5],sep="->")
#
# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# print(scores)
# print(name)
# query_name = input()

from functools import reduce
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     score_list = list(set(arr))
#     winner_score = max(score_list)
#     score_list.remove(winner_score)
#     runnerup_score = max(score_list)
#     print(runnerup_score)

# n = int(input())
# master_list = []
# commands = []
# values = []
# for _ in range(n):
#     cmd, *args = input().split()
#     commands.append(cmd)
#     values.append(args)
# print(commands)
# print(values)
#
# if cmd not in ["insert", "print", "remove", "append", "sort", "pop", "reverse"]:
#     print("Command Not Found !")
# else:
#     for index,cmd in enumerate(commands):
#         if cmd == "insert":
#             master_list.insert(int(values[index][0]),int(values[index][1]))
#         elif cmd == "print":
#             print(master_list)
#         elif cmd == "remove":
#             master_list.remove(int(values[index][0]))
#         elif cmd == "append":
#             master_list.append(int(values[index][0]))
#         elif cmd == "sort":
#             master_list.sort()
#         elif cmd == "pop":
#             master_list.pop()
#         elif cmd == "reverse":
#             master_list.reverse()
#         else:
#             pass

# name = "Kuldeep"
# name= "".join(name.split("e"))
# print(name)


# def count_substring(string, sub_string):
#     substring_found = 0
#     counter = 0
#     for i in string:
#         for j in sub_string:
#             if i == j:
#                 break
#             else:
#                 continue
#         counter += 1
#         if counter == len(sub_string):
#             substring_found += 1
#             string = string.replace(sub_string[0],"",1)
#             print(string)
#     return substring_found
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)

if __name__ == '__main__':
    s = input()
    print(s.isalnum())
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))


