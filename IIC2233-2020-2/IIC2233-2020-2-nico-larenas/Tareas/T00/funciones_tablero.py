import random
from tablero import print_tablero
from parametros import NUM_BARCOS
from parametros import RADIO_EXP
barcos = NUM_BARCOS
radio = RADIO_EXP

class Tablero:
    def __init__ (self, filas, columnas):
        self.barcos = barcos
        tab = []
        m = 0
        while m < int(filas):
            fila = []
            n = 0
            while n < int(columnas):
                fila.append(" ")
                n += 1
            tab.append(fila)
            m += 1
        self.tab = tab
        bar = 0
        while bar < barcos:
            coord_uno = random.randrange(0,filas)
            coord_dos = random.randrange(0,columnas)
            if self.tab[coord_uno][coord_dos] == " ":
                self.tab[coord_uno][coord_dos] = "B"
                bar += 1
    
    def bombas(self, letra, numero):
        if self.tab[numero][letra] == " ":
            self.tab[numero][letra] = "X"
        elif self.tab[numero][letra] == "B":
            self.tab[numero][letra] = "F"
            self.barcos -= 1
        
    def bomba_cruz(self, letra, numero):
        self.bombas(letra, numero)
        for bomba in range(numero - (radio - 1), numero + radio):
            if bomba < len(self.tab):
                self.bombas(letra, bomba)
        for bomba in range(letra - (radio - 1), letra + radio):
            if bomba < len(self.tab[0]):
                self.bombas(bomba, numero)
    
    def bomba_x(self, letra, numero):
        self.bombas(letra, numero)
        for bomba in range((2*radio)-1):
            let = letra + bomba - (radio - 1) 
            num= numero + bomba - (radio - 1)
            if l et < len(self.tab[0]) and num < len(self.tab) and let > 0 and num > 0:
                self.bombas(let, num)

        for bomba in range((2*radio)-1):
            let = letra + bomba - (radio - 1)
            num = numero - bomba + (radio - 1)
            if let < len(self.tab[0]) and num < len(self.tab) and let > 0 and num > 0:
                self.bombas(let, num)

    def bomba_diam(self, letra, numero):
        self.bombas(letra, numero)
        for bomba in range((radio)):
            for i in range ((2*bomba) + 1):
                let = letra + i - bomba
                num = numero + bomba - radio + 1
                if let < len(self.tab) and num < len(self.tab[0]) and let > 0 and num > 0:
                    self.bombas(let, num)

        for bomba in range((radio-1)):
            for i in range ((2*bomba) + 1):
                let = letra + i - bomba
                num = numero + radio -1 - bomba
                if let < len(self.tab) and num < len(self.tab[0]) and let > 0 and num > 0:
                    self.bombas(let, num)


    