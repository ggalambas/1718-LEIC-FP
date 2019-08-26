# FUNDAMENTOS DA PROGRAMACAO
# PROJETO 1 - PALAVRA GURU
# 86430 GUILHERME GALAMBAS


# <artigo_def>::=A|O
# <vogal_palavra>::=<artigo_def>|E
def vogal_palavra(car):
    return car in ('A', 'O', 'E')

# <vogal>::=I|U|<vogal_palavra>
def vogal(car):
    return car in ('I', 'U') or vogal_palavra(car)

# <ditongo_palavra>::=AI|AO|EU|OU
def ditongo_palavra(car):
    return car in ('AI', 'AO', 'EU', 'OU')

# <ditongo>::=AE|AU|EI|OE|OI|IU|<ditongo_palavra>
def ditongo(car):
    return car in ('AE', 'AU', 'EI', 'OE', 'OI', 'IU') or ditongo_palavra(car)

# <par_vogais>::=<ditongo>|IA|IO
def par_vogais(car):
    return car in ('IA', 'IO') or ditongo(car)

# <consoante_terminal>::=L|M|R|S|X|Z
def consoante_terminal(car):
    return car in ('L', 'M', 'R', 'S', 'X', 'Z')

# <consoante_final>::=N|P|<consoante_terminal>
def consoante_final(car):
    return car in ('N', 'P') or consoante_terminal(car)

# <consoante>::=B|C|D|F|G|H|J|L|M|N|P|Q|R|S|T|V|X|Z
def consoante(car):
    return car in ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z')

# <par_consoantes>::=BR|CR|FR|GR|PR|TR|VR|BL|CL|FL|GL|PL
def par_consoantes(car):
    return car in ('BR', 'CR', 'FR', 'GR', 'PR', 'TR', 'VR', 'BL', 'CL', 'FL', 'GL', 'PL')

# <consoante_freq>::=D|L|M|N|P|R|S|T|V
# <monossilabo_2>::=AR|IR|EM|UM|<vogal_palavra>S|<ditongo_palavra>
#               |<consoante_freq><vogal>
def monossilabo_2(car):
    return car in ('AR', 'IR', 'EM', 'UM') or\
           vogal_palavra(car[0]) and car[1]=='S' or\
           ditongo_palavra(car) or\
           car[0] in ('D', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'V') and vogal(car[1])

# <monossilabo_3>::=<consoante><vogal><consoante_terminal>
#               |<consoante><ditongo>
#               |<par_vogais><consoante_terminal>
def monossilabo_3(car):
    return consoante(car[0]) and vogal(car[1]) and consoante_terminal(car[2]) or\
           consoante(car[0]) and ditongo(car[1:]) or\
           par_vogais(car[:2]) and consoante_terminal(car[2])

# <monossilabo>::=<vogal_palavra>|<monossilabo_2>|<monossilabo_3>
def monossilabo(car, tamanho):
    if tamanho == 3:
        return monossilabo_3(car)
    elif tamanho == 2:
        return monossilabo_2(car)
    elif tamanho == 1:
        return vogal_palavra(car)
    else:
        return False

# <silaba_2>::=<par_vogais>|<consoante><vogal>|<vogal><consoante_final>
def silaba_2(car):
    return par_vogais(car) or\
           consoante(car[0]) and vogal(car[1]) or\
           vogal(car[0]) and consoante_final(car[1])

# <silaba_3>::=QUA|QUE|QUI|GUE|GUI|<vogal>NS|<consoante><par_vogais>
#               |<consoante><vogal><consoante_final>
#               |<par_vogais><consoante_final>
#               |<par_consoantes><vogal>
def silaba_3(car):
    return car in ('QUA', 'QUE', 'QUI', 'GUE', 'GUI') or\
           vogal(car[0]) and car[1:]=='NS' or\
           consoante(car[0]) and par_vogais(car[1:]) or\
           consoante(car[0]) and vogal(car[1]) and consoante_final(car[2]) or\
           par_vogais(car[:2]) and consoante_final(car[2]) or\
           par_consoantes(car[:2]) and vogal(car[2])

