import time 
import numpy as numpy
import sys 

#imprimir con demora..
def imprimir_con_retraso(s):
    #imprimir una letra a la vez 
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
#crear la clase 
class Pokemon:
    def __init__(self, nombre, tipos, movimientos, EVs, puntos_de_salud='===================='):
        #guardar las variables como tribujo uwu 
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ataque = EVs['ataque']
        self.defensa = EVs['defensa']
        self.puntos_de_salud = puntos_de_salud
        self.barras = 20 

    def impresa(self,Pokemon2):
        '''Imprimir información de lucha
        '''
        print("\t----BATALLA POKEMON!!!!!!----")
        print(f"\n{self.nombre}")
        print(f"Tipo/: {self.tipos}")
        print(f"ataque/: {self.ataque}")
        print(f"defensa/: {self.defensa}")
        print("Nv/: ", 3*(1+np.mean( [self.ataque,self.defensa])))
        print("\nVS")
        print(f"\n{Pokemon2.nombre}")
        print("tipo/", Pokemon2.tipos)
        print("ataque/", Pokemon2.ataque)
        print("defensa/", Pokemon2.defensa)
        print("NV/: ", 3*(1+np.mean([Pokemon2.ataque,Pokemon2.defensa])))
        time.sleep(2)

    def ventaja(self,Pokemon2):
        '''Considerar la ventaja del tipo
        Actualiza poderes de ataque y defensa uwu
        devuelve dos cadenas de información :3 
        '''
        version = ['fuego', 'agua', 'planta']
        for i,k in enumerate(version):
            
            if self.tipos == k:
                #Son tipo mismo
                if Pokemon2.tipos == k:
                    cadena_1_ataque = '\nNo es muy efectivo u.u...'
                    cadena_2_ataque = '\nNo es muy efectivo unu...'

                #Pokemon2 es FUERTE
                if Pokemon2.tipos == version[(i+1)%3]:
                    Pokemon2.ataque *= 2
                    Pokemon2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /= 2
                    cadena_1_ataque = '\nNo es muy efectivo u.u ....'
                    cadena_2_ataque = '\n¡Es muy eficaz!!!!!! omg daño masivo'

                #Pokemon2 es DEBIL
                if Pokemon2.tipos == version[(i+2)%3]:
                    self.ataque *= 2
                    self.defensa *= 2
                    Pokemon2.ataque /= 2
                    Pokemon2.defensa /= 2
                    cadena_1_ataque = '\n¡Es muy eficaz!!!! wow daño craneoencefalico irreversible '
                    cadena_2_defensa = '\nNo es muy efectivo.... troste'
            
            
            return cadena_1_ataque, cadena_2_ataque

    def turno(self, Pokemon2, cadena_1_ataque, cadena_2_ataque):
        '''Empieza con Pokemon1, elige ataque y calcular
        los nuevos puntos de salud uwu.
        Haz lo mismo con Pokemon2. Sigue hasta que los puntos de salud de uno los pokemons sea < 0
        Actualizar los datos.
        '''
        while (self.barras > 0) and (Pokemon2.barras > 0):
            #imprime los puntos de salud de cada pokemon :3 
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}")


            #POKEMON 1
            print(f"¡Adelante {self.nombre}!!!")
            for i, x in enumerate(self.movimientos):
                print(f"{i+1}.", x)
            index = int(input("Elige un movimiento!!: "))
            imprimir_con_retraso(f"\n{self.nombre} usó {self.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_1_ataque)

            #determinar el daño
            Pokemon2.barras -= self.ataque
            Pokemon2.puntos_de_salud = ""

            # Agregar barras adicionales más defensa boost 
            for j in range(int(Pokemon2.barras+.1*Pokemon2.defensa)):
                Pokemon2.puntos_de_salud += "="

            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
            time.sleep(.5)

            #comprueba si su pokemon se debilitó 
            if Pokemon2.barras <= 0:
                imprimir_con_retraso("\n..." + Pokemon2.nombre, "se murició...")
                break

            #POKEMON 2
            print(f"¡Adelante {Pokemon2.nombre}!!")
            
            for i, x in enumerate(Pokemon2.nombre):
                print(f"{i+1}.", x)
            index = int(input("Elige un movimiento!!: "))
            imprimir_con_retraso(f"\n{Pokemon2.nombre} usó {Pokemon2.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_2_ataque)

            #determinar el daño
            self.barras -= Pokemon2.ataque
            self.puntos_de_salud = ""

            # Ag regar barras adicionales más defensa boost 
            for j in range(int(self.barras+.1*self.defensa)):
                self.puntos_de_salud += "="

            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
            time.sleep(.5)

            #comprueba si su pokemon se debilitó 
            if self.barras <= 0:
                imprimir_con_retraso("\n..." + self.nombre, "se murició...")
                break

    def lucha (self, Pokemon2):
        '''Permitir que dos pokemon luchen entre ellos
        '''

        #Imprimir información de lucha
        self.impresa(Pokemon2)
        #Considerar la ventaja de tipo
        cadena_1_ataque, cadena_2_ataque = self.ventaja(Pokemon2)

        #Ahora para la lucha real ... 
        #Continua mientras pokemon aún tenga puntos_de_salud
        self.turno(Pokemon2, cadena_1_ataque, cadena_2_ataque)

        #Recibir dinero (premio)   
        money = np.random.choice(5000)
        imprimir_con_retraso(f"\nEl oponente te pago ${money}.\n")
if __name__ == '__main__':
    #crear pokemon objeto
    Charizard = Pokemon('Charizard', 'fuego', ['Lanzallamas', 'Pirotecnia', 'Giro fuego', 'Ascuas'], {'ataque':12, 'defensa': 8})
    Blastoise = Pokemon('Blastoise', 'Agua', ['Pistola agua', 'Burbuja', 'Hidropulso', 'Hidrobomba'], {'ataque':18, 'defensa': 10})
    Venusaur =  Pokemon('Venusaur', 'planta', ['Latigo Cepa', 'Hoja Afilada', 'Rayo Solar', 'Abatidoras'], {'ataque':8, 'defensa': 12})
    Charizard.lucha(Blastoise)



    # #informe:
    # sigue sin funcionar ni una wea u.u pero ya me dio paja seguirlo, quizás cuando encuentre la solución en otra parte, lo continue
    # triste, desde que abro los ojos, hasta que gracias a dios lo cierro