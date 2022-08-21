class Ascensor:
    def __init__(self):
        self.pisoActual = 1

    def moverse(self, dir='s'):
        if dir.lower() == 's':
            if self.pisoActual < 10:
                print(f'\nsubiendo, piso {self.pisoActual}')
                self.pisoActual += 1
            else:
                print('no puede subir más')
        if dir.lower() == 'b':
            if self.pisoActual > 1:
                print(f'\nbajando, piso {self.pisoActual}')
                self.pisoActual -= 1
            else:
                print('no puede bajar más')

ascNorte = Ascensor()
ascSur = Ascensor()

def opcN_S():
    posUsuario = int(input('ingrese su ubicación [1: Norte, 2: Sur] ==>> '))
    return posUsuario

posUsuario = opcN_S()

# norte
def actualN(ascNorte):
    print(f'\npiso {ascNorte.pisoActual}, llegamos <<==\n')

def destinoN(ascNorte, actual, destinoUsuario, finUsuario):
    if destinoUsuario  == 's':
        while ascNorte.pisoActual < finUsuario:
            ascNorte.moverse('s')
        actual(ascNorte)
    elif destinoUsuario == 'b':
        while ascNorte.pisoActual > finUsuario:
            ascNorte.moverse('b')
        actual(ascNorte)

def inicialN(ascNorte, actual, pisoUsuario):
    while pisoUsuario > ascNorte.pisoActual:
        ascNorte.moverse('s')
    actual(ascNorte)

# sur
def actualS(ascSur):
    print(f'\npiso {ascSur.pisoActual}, llegamos\n')

def destinoS(ascSur, actual, destinoUsuario, finUsuario):
    if destinoUsuario  == 's':
        while ascSur.pisoActual < finUsuario:
            ascSur.moverse('s')
        actual(ascSur)
    elif destinoUsuario == 'b':
        while ascSur.pisoActual > finUsuario:
            ascSur.moverse('b')
        actual(ascSur)

def inicialS(ascSur, actual, pisoUsuario):
    while pisoUsuario > ascSur.pisoActual:
        ascSur.moverse('s')
    actual(ascSur)

# generales
def eleccion():
    destinoUsuario = input('baja o sube?: ')
    finUsuario = int(input('\na que piso va? '))
    return destinoUsuario,finUsuario

def remate():
    nombre = input('tu nombre es?: ')
    despedida = print(f'\nregresa pronto, {nombre}')

if posUsuario == 1:
    pisoUsuario = int(input('\nen qué piso está?: '))
    inicialN(ascNorte, actualN, pisoUsuario)
    destinoUsuario, finUsuario = eleccion()
    destinoN(ascNorte, actualN, destinoUsuario, finUsuario)
    remate()
elif posUsuario == 2:
    pisoUsuario = int(input('\nen qué piso está?: '))
    inicialS(ascSur, actualS, pisoUsuario)
    destinoUsuario, finUsuario = eleccion()
    destinoS(ascSur, actualS, destinoUsuario, finUsuario)
    remate()