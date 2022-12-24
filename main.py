from random import choice, choices, randint
import unidecode as unidecode


class CopaDoMundo():
    def __init__(self):
        self.selecoes_classificadas = []
        self.selecoes_fracos = []
        self.selecoes_medios = []
        self.selecoes_fortes = []
        self.chave_a = []
        self.chave_b = []

    def seleciona_32_selocoes(self):
        cup = ["França", "Inglaterra", "Brasil"]
        w_cup = []
        #abre o txt que contém paises selecionados e os add a lista linha
        arquivo = open("paises.txt", encoding='utf-8', mode='r')
        linha = []
        for l in arquivo:
            l = l.strip()
            linha.append(l)
        arquivo.close()
        #seleciona aleatoriamente 29 paises da lista linha
        while len(w_cup) < 32:
            cup.append(choice(linha))
            for e in cup:
                if e not in w_cup:
                    w_cup.append(e)
        #remove os acentos e adiciona ao self
        for i in range(len(w_cup)):
            w_cup[i] = unidecode.unidecode(w_cup[i])
            self.selecoes_classificadas.append(w_cup[i])

    def set_ordena_32_selecoes(self):
        return self.selecoes_classificadas.sort()

    def mede_forca_selecoes(self):
        for selecao in self.selecoes_classificadas:
            roll = randint(1,6)
            if roll == 1:
                self.selecoes_fracos.append(selecao)
            elif roll == 6:
                self.selecoes_fortes.append(selecao)
            else:
                self.selecoes_medios.append(selecao)

    def separa_chaves(self):
        sorteados_chave = []
        while len(self.chave_a) <= 3:
            time = choice(self.selecoes_classificadas)
            if time not in sorteados_chave:
                if time not in self.chave_a:
                    self.chave_a.append(time)
                    sorteados_chave.append(time)

        while len(self.chave_b) <= 3:
            time = choice(self.selecoes_classificadas)
            if time not in sorteados_chave:
                if time not in self.chave_b:
                    self.chave_b.append(time)
                    sorteados_chave.append(time)

    def separa_chaves2(self):
        chave = []
        lista_chave = []
        sorteados = []

        for c in range(1,9):
            chave.clear()
            while len(chave) <=4:
                time = choice(self.selecoes_classificadas)
                if time not in sorteados:
                    if time not in chave:
                        chave.append(time)
                        sorteados.append(time)







    def __str__(self):
        return f'COPA DO MUNDO NIGHT CITY\n' \
               f'As seleções classificadas para a copa foram:\n{self.selecoes_classificadas}\n' \
               f'\nAs seleções consideradas:\nFracas: {self.selecoes_fracos}\nMedias: {self.selecoes_medios}\nFortes: {self.selecoes_fortes}\n' \
               f'\nCHAVES\nChave A\n{self.chave_a}\nChave B\n{self.chave_b}' \









copa = CopaDoMundo()
copa.seleciona_32_selocoes()
copa.set_ordena_32_selecoes()
copa.mede_forca_selecoes()
copa.separa_chaves()
print(copa)
