# Alexa Katalina Garzon Medina
# 213022_869
# Ingeniería de Sistemas
# Código Fuente: autoría propia

# Problema 3

# Matriz de inventario
INVENTARIO = [
    #['Codigo','Producto','Stock actual','Stock mínimo'],
    ['A101', 'Teclado',4, 10],
    ['A102', 'Mouse', 20, 15],
    ['A103', 'Monitor', 5, 12],
    ['A104', 'USB', 17, 10],
    ['A105', 'Laptop', 2, 7]
]

# Función para Calcular el stock
def calcular_pedido(stock_actual, stock_minimo):
    """Calcula la cantidad a pedir para reponer el inventario."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0
print("Inventario y pedidos:")

# Recorrer la matriz
for producto in INVENTARIO:
    codigo = producto[0]
    nombre = producto[1]
    stock_actual = producto[2]
    stock_minimo = producto[3]
    cantidad_a_pedir = calcular_pedido(stock_actual, stock_minimo)
    print(f"Producto: {nombre} (Código: {codigo}) - Stock actual: {stock_actual} - Stock mínimo: {stock_minimo} - Cantidad a pedir: {cantidad_a_pedir}")
