# 86430 GUILHERME GALAMBAS
# FUNDAMENTOS DA PROGRAMACAO
# PROJETO 2 - PALAVRA GURU MULTI JOGADOR

from functions1_sol import e_palavra
from itertools import permutations


#TAD PALAVRA_POTENCIAL

# cria_palavra_potencial: cad. caracteres x tuplo de letras --> palavra_potencial
def cria_palavra_potencial(cad, t):

    if not( isinstance(cad, str) and isinstance(t, tuple) ):
        raise ValueError('cria_palavra_potencial:argumentos invalidos.')
    for el in t:
        if not ord('A') <= ord(el) <= ord('Z'):
            raise ValueError('cria_palavra_potencial:argumentos invalidos.')

    lst = list(t)
    for car in cad:
        if not ord('A') <= ord(car) <= ord('Z'):
            raise ValueError('cria_palavra_potencial:argumentos invalidos.')
        elif car not in lst:
            raise ValueError('cria_palavra_potencial:a palavra nao e valida.')
        lst.remove(car)

    return cad

# palavra_tamanho: palavra_potencial --> inteiro
def palavra_tamanho(pp):
    return len(pp)

# e_palavra_potencial: universal --> logico
def e_palavra_potencial(uni):

    if isinstance(uni, str):
        for el in uni:
            if not ord('A') <= ord(el) <= ord('Z'):
                return False
        return True
    return False

# palavras_potenciais_iguais: palavra_potencial x palavra_potencial --> logico
def palavras_potenciais_iguais(pp1, pp2):
    return pp1 == pp2

# palavra_potencial_menor: palavra_potencial x palavra_potencial --> logico
def palavra_potencial_menor(pp1, pp2):

    if palavras_potenciais_iguais(pp1, pp2):
        return False

    i = 0
    while i <= palavra_tamanho(pp1) and i <= palavra_tamanho(pp2):
        if pp1[i] != pp2[i]:
            return pp1[i] < pp2[i]
        i+=1

    return palavra_tamanho(pp1) == i-1

# palavra_potencial_para_cadeia: palavra_potencial --> cad. caracteres
def palavra_potencial_para_cadeia(pp):

    cad = ''
    for el in pp:
        cad += el

    return cad


# TAD CONJUNTO_PALAVRAS

class conjunto_palavras:
    def __init__(self):
        self.pps = {}
        self.tam = 0

    def acrescentar(self):
        self.tam += 1

    def chaves(self):
        return sorted(self.pps.keys())

# cria_conjunto_palavras: --> conjunto_palavras
def cria_conjunto_palavras():
    return conjunto_palavras()

# numero_palavras: conjunto_palavras --> inteiro
def numero_palavras(conj):
    return conj.tam

# subconjunto_por_tamanho: conjunto_palavras x inteiro --> lista
def subconjunto_por_tamanho(conj, tam):

    if tam in conj.pps:
        return conj.pps[tam]

    return []

# acrescenta_palavra: conjunto_palavras x palavra_potencial -->
def acrescenta_palavra(conj, pp):

    if not( e_conjunto_palavras(conj) and e_palavra_potencial(pp) ):
        raise ValueError('acrescenta_palavra:argumentos invalidos.')

    adicionado = False
    tam = palavra_tamanho(pp)

    if tam not in conj.pps:
        conj.pps[tam] = []

    if pp not in conj.pps[tam]:
        conj.acrescentar()
        for el in conj.pps[tam]:
            if palavra_potencial_menor(pp, el):
                pos = conj.pps[tam].index(el)
                conj.pps[tam].insert(pos, pp)
                adicionado = True
                break
        if not adicionado:
            conj.pps[tam].append(pp)

# e_conjunto_palavras: universal --> logico
def e_conjunto_palavras(uni):
    return isinstance(uni, conjunto_palavras)

# conjuntos_palavras_iguais: conjunto_palavras x conjunto_palavras --> logico
def conjuntos_palavras_iguais(conj1, conj2):
    if numero_palavras(conj1) == numero_palavras(conj2) and conj1.chaves() == conj2.chaves():
        for tam in conj1.pps:
            if subconjunto_por_tamanho(conj1, tam) != subconjunto_por_tamanho(conj2, tam):
                return False
        return True
    return False

# conjunto_palavras_para_cadeia: conjunto_palavras --> cad. caracteres
def conjunto_palavras_para_cadeia(conj):

    cad = ''
    for tam in conj.chaves():
        cad += str(tam) + '->['
        for pp in subconjunto_por_tamanho(conj, tam):
            cad += palavra_potencial_para_cadeia(pp) + ', '
        cad = cad[:-2] + '];'

    return '[' + cad[:-1] + ']'


# TAD JOGADOR

class jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
        self.validas = cria_conjunto_palavras()
        self.invalidas = cria_conjunto_palavras()

    def incrementar(self, pontos):
        self.pontuacao += pontos

    def decrementar(self, pontos):
        self.pontuacao -= pontos

