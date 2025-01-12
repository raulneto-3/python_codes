def trianguloretangulo(n = 10):
    for i in range(1, n+1):
        print("*" * i)
    for i in range(n-1, 0, -1):
        print("*" * i)

if __name__ == '__main__':
    trianguloretangulo()