class Complejo:
    def __init__(self, real, imaginaria):
        self.real = real
        self.imaginaria = imaginaria

    def suma(self, otro):
        return Complejo(self.real + otro.real,
                        self.imaginaria + otro.imaginaria)

    def resta(self, otro):
        return Complejo(self.real - otro.real,
                        self.imaginaria - otro.imaginaria)

    def multiplicacion(self, otro):
        real = self.real * otro.real - self.imaginaria * otro.imaginaria
        imaginaria = self.real * otro.imaginaria + self.imaginaria * otro.real
        return Complejo(real, imaginaria)

    def division(self, otro):
        denominador = otro.real**2 + otro.imaginaria**2
        real = (self.real * otro.real + self.imaginaria * otro.imaginaria) / denominador
        imaginaria = (self.imaginaria * otro.real - self.real * otro.imaginaria) / denominador
        return Complejo(real, imaginaria)

    def modulo(self):
        valor = (self.real**2 + self.imaginaria**2) ** 0.5
        return Complejo(valor, 0)

    def formato(self, decimales=2):
        signo = "-" if self.imaginaria < 0 else "+"
        return f"{self.real:.{decimales}f}{signo}{abs(self.imaginaria):.{decimales}f}i"


def ingresar_numero():
    real = float(input("Ingrese la parte real: "))
    imaginaria = float(input("Ingrese la parte imaginaria: "))
    return Complejo(real, imaginaria)


def main():
    a = ingresar_numero()
    b = ingresar_numero()

    print("A =", a.formato())
    print("B =", b.formato())
    print("A + B →", a.suma(b).formato(1))
    print("A - B →", a.resta(b).formato(1))
    print("A * B →", a.multiplicacion(b).formato(2))
    print("A / B →", a.division(b).formato(2))
    print("Mod(A) →", a.modulo().formato(2))
    print("Mod(B) →", b.modulo().formato(2))


if __name__ == "__main__":
    main()