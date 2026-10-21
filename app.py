#Importar en con subcarpetas
from colorama import Fore, Style    
from servicios.finanzas import calcular_iva

iva_calculado = calcular_iva(10000)
print(Fore.GREEN + f"El IVA de 1000 es: {iva_calculado}")

