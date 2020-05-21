import math
import cmath

PI = math.pi

def fft(A, invert):
    """
    Entrada: Un arreglo A de coeficiente, invert un booleano que me indica si necesito calcular la DFT o la DFT inversa
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
    ans = []
    fa = [complex(a[i], 0) for i in range(len(a))]
    fb = [complex(b[i], 0) for i in range(len(a))]

    n = 1
    while n < len(a) + len(b):
        n *= 2
    print(n)
    for i in range(len(fa), n):
        fa.append(complex(0, 0))
        fb.append(complex(0, 0))

    #convertir a punto valor
    fft(fa, False)
    fft(fb, False)

    #multiplicar en punto valor con coste O(n)
    for i in range(n):
        ans.append(fa[i] * fb[i])

    #vuelvo a la representacion de coeficientes
    fft(ans, True)

    ans2 = []
    for i in range(n):
        ans2.append(round(ans[i].real))

    return ans2

def main():
    #A = b1; B = b2
    A = [3,4,5]
    B = [2,1,2]
    ta = A[::-1]
    tb = B
    for i in range(len(A)):
        ta.append(0)
        tb.append(B[i])

    C = multiply(A, B)
    aux = []
    m = len(A)
    for i in range(m-1, 2*m-1):
        aux.append(C[i])
    print(aux)

main()
