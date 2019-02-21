from random import choice
from time import sleep
import sys
from os import get_terminal_size as get_size
from string import ascii_lowercase as string
from colored import fg, attr

class Architect:
    def __init__(self, recomeco=False):
        if not recomeco:
            print(fg('green'))
        print('\n'*30)
        self.colunas, self.linhas = list(get_size())
        self.minCol, self.maxCol = int(self.colunas/3), int(self.colunas/2)
        self.linhas_matrix, self.local = [], dict()
        for a in range(self.linhas):
            self.linhas_matrix.append(' ' * self.colunas)
        self.parar, self.trava = False, False
        self._gerar_linhas()

    def _gerar_linhas(self):
        self.trava = (True if len(self.local) >= self.maxCol
                      or self.parar else False)
        for a in self.local.copy():
            self.local[a] = [n + 1 for n in self.local[a]]
            if self.local[a][0] == self.linhas + 1:
                self.local.pop(a)
        if not self.trava:
            ponta = choice(range(self.linhas//3))
            if len(self.local) >= self.minCol:
                if choice([0, 1]):
                    nova_lista = list(filter(self._notIn, range(self.colunas)))
                    coluna = choice(nova_lista)
                    self.local[coluna] = [-choice(range(24)), ponta]
            elif len(self.local) >= 0:
                nova_lista = list(filter(self._notIn, range(self.colunas)))
                coluna = choice(nova_lista)
                self.local[coluna] = [-choice(range(24)), ponta]

    def _refazer_strings(self):
        for linha in range(self.linhas):
            temp = self.linhas_matrix[linha].replace(fg('white'), '')
            temp = temp.replace(fg('grey_89'), '').replace(fg('grey_66'), '')
            temp = list(temp.replace(fg('green'), ''))
            for coluna in self.local:
                a, b = self.local[coluna]
                if temp[coluna] == ' ' and linha == b:
                    temp[coluna] = fg('white') + choice(string) + fg('green')
                elif temp[coluna] != ' ' and abs(a-b) > 1 and linha == b-1:
                    temp[coluna] = fg('grey_89') + choice(string) + fg('green')
                elif temp[coluna] != ' ' and abs(a-b) > 2 and linha == b-2:
                    temp[coluna] = fg('grey_66') + choice(string) + fg('green')
                elif temp[coluna] != ' ' and linha not in range(a, b):
                    temp[coluna] = ' '
            self.linhas_matrix[linha] = ''.join(temp)

    def _notIn(self, item):
        return item not in self.local

    def rain(self):
        try:
            display = [self.colunas, self.linhas]
            while self.local and display == list(get_size()):
                for linha in self.linhas_matrix:
                    print(linha)
                self._gerar_linhas()
                self._refazer_strings()
                sleep(0.07)  # 0.1
            if display != list(get_size()):
                self.__init__(True)
                sleep(0.26)
                self.rain()
        except KeyboardInterrupt:
            self.parar = True
            self.rain()


def texto_efeito_pausa(texto: str):
    for a in texto:
        print(a, end='')
        sys.stdout.flush()
        sleep(0.04)
    print()


def main():
    texto_efeito_pausa('Running Matrix')
    sleep(1)
    matrix = Architect()
    matrix.rain()
    for linha in matrix.linhas_matrix:
        print(linha)
    print(attr(0))
    texto_efeito_pausa(attr(0) + '\nDisconnected.')


if __name__ == '__main__':
    main()



