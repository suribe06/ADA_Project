#Codigo realizado por Santiago Uribe Pastas identificado con el codigo de estudiante 8925546
"""
Código de honor:
Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
"""

from sys import stdin
from collections import deque

def check(reds, b2):
    """
    En la funcion check el arreglo reds almacena las posiciones en donde en el brazalete 1 hayuna R, y busco esas posiciones
    en el brazalete 2 y reviso si hay una R en esas posiciones. La respuesta la almeceno en una variable y la retorno
    """
    flag = True
    i = 0
    while i < len(reds) and flag:
        if b2[reds[i]] == 'R':
            flag = False
        i += 1
    return flag

def solve(n, b1, b2):
    ans, i = 0, 0
    reds = []

    #Almaceno en una lista los indices donde en el brazalete 1 hay una 'R'
    for j in range(n):
        if b1[j] == 'R':
            reds.append(j)

    #Simulo las rotaciones el brazalete 2 con un deque (popleft y append)
    #Y por cada rotacion del brazalete 2 reviso si forma una configuracion aceptable con el brazalete 1
    while i < n:
        first = b2[0]
        b2.popleft()
        b2.append(first)
        if check(reds, b2): #Si check retorna True indica que es una configuracion valida
            ans += 1
        i += 1
    return ans

def main():
    line = stdin.readline()
    while len(line) != 0:
        n = int(line)
        b1 = deque(stdin.readline().strip())
        b2 = deque(stdin.readline().strip())
        ans = solve(n, b1, b2)
        print(ans)
        line = stdin.readline()

main()