# cria_jogador: cad. caracteres --> jogador
def cria_jogador(cad):

    if not isinstance(cad, str):
        raise ValueError('cria_jogador:argumento invalido.')

    return jogador(cad)

# jogador_nome: jogador --> cad. caracteres
def jogador_nome(jog):
    return jog.nome

# jogador_pontuacao: jogador --> inteiro
def jogador_pontuacao(jog):
    return jog.pontuacao

# jogador_palavras_validas: jogador --> conjunto_palavras
def jogador_palavras_validas(jog):
    return jog.validas

# jogador_palavras_invalidas: jogador --> conjunto_palavras
def jogador_palavras_invalidas(jog):
    return jog.invalidas

# adiciona_palavra_valida: jogador x palavra_potencial -->
def adiciona_palavra_valida(jog, pp):

    if not( e_jogador(jog) and e_palavra_potencial(pp) ):
        raise ValueError('adiciona_palavra_valida:argumentos invalidos.')

    if pp not in subconjunto_por_tamanho(jogador_palavras_validas(jog), palavra_tamanho(pp)):
        jog.incrementar(palavra_tamanho(pp))
        acrescenta_palavra(jogador_palavras_validas(jog), pp)

# adiciona_palavra_invalida: jogador x palavra_potencial -->
def adiciona_palavra_invalida(jog, pp):

    if not( e_jogador(jog) and e_palavra_potencial(pp) ):
        raise ValueError('adiciona_palavra_invalida:argumentos invalidos.')

    if pp not in subconjunto_por_tamanho(jogador_palavras_invalidas(jog), palavra_tamanho(pp)):
        jog.decrementar(palavra_tamanho(pp))
        acrescenta_palavra(jogador_palavras_invalidas(jog), pp)

# e_jogador: universal --> logico
def e_jogador(uni):
    return isinstance(uni, jogador)

# jogador_para_cadeia: jogador --> cad. caracteres
def jogador_para_cadeia(jog):
    return 'JOGADOR ' + jogador_nome(jog) + ' PONTOS=' + str(jogador_pontuacao(jog))\
        + ' VALIDAS=' + conjunto_palavras_para_cadeia(jogador_palavras_validas(jog))\
        + ' INVALIDAS=' + conjunto_palavras_para_cadeia(jogador_palavras_invalidas(jog))


# FUNCOES ADICIONAIS

# gera_todas_palavras_validas: tuplo de letras --> conjunto_palavras
def gera_todas_palavras_validas(t):

    conj = cria_conjunto_palavras()

    for i in range(len(t)):
        combinacoes = tuple(permutations(t, i+1))
        for el in combinacoes:
            cad = ''.join(el)
            if e_palavra( cad ):
                acrescenta_palavra(conj, cria_palavra_potencial(cad, t))

    return conj

# guru_mj: tuplo de letras -->
def guru_mj(t):

    print('Descubra todas as palavras geradas a partir das letras:\n' + str(t))
    print('Introduza o nome dos jogadores (-1 para terminar)...')
    jogadores = []
    num_jogadores = 0
    nome = input('JOGADOR ' + str(num_jogadores+1) + ' -> ')
    while nome != str(-1):
        jogadores.append(cria_jogador(nome))
        num_jogadores += 1
        nome = input('JOGADOR ' + str(num_jogadores+1) + ' -> ')

    palavras_validas = gera_todas_palavras_validas(t)
    restantes = numero_palavras(palavras_validas)
    jogada = 0
    n = 0
    tentativas = []

    while restantes != 0:

        jogada += 1
        print('JOGADA ' + str(jogada) + ' - Falta descobrir ' + str(restantes) + ' palavras')
        tentativa = input('JOGADOR ' + jogador_nome(jogadores[n]) + ' -> ')

        tentativa = cria_palavra_potencial(tentativa, t)
        tam = palavra_tamanho(tentativa)
        if tentativa in subconjunto_por_tamanho(palavras_validas, tam):
            print(tentativa + ' - palavra VALIDA')
            if tentativa not in tentativas:
                restantes -= 1
                tentativas.append(tentativa)
                adiciona_palavra_valida(jogadores[n], tentativa)
        else:
            print(tentativa + ' - palavra INVALIDA')
            adiciona_palavra_invalida(jogadores[n], tentativa)

        if n < num_jogadores-1:
            n += 1
        else:
            n = 0

    pontuacao_max = -float('inf')
    resultados = ''

    for jog in jogadores:

        resultados += jogador_para_cadeia(jog) + '\n'

        pontuacao = jogador_pontuacao(jog)
        if pontuacao > pontuacao_max:
            empate = False
            pontuacao_max = pontuacao
            vencedor = jogador_nome(jog)

        elif pontuacao == pontuacao_max:
            empate = True

    if not empate:
        print('FIM DE JOGO! O jogo terminou com a vitoria do jogador ' + vencedor + ' com ' + str(pontuacao_max) + ' pontos.')
    else:
        print('FIM DE JOGO! O jogo terminou em empate.')

    print(resultados[:-1])
