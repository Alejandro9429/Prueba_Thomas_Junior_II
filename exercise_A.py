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

    
def create_output(conteo):
    with open("salida_A.txt", "w", encoding="utf-8") as salida:
        salida.write(str(len(conteo)) + "\n")
        salida.write(" ".join(str(v) for v in conteo.values()))

open_file()