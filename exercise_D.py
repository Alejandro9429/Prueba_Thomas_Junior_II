GENEROS_VALIDOS = ("Masculino", "Femenino")


def solo_letras(texto):
    limpio = texto.replace(" ", "").replace("-", "")
    return limpio.isalpha()


def letras_y_numeros(texto):
    limpio = texto.replace(" ", "")
    return limpio.isalnum()


class Producto:
    def __init__(self, nombre, codigo_barras, fabricante, categoria, genero):
        nombre = nombre.strip()
        codigo_barras = codigo_barras.strip()
        fabricante = fabricante.strip()
        categoria = categoria.strip()
        genero = genero.strip().capitalize()

        if not letras_y_numeros(nombre):
            raise ValueError(f"Nombre inválido: {nombre!r}")
        if not codigo_barras.isdigit():
            raise ValueError(f"Código de barras inválido: {codigo_barras!r}")
        if not solo_letras(fabricante):
            raise ValueError(f"Fabricante inválido: {fabricante!r}")
        if not solo_letras(categoria):
            raise ValueError(f"Categoría inválida: {categoria!r}")
        if genero not in GENEROS_VALIDOS:
            raise ValueError(f"Género inválido: {genero!r}")

        self.nombre = nombre
        self.codigo_barras = codigo_barras
        self.fabricante = fabricante
        self.categoria = categoria
        self.genero = genero

    def __repr__(self):
        return f"Producto({self.nombre!r})"


def agrupar_productos(productos):
    agrupados = {}

    for p in productos:
        if p.fabricante not in agrupados:
            agrupados[p.fabricante] = {}
        categorias = agrupados[p.fabricante]

        if p.categoria not in categorias:
            categorias[p.categoria] = {}
        generos = categorias[p.categoria]

        if p.genero not in generos:
            generos[p.genero] = []
        generos[p.genero].append(p)

    return agrupados


def main():
    productos = [
        Producto("Zapatos XYZ", "8569741233658", "Deportes XYZ", "Zapatos", "Masculino"),
        Producto("Zapatos ABC", "7452136985471", "Deportes XYZ", "Zapatos", "Femenino"),
        Producto("Camisa DEF", "5236412896324", "Deportes XYZ", "Camisas", "Masculino"),
        Producto("Bolso KLM", "5863219635478", "Carteras Hi-Fashion", "Bolsos", "Femenino"),
    ]

    resultado = agrupar_productos(productos)

    from pprint import pprint
    pprint(resultado, sort_dicts=False)

    print(resultado["Deportes XYZ"]["Zapatos"]["Masculino"])

    try:
        Producto("Gorra 1", "12A45", "Deportes XYZ", "Gorras", "Masculino")
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()