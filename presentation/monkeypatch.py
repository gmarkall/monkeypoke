class A:
    pass

def greet(self):
    print("Hello")

# Monkey-patch A:
A.greet = greet

a = A()

# Prints "Hello":
a.greet()
