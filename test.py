print("This is github test")
print("Another test")
print("try again")


def fib(num):
    a, b = 0, 1
    for i in range(num):
        print(a)
        a, b = b, a + b


if __name__ == "__main__":
    fib(10)
    print('good work')

