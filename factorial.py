def Factorial(n):
    if n == 0:
      return 1



    return n * Factorial(n-1)

def void():
    n = int(input('Escribe un entero: '))
    print(Factorial(n))



if __name__ == '__main__':
    void()