import sys
from funciones import *

def main(): 
    driver = generarDriver()
    ingresar(driver)
    input("Presione una tecla para terminar.")
    
if __name__ == "__main__":
    sys.exit(main())