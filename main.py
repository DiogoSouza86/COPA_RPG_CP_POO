from random import choice, choices, randint
import unidecode as unidecode


class CopaDoMundo():
    def __init__(self):
        self.selecoes_classificadas = []
        self.selecoes_fracos = []
        self.selecoes_medios = []
        self.selecoes_fortes = ['Nigth City']
        self.chave_a = []
        self.chave_b = []
        self.chave_c = []
        self.chave_d = []
        self.chave_e = []
        self.chave_f = []
        self.chave_g = []
        self.chave_h = []


    def seleciona_32_selocoes(self):
        cup = ["França", "Inglaterra", "Brasil", "Nigth City"]
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
            if selecao != "Nigth City":
                roll = randint(1,6)
                if roll == 1:
                    self.selecoes_fracos.append(selecao)
                elif roll == 6:
                    self.selecoes_fortes.append(selecao)
                else:
                    self.selecoes_medios.append(selecao)

    def set_ordena_selecoes_fortes(self):
        return self.selecoes_fortes.sort()

    def separa_chaves2(self):
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

    def separa_chaves(self):
        sorteados_chave = self.selecoes_classificadas.copy()
        for c in range(1,9):

            chave = []
            #sorteia 4 times por chave
            while len(chave) <= 3:
                time = choice(sorteados_chave)
                if time not in chave:
                    sorteados_chave.remove(time)
                    chave.append(time)


            #aponta para qual self a variável chave é destinada
            if   c == 1:
                for item in chave:
                    self.chave_a.append(item)
            elif c == 2:
                for item in chave:
                    self.chave_b.append(item)
            elif c == 3:
                for item in chave:
                    self.chave_c.append(item)
            elif c == 4:
                for item in chave:
                    self.chave_d.append(item)
            elif c == 5:
                for item in chave:
                    self.chave_e.append(item)
            elif c == 6:
                for item in chave:
                    self.chave_f.append(item)
            elif c == 7:
                for item in chave:
                    self.chave_g.append(item)
            else:
                for item in chave:
                    self.chave_h.append(item)
            chave.clear()

    def gols_a(self):
        lista_gols =  [0, 1, 2, 3, 4, 5]
        if self.chave_a[0] in self.selecoes_fortes:
            if self.chave_a[1] in self.selecoes_fortes:
                gols = choices(lista_gols, weights=[0.5, 20.5, 25, 25, 10, 10])
                return gols
            elif self.chave_a[1] in self.selecoes_medios:
                gols = choices(lista_gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
                return gols
            elif self.chave_a[1] in self.selecoes_fracos:
                gols = choices(lista_gols, weights=[0.5, 20.5, 25, 25, 10, 10])
                return gols
        elif self.chave_a[0] in self.selecoes_medios:
            if self.chave_a[1] in self.selecoes_fortes:
                gols = choices(lista_gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
                return gols
            elif self.chave_a[1] in self.selecoes_medios:
                gols = choices(lista_gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
                return gols
            elif self.chave_a[1] in self.selecoes_fracos:
                gols = choices(lista_gols, weights=[10, 30, 30, 10, 10, 10])
                return gols
        elif self.chave_a[0] in self.selecoes_fracos:
            if self.chave_a[1] in self.selecoes_fortes:
                gols = choices(lista_gols, weights=[40.5, 30, 10, 0.5, 0.5, 0.5])
                return gols
            elif self.chave_a[1] in self.selecoes_medios:
                gols = choices(lista_gols, weights=[30, 30, 10, 10, 10, 10])
                return gols
            elif self.chave_a[1] in self.selecoes_fracos:
                gols = choices(lista_gols, weights=[30, 30, 20, 10, 0.5, 0.5])
                return gols

    def pontos4(self,time1, time2):
            if time1 in (times_fortes) and time2 in (times_fracos):
                gols = [0, 1, 2, 3, 4, 5]
                ff_gols = choices(gols, weights=[0.5, 20.5, 25, 25, 10, 10])
                return ff_gols
            if time1 in (times_fortes) and time2 in (times_medios):
                gols = [0, 1, 2, 3, 4, 5]
                ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
                return ff_gols
            if time1 in (times_fortes) and time2 in (times_fortes):
                gols = [0, 1, 2, 3, 4, 5]
                ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
                return ff_gols

            if time1 in (times_medios) and time2 in (times_fortes):
                gols = [0, 1, 2, 3, 4, 5]
                ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
                return ff_gols
            if time1 in (times_medios) and time2 in (times_medios):
                gols = [0, 1, 2, 3, 4, 5]
                ff_gols = choices(gols, weights=[30, 30, 25, 0.5, 0.5, 0.5])
                return ff_gols
            if time1 in (times_medios) and time2 in (times_fracos):
                gols = [0, 1, 2, 3, 4, 5]
                ff_gols = choices(gols, weights=[10, 30, 30, 10, 10, 10])
                return ff_gols

            if time1 in (times_fracos) and time2 in (times_fortes):
                gols = [0, 1, 2, 3, 4, 5]
                ff_gols = choices(gols, weights=[40.5, 30, 10, 0.5, 0.5, 0.5])
                return ff_gols
            elif time1 in (times_fracos) and time2 in (times_medios):
                gols = [0, 1, 2, 3, 4, 5]
                ff_gols = choices(gols, weights=[30, 30, 10, 10, 10, 10])
                return ff_gols
            elif time1 in (times_fracos) and time2 in (times_fracos):
                gols = [0, 1, 2, 3, 4, 5]
                ff_gols = choices(gols, weights=[30, 30, 20, 10, 0.5, 0.5])
                return ff_gols

    def pontos5(self, time1, time2):
        if time1 in self.selecoes_fortes and time2 in self.selecoes_fortes:

    def resultado_chave(self, g1, g2, g3, g4):

        print( f'{self.chave_a[0]} {g1} X {g2} {self.chave_a[1]}\n'
               f'{self.chave_a[2]} {g3} X {g4} {self.chave_a[3]}\n')

    def __str__(self):
        return f'COPA DO MUNDO NIGHT CITY\n' \
               f'As seleções classificadas para a copa foram:\n{self.selecoes_classificadas}\n' \
               f'\nAs seleções consideradas:\nFracas: {self.selecoes_fracos}\nMedias: {self.selecoes_medios}\nFortes: {self.selecoes_fortes}\n' \
               f'\nCHAVES\nChave A\n{self.chave_a}\nChave B\n{self.chave_b}\nChave C\n{self.chave_c}\nChave D\n{self.chave_d}\n' \
               f'Chave E\n{self.chave_e}\nChave F\n{self.chave_f}\nChave G\n{self.chave_g}\nChave H\n{self.chave_h}\n' \
               f'\nFASE DE GRUPOS\n' \
               f'' \


copa = CopaDoMundo()
copa.seleciona_32_selocoes()
copa.set_ordena_32_selecoes()
copa.mede_forca_selecoes()
copa.set_ordena_selecoes_fortes()
copa.separa_chaves()
print(copa)
g1 = copa.gols_a()
g2 = copa.gols_a()
g3 = copa.gols_a()
g4 = copa.gols_a()
copa.resultado_chave(g1, g2, g3, g4)
