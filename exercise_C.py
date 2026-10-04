from datetime import datetime, timedelta

FORMATO = "%d/%m/%Y %H:%M:%S:%z"
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
HORAS_POR_DIA = 8


def leer_fecha(mensaje):
    while True:
        texto = input(mensaje).strip()
        try:
            return datetime.strptime(texto, FORMATO)
        except ValueError:
            print("Formato incorrecto. Ejemplo: 12/02/2026 19:25:35:+0000")


def contar_dias_semana(inicio, fin):
    conteo = [0] * 7
    dia = inicio.date()
    ultimo = fin.date()
    while dia <= ultimo:
        conteo[dia.weekday()] += 1
        dia = dia + timedelta(days=1)
    return conteo


def horas_laborales(conteo):
    dias_laborales = sum(conteo[:5])
    return dias_laborales * HORAS_POR_DIA


def calcular_diferencia(inicio, fin):
    segundos = (fin - inicio).total_seconds()
    horas = segundos / 3600
    dias = segundos / 86400
    return segundos, horas, dias


def main():
    fecha_1 = leer_fecha("Ingresa la fecha A (DD/MM/AAAA hh:mm:ss:+0000): ")
    fecha_2 = leer_fecha("Ingresa la fecha B (DD/MM/AAAA hh:mm:ss:+0000): ")

    if fecha_1 > fecha_2:
        fecha_1, fecha_2 = fecha_2, fecha_1

    fecha_2_local = fecha_2.astimezone(fecha_1.tzinfo)

    conteo = contar_dias_semana(fecha_1, fecha_2_local)
    print("\nDías entre las fechas (ambos extremos incluidos):")
    for nombre, cantidad in zip(DIAS, conteo):
        print(f"  {nombre}: {cantidad}")

    print("\nHoras laborales:", horas_laborales(conteo))

    segundos, horas, dias = calcular_diferencia(fecha_1, fecha_2)
    print("\nDiferencia entre las fechas:")
    print(f"  Segundos: {segundos:.0f}")
    print(f"  Horas: {horas:.2f}")
    print(f"  Días: {dias:.2f}")


if __name__ == "__main__":
    main()