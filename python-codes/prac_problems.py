'''
# largest of three numbers

def largest_three (a,b,c):
    if a>=b:
        if a>=c:
            return a
        else:
            return c
    else:
        if b>=c:
            return b
        else:
            return c
        
n1 = int(input("Enter 1st no: "))
n2 = int(input("Enter 2nd no: "))
n3 = int(input("Enter 3rd no: "))

largest = largest_three(n1,n2,n3)
print(f"The largest number of {n1}, {n2} and {n3} is {largest}")

'''

# # if enter 1 (add) and if enter 2 (sub)
# def calculate(choice, a, b):
#     if choice ==1:
#         return a+b, '+'
#     elif choice ==2 :
#         return a-b, '-'
#     elif choice ==3:
#         return a*b, '*'
#     elif choice==4:
#         if b !=0:
#             return a/b, '/'
#         else:
#             return "Division by 0: invalid", '/'
    
# choice = int(input("Enter choice (1-4): "))
# a = int(input("Enter no.: "))
# b = int(input("Enter no.: "))

# result, operator = calculate(choice, a ,b)
# print(f"{a} {operator} {b} = {result}")



#stars

def stars_pattern(n):
    for i in range(1,n+1):
        print("*" * i)

#n=int(input("enter no of rows: "))
#stars_pattern(n)

# pyramid stars
def pyramid_pattern(n):
    for i in range(1, n+1):
        for j in range (n-i):
            print(" ", end="")
        for k in range (1, 2*i):
            print("*", end="")
        print()
            
pyramid_pattern(2)

def pyramid_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

pyramid_pattern(2)