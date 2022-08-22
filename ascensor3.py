class Ascensor:
    def __init__(self):
        self.pisoActual = 1

    def moverse(self, dir='s'):
        if dir.lower() == 's':
            self.pisoActual += 1
            print(f'\nsubiendo, piso {self.pisoActual}')
        if dir.lower() == 'b':
            self.pisoActual -= 1
            print(f'\nbajando, piso {self.pisoActual}')

norte = Ascensor()
sur = Ascensor()

def inicialN(norte, pisoUsuario):
    while norte.pisoActual < pisoUsuario:
        norte.moverse('s')
    print(f'\nestamos en el piso {norte.pisoActual}')

def subiendoN(norte, destinoUsuario):
    while norte.pisoActual < destinoUsuario:
        norte.moverse('s')
    print(f'\nestamos en el piso {norte.pisoActual}')

def bajandoN(norte, destinoUsuario):
    while norte.pisoActual > destinoUsuario:
        norte.moverse('b')
    print(f'\nestamos en el piso {norte.pisoActual}')

def inicialS(sur, pisoUsuario):
    while sur.pisoActual < pisoUsuario:
        sur.moverse('s')
    print(f'\nestamos en el piso {sur.pisoActual}')

def subiendoS(sur, destinoUsuario):
    while sur.pisoActual < destinoUsuario:
        sur.moverse('s')
    print(f'\nestamos en el piso {sur.pisoActual}')

def bajandoS(sur, destinoUsuario):
    while sur.pisoActual > destinoUsuario:
        sur.moverse('b')
    print(f'\nestamos en el piso {sur.pisoActual}')

def error():
    print(f'\n?, no fume cochinadas')

ubicacion  = int(input('va a usar cuál ascensor?, 1 para norte, 2 para sur: '))

if ubicacion == 1:
    pisoUsuario = int(input('\nen qué piso está ubicado?: '))

    if pisoUsuario >= 2 and pisoUsuario <= 10:
        inicialN(norte, pisoUsuario)

        rumboUsuario = input('\nsube o baja?: ')
        destinoUsuario = int(input('\npara qué piso va?: '))

        if rumboUsuario == 's' and destinoUsuario >= 2 and destinoUsuario <= 10:
            subiendoN(norte, destinoUsuario)
        elif rumboUsuario == 'b' and destinoUsuario >= 1 and destinoUsuario <= 10:
            bajandoN(norte, destinoUsuario)
        else:
            error()

    else:
        error()
    
elif ubicacion == 2:
    pisoUsuario = int(input('\nen qué piso está ubicado?: '))

    if pisoUsuario >= 2 and pisoUsuario <= 10:
        inicialS(sur, pisoUsuario)

        rumboUsuario = input('\nsube o baja?: ')
        destinoUsuario = int(input('\npara qué piso va?: '))

        if rumboUsuario == 's' and destinoUsuario >= 2 and destinoUsuario <= 10:
            subiendoS(sur, destinoUsuario)
        elif rumboUsuario == 'b' and destinoUsuario >= 1 and destinoUsuario <= 10:
            bajandoS(sur, destinoUsuario)
        else:
            error()

    else:
        error()
