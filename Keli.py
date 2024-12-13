import math


def generate_cayley_table(elements, operation):
    table = []
    for i in range(len(elements)):
        row = []
        for j in range(len(elements)):
            result = operation(elements[i], elements[j])
            row.append(result)
        table.append(row)
    return table


def print_cayley_table(table, elements):
    print("-\t|", end="")
    for element in elements:
        print(f"{element}\t|", end="")
    print()
    print("-" * ((len(elements) + 1) * 8))
    for i, row in enumerate(table):
        print(f"{elements[i]}\t|", end="")
        for result in row:
            print(f"{result}\t|", end="")
        print()
        print("-" * ((len(elements) + 1) * 8))


#def check_operation(operation_char, operation):



elements = []

print(
    "This is Keli table generator, which describes the structure of finite "
    "algebraic systems with a single binary operation. The table allows you to " 
    "determine whether a group is Abelian, find the core of the group and the "
    "inverse elements with respect to other elements in this group. \n"
    )

print("Enter operation that takes place in this group (+ or *):")
operation_char = input()
if operation_char == "+":
    operation = lambda x, y: (x + y)
elif operation_char == "*":
    operation = lambda x, y: (x * y)
else:
    print("Incorrect input!")
    exit()

print("Do you want to build a group modulo some number enter this number? Y/n")
enter = input()
if (enter == "y") or (enter == "Y"):
    print("Enter your number:")
    n = int(input())
    print(
        "Do you want to create group where all the elements are mutually simple" 
        "with the entered number? Y/n"
        )
    enter = input()
    if (enter == "y") or (enter == "Y"):
        if operation_char == "*":
            operation = lambda x, y: (x * y) % n
        else:
            operation = lambda x, y: (x + y) % n
        for i in range(1, n):
            if math.gcd(n, i) == 1:
                elements.append(i)
    else:
        if operation_char == "*":
            operation = lambda x, y: (x * y)
        else:
            operation = lambda x, y: (x + y)
        for i in range(1, n):
            elements.append(i)


table = generate_cayley_table(elements, operation)
print_cayley_table(table, elements)


print("Порядок [1] = 1")
x = 1
for i in range(1, len(elements) - 1):
    while (elements[i]**x % n != 1):
        x += 1
        if (x == 10):
            print("Порядок = inf")
            break
    print(f"Порядок [{elements[i]}] = {x}")
    x = 1



