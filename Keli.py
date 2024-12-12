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

elements = []
n = int(input())
for i in range(1, n):
    if math.gcd(n, i) == 1:
        elements.append(i)

operation = lambda x, y: (x * y) % n

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



