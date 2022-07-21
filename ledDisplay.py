'''
    Programa para simular el funcionamiento de un display numérico de Leds individuales
'''

# Library to print text with colors
from colorama import init, Fore
init(autoreset=True)

# Clean the screen
import os
clear = lambda: os.system('cls')
clear()

# Dictionary with the digits definition
dictDigits = {
    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('#####'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###')
}

# Function to draw the digits simulating a LED display
def digitDraw(digits):
    digitDisplay = ''
    for row in range(len(dictDigits['0'])):
        print(Fore.RED + ' '.join(dictDigits[i][row] for i in str(digits)))
        digitDisplay += digitDisplay
    return digitDisplay

# Main program
print('Este script permite visualizar cualquier número entero positivo en una versión de LED Display.\n')

try:
    digits = int(input('Ingrese un número entero positivo: '))
    if digits >= 0 and digits % 1 == 0:
        print('\nEsta es la versión en Led Display del número', digits, ':\n')
        print(digitDraw(digits))
    else:
        print(Fore.RED + '\nSolo se aceptan números enteros positivos, por favor intente de nuevo.\n')
except:
    print(Fore.RED + '\nUsted no ha ingresado un número entero positivo, por favor intente de nuevo.\n')
