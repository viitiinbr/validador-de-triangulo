# Validador de Triângulo

n1 = float(input('digite um comprimento\n'))
n2 = float(input('digite um outro comprimento\n'))
n3 = float(input('digite um outro comprimento\n'))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print(f'{n1},{n2} e {n3} formam um triangulo')
else:
    print(f'{n1},{n2} e {n3} não formam um triangulo')

def tipo_trian (n1,n2,n3):
    if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
        if n1 == n2 == n3:
            return 'triangulo equilatero'
        elif n1 == n2 or n1 == n3 or n2 == n3:
            return 'triangulo isosceles'
        else:
            return 'triangulo escaleno'
    else:
        return 'não é um triangulo valido'

resultado = tipo_trian (n1,n2,n3)
print(resultado)