#Importar en con subcarpetas
from colorama import Fore, Style    
from servicios.finanzas import calcular_iva

iva_calculado = calcular_iva(10000)
print(Fore.GREEN + f"El IVA de 1000 es: {iva_calculado}")

#from validaciones import es_mayor_de_edad

#edades = [15, 20, 17]

#for edad in edades:
    #if es_mayor_de_edad(edad):
        #print(f"Edad: {edad} Acceso permitido")
    #else:
        #print(f"Edad: {edad} Acceso denegado")
        
