username = "ParthDave"

def func():
    # username = "hello"
    print(username) 

func()
print(username)


# //////////////
x = 99
# def func2(y):
#     z = x + y
#     return z

# print(func2(1))




# def func3():
#     global x
#     x = 12

# func3()
# print(x)





def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()




# clouser example
def chintucoder(num):
    def actual(x):
        return x ** num
    return actual

f = chintucoder(2)
g = chintucoder(3)

print(f(3))
print(g(3))