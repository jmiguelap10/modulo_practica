import sys
from modelos.inventario import Inventario
from modelos.producto import Producto
from modelos.producto_perecedero import ProductoPerecedero
from modelos.producto_digital import ProductoDigital
from modelos.excepciones import ProductoNoEncontradoError, StockInsuficienteError
from persistencia.almacenamiento import AlmacenamientoJSON
from modelos.producto_estandar import ProductoEstandar


def mostrar_menu() -> None:
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
    print("1. Listar productos y métricas")
    print("2. Registrar producto estándar")
    print("3. Registrar producto perecedero")
    print("4. Registrar producto digital")
    print("5. Buscar producto")
    print("6. Retirar stock (venta/despacho)")
    print("7. Salir")


def listar_productos(inv: Inventario) -> None:
    if not inv.productos:
        print("\n[!] El inventario está vacío.")
        return

    print("\n--- Listado de Productos ---")
    for prod in inv.productos:
        tipo = type(prod).__name__
        print(f"- [{tipo}] {prod.nombre} | Precio: ${prod.precio:,.2f} | Stock: {prod.stock}")

    print("----------------------------")
    print(f"Total unidades: {inv.total_unidades()}")
    print(f"Valorización total: ${inv.valor_total_inventario():,.2f}")


def registrar_producto_estandar(inv: Inventario, storage: AlmacenamientoJSON) -> None:
    try:
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio unitario: "))
        stock = int(input("Stock inicial: "))
        
        nuevo = ProductoEstandar(nombre, precio, stock)
        inv.agregar_producto(ProductoEstandar("Monitor 24\"", 750000.0, 8))
        storage.guardar(inv)
        print(f"[OK] Producto \"{nuevo.nombre}\" agregado y guardado en disco.")
    except (ValueError, TypeError) as err:
        print(f"[ERROR] Datos inválidos: {err}")


def registrar_producto_perecedero(inv: Inventario, storage: AlmacenamientoJSON) -> None:
    try:
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio unitario: "))
        stock = int(input("Stock inicial: "))
        dias = int(input("Días para caducar: "))

        nuevo = ProductoPerecedero(nombre, precio, stock, dias)
        inv.agregar_producto(nuevo)
        storage.guardar(inv)
        print(f"[OK] Producto perecedero \"{nuevo.nombre}\" agregado y guardado en disco.")
    except (ValueError, TypeError) as err:
        print(f"[ERROR] Datos inválidos: {err}")


def registrar_producto_digital(inv: Inventario, storage: AlmacenamientoJSON) -> None:
    try:
        nombre = input("Nombre del producto digital: ")
        precio = float(input("Precio unitario: "))
        enlace = input("Enlace de descarga: ")

        nuevo = ProductoDigital(nombre, precio, enlace)
        inv.agregar_producto(nuevo)
        storage.guardar(inv)
        print(f"[OK] Producto digital \"{nuevo.nombre}\" agregado y guardado en disco.")
    except (ValueError, TypeError) as err:
        print(f"[ERROR] Datos inválidos: {err}")


def buscar_producto_cli(inv: Inventario) -> None:
    nombre = input("Nombre del producto a buscar: ")
    try:
        prod = inv.buscar_producto(nombre)
        print(f"\n[Encontrado] {prod.nombre} | Tipo: {type(prod).__name__} | Precio: ${prod.precio:,.2f} | Stock: {prod.stock}")
        
        if isinstance(prod, ProductoPerecedero):
            print(f"  -> Días restantes: {prod.dias_para_caducar} | Precio liquidación: ${prod.calcular_precio_liquidado():,.2f}")
        elif isinstance(prod, ProductoDigital):
            print(f"  -> Enlace de descarga: {prod.enlace_descarga}")
            
    except ProductoNoEncontradoError as err:
        print(f"[ERROR] {err}")


def retirar_stock_cli(inv: Inventario, storage: AlmacenamientoJSON) -> None:
    nombre = input("Nombre del producto a retirar: ")
    try:
        cantidad = int(input("Cantidad a retirar: "))
        inv.retirar_stock(nombre, cantidad)
        storage.guardar(inv)
        prod = inv.buscar_producto(nombre)
        print(f"[OK] Stock actualizado y guardado en disco. Stock actual de \"{prod.nombre}\": {prod.stock}")
    except (ProductoNoEncontradoError, StockInsuficienteError, ValueError) as err:
        print(f"[ERROR] No se pudo procesar el retiro: {err}")


def main() -> None:
    storage = AlmacenamientoJSON("inventario.json")
    inv = storage.cargar()

    opciones = {
        "1": lambda: listar_productos(inv),
        "2": lambda: registrar_producto_estandar(inv, storage),
        "3": lambda: registrar_producto_perecedero(inv, storage),
        "4": lambda: registrar_producto_digital(inv, storage),
        "5": lambda: buscar_producto_cli(inv),
        "6": lambda: retirar_stock_cli(inv, storage),
        "7": lambda: sys.exit(0),
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()
        accion = opciones.get(opcion)

        if accion:
            accion()
        else:
            print("\n[!] Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()