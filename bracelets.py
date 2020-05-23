from sys import stdin
import math
import cmath

PI = math.pi

def fft(A, invert):
    """
    Entrada: Un arreglo A de coeficientes, invert un booleano que me indica si necesito calcular la DFT o la DFT inversa
    Salida: Dependiendo de invert retorno la DFT o la DFT inversa de A
    """
    n = len(A)
    if n == 1:
        return

    Aeven, Aodd = [], []
    #Separo indices pares e impares
    for i in range(int(n/2)):
        Aeven.append(A[2*i])
        Aodd.append(A[2*i+1])

    fft(Aeven, invert)
    fft(Aodd, invert)

    #Diagrama mariposa
    angle = 2 * PI / n * (-1 if invert else 1)
    w = complex(1,0)
    wn = complex(math.cos(angle), math.sin(angle))
    for i in range(int(n/2)):
        A[i] = Aeven[i] + w * Aodd[i]
        A[i + int(n/2)] = Aeven[i] - w * Aodd[i]
        if invert: #Para la interpolacion
            A[i] /= 2
            A[i+int(n/2)] /= 2
            #Ya que esto se hace en cada iteracion, esto terminará dividiendo los valores finales por n.
        w *= wn

def multiply(a, b):
    """
    Entrada: Un arreglo A y un arreglo B, dichos arreglos son de coeficientes que representan los polinomios
    Salida: La multiplicacion de A y B, usando la propiedad A * B = InverseDFT(DFT(A) * DFT(B))
    """
    c, ans = [], []
    fa = [complex(a[i], 0) for i in range(len(a))]
    fb = [complex(b[i], 0) for i in range(len(a))]

    n = 1
    while n < len(a) + len(b):
        n *= 2

    for i in range(len(fa), n):
        fa.append(complex(0, 0))
        fb.append(complex(0, 0))

    #convertir a punto valor
    fft(fa, False)
    fft(fb, False)

    #multiplicar en punto valor con coste O(n)
    for i in range(n):
        c.append(fa[i] * fb[i])

    #vuelvo a la representacion de coeficientes
    fft(c, True)

    for i in range(n):
        ans.append(round(c[i].real))

    return ans

def solve(A, B):
    ans = 0
    ta = A[::-1]
    tb = B
    for i in range(len(A)):
        ta.append(0)
        tb.append(B[i])

    C = multiply(ta, tb)
    m = len(A)
    for i in range(m-1, 2*m-1):
        if C[i] == 0:
            ans += 1
    return ans

def main():
    line = stdin.readline()
    while len(line) != 0:
        n = int(line)
        b1 = [0 if x == 'B' else 1 for x in stdin.readline().strip()]
        b2 = [0 if x == 'B' else 1 for x in stdin.readline().strip()]
        ans = solve(b1, b2)
        print(ans)
        line = stdin.readline()

main()
