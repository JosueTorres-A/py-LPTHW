print("Enter a non negative number:")

limit = int(input("> "))

print("Enter the step: ")

step = int(input("> "))

i = 0
numbers = []

for i in range(0, limit, step):
    print("At the top i is %d" % i)
    numbers.append(i)    
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

# while i < limit:
#     print("At the top i is %d" % i)
#     numbers.append(i)
    
#     i += step
#     print("Numbers now: ", numbers)
#     print("At the bottom i is %d" % i)
    

print("The numbers: ")

for num in numbers:
    print(num)