class MyClass:
    def __init__(self):
        self.__hidden = "Hello"
        print(self.__hidden) # Works


if __name__ == "__main__":
    m1 = MyClass()
    print(m1.__hidden) # Doesn't Work