#<silaba_4>::=<par_vogais>NS|<consoante><vogal>NS|<consoante><vogal>IS
#               |<par_consoantes><par_vogais>
#               |<consoante><par_vogais><consoante_final>
def silaba_4(car):
    return par_vogais(car[:2]) and car[2:]=='NS' or\
           consoante(car[0]) and vogal(car[1]) and car[2:] in ('NS', 'IS') or\
           par_consoantes(car[:2]) and par_vogais(car[2:]) or\
           consoante(car[0]) and par_vogais(car[1:3]) and consoante_final(car[3])

# <silaba_5>::=<par_consoantes><vogal>NS
def silaba_5(car):
    return par_consoantes(car[:2]) and vogal(car[2]) and car[3:]=='NS'

# <silaba_final>::=<monossilabo_2>|<monossilabo_3>|<silaba_4>|<silaba_5>
def silaba_final(car, tamanho):
    if tamanho == 5:
        return silaba_5(car)
    elif tamanho == 4:
        return silaba_4(car)
    elif tamanho == 3:
        return monossilabo_3(car)
    elif tamanho == 2:
        return monossilabo_2(car)

# <silaba>::=<vogal>|<silaba_2>|<silaba_3>|<silaba_4>|<silaba_5>
def silaba(car, tamanho):
    if tamanho == 5:
        return silaba_5(car)
    elif tamanho == 4:
        return silaba_4(car)
    elif tamanho == 3:
        return silaba_3(car)
    elif tamanho == 2:
        return silaba_2(car)
    elif tamanho == 1:
        return vogal(car)
    else:
        return False

# <palavra>::=<monossilabo>|<silaba>*<silaba_final>
def palavra(car, tamanho):

    # funcao auxiliar a' verificacao da silaba final
    def final_aux(car, tamanho):
        if tamanho == 1 or silaba_final(car, tamanho):
            return tamanho
        else:
            return final_aux(car[1:], tamanho-1)

    # funcao auxiliar ao teste das silabas
    def palavra_aux(car, tamanho):
        if tamanho == 0:
            return True
        elif tamanho > 5:
            i_max = 5
        else:
            i_max = tamanho
        # faz o teste do fim da palavra para o inicio
        # testanto das silabas maiores para as mais pequenas
        for i in range(i_max, 0, -1):
            if silaba(car[tamanho-i:], i):
                return palavra_aux(car[:tamanho-i], tamanho-i)
        return False

    # testa se a cadeia de caracteres e' um monossilabo
    if monossilabo(car, tamanho):
        return True
    # verifica se a ultima silaba e' uma silaba final
    if tamanho > 5:
        tamanho_final = final_aux(car[tamanho-5:], 5)
    else:
        tamanho_final = final_aux(car, tamanho)

    # retira a silaba final e testa se o resto da palavra
    # e' composta por silabas
    if tamanho_final != 1:
        tamanho -= tamanho_final
        return palavra_aux(car[:tamanho], tamanho)
    else:
        return False

# e_silaba: cad. caracteres > booleano
def e_silaba(car):
    if not isinstance(car, str):
        raise ValueError('e_silaba:argumento invalido')
    tamanho = len(car)
    return silaba(car, tamanho)

# e_monossilabo : cad. caracteres > booleano
def e_monossilabo(car):
    if not isinstance(car, str):
        raise ValueError('e_monossilabo:argumento invalido')
    tamanho = len(car)
    return monossilabo(car, tamanho)

# e_palavra : cad. caracteres > booleano
def e_palavra(car):
    if not isinstance(car, str):
        raise ValueError('e_palavra:argumento invalido')
    tamanho = len(car)
    return palavra(car, tamanho)
