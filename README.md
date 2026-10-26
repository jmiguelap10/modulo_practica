# Sistema de Gestión de Inventario en Python

Sistema modular de gestión de inventarios desarrollado bajo principios de **Programación Orientada a Objetos (POO)**, diseño guiado por contratos mediante **Clases Base Abstractas (ABC)**, persistencia desacoplada en formato **JSON** y cobertura automatizada con **pytest**.

---

## 🏛 Arquitectura y Decisiones de Diseño

El sistema está estructurado bajo una separación estricta de responsabilidades (**SRP**):

* **Dominio (`modelos/`):** Contiene la lógica del negocio pura y las entidades del catálogo, blindadas mediante encapsulamiento estricto (`@property` y setters defensivos) para prevenir estados inconsistentes.
* **Persistencia (`persistencia/`):** Aísla la serialización y lectura de disco. Emplea un patrón de fábrica polimórfica para reconstruir instancias concretas sin acoplar el dominio al almacenamiento físico.
* **Pruebas (`test/`):** Suite completa con 33 pruebas unitarias y de integración que validan casos de éxito, límites numéricos, tipos de datos y manejo de excepciones personalizadas.
* **Interfaz de Usuario (`main.py`):** CLI interactiva con despachador desacoplado de comandos mediante funciones diferidas (`lambda`).

### Diagrama de Clases

```text
       ┌────────────────────────┐
       │     Producto (ABC)     │
       ├────────────────────────┤
       │ - nombre: str          │
       │ - precio: float        │
       │ - stock: int           │
       ├────────────────────────┤
       │ + aplicar_descuento()  │
       │ + reducir_stock()*     │
       │ + to_dict()*           │
       └───────────▲────────────┘
                   │
         ┌─────────┴───────────────┐
         │                         │
┌────────┴─────────┐     ┌─────────┴────────────┐
│ ProductoEstandar │     │   ProductoDigital    │
├──────────────────┤     ├──────────────────────┤
│                  │     │ - enlace_desc: str   │
├──────────────────┤     ├──────────────────────┤
│ + reducir_stock()│     │ + reducir_stock()    │
│ + to_dict()      │     │ + to_dict()          │
└────────▲─────────┘     └──────────────────────┘
         │
┌────────┴──────────────┐
│  ProductoPerecedero   │
├───────────────────────┤
│ - dias_caducar: int   │
├───────────────────────┤
│ + precio_liquidado()  │
│ + to_dict()           │
└───────────────────────┘
(*) Métodos abstractos obligatorios.