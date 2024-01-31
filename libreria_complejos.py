import math

def suma(a,b):
    suma_real = a[0]+b[0]
    suma_complejo = a[1]+b[1]
    return (suma_real, suma_complejo)

def multiplicacion(a,b):
    multiplicacion_real = (a[0]*b[0])-(a[1]*b[1])
    multiplicacion_complejo = (a[0]*b[1])+(a[1]*b[0])
    return (multiplicacion_real, multiplicacion_complejo)

def division(a,b):
    div = ((b[0]**2)+(b[1]**2))
    if div != 0:
        division_real = ((a[0]*b[0])+(a[1]*b[1]))/ div
        division_complejo = ((b[0]*a[1])-(a[0]*b[1]))/div
        return (division_real, division_complejo)
    else:
        raise Exception ("No es valido, su divisor es igual a 0")

def resta(a,b):
    resta_real = a[0] - b[0]
    resta_complejo = a[1] - b[1]
    return (resta_real, resta_complejo)

def modulo(a):
    modu = ((a[0]**2)+(a[1]**2))**(1/2)
    return modu

def conjugado(a):
    conju = (a[0],-a[1])
    return conju

def cart_to_polar(a):
    modulo = ((a[0]**2)+(a[1]**2))**(1/2)
    fase = math.atan2(a[1],a[0])
    return (modulo, fase)

def polar_to_cart(c):
    a = c[0]*math.cos(c[1])
    b = c[0]*math.sin(c[1])
    return (a,b)

def fase(a):
    fase_complejo = math.atan2(a[1], a[0])
    return fase_complejo
