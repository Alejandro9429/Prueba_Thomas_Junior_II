def open_file():
    with open("entry_E_A.txt", "r", encoding="utf-8") as archivo:
        n = int(archivo.readline())
        conteo = {}
        data = archivo.readlines()
        contar_palabras(n, conteo, data)
        return n, conteo, data

def contar_palabras(n, conteo, data):
    for i in range(n):
        palabra = data[i].strip()
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    create_output(conteo)
    return conteo

    
def build_output_text(conteo):
    first_line = str(len(conteo))
    second_line = " ".join(str(v) for v in conteo.values())
    return first_line + "\n" + second_line


def create_output(conteo):
    text = build_output_text(conteo)
    with open("salida_A.txt", "w", encoding="utf-8") as salida:
        salida.write(text)
    print(text)

n, conteo, data = open_file()
print(conteo)