from random import randint


def print_hi(name):
    # use a breakpoint in the code
    print(f'Hi, {name}')


# press the green button to run the script
if __name__ == '__main__':
    print_hi('VsCode')

# imperative
n = 10
sum_imperative = 0
for i in range(1, n+1):
    sum_imperative += i
print(f'Sum = {sum_imperative}')

# declarative
N = 10
numbers = range(1, N + 1)
print(f'Sum = {sum(numbers)}')

# imperative
N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)


for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)

# declarative
N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)
print(sorted(a))
