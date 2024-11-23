import re
from typing import List, Any


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)




def compara_assinatura(as_a, as_b):
    '''Compara duas assinaturas e retorna o grau de similaridade.'''
    soma_diferencas = 0
    for i in range(len(as_a)):
        soma_diferencas += abs(as_a[i] - as_b[i])
    return soma_diferencas / 6  # Dividido por 6, pois há 6 traços linguísticos


def calcula_assinatura(texto):
    '''Calcula a assinatura de um texto.'''
    sentencas = separa_sentencas(texto)
    frases = [frase for sentenca in sentencas for frase in separa_frases(sentenca)]
    palavras = [palavra for frase in frases for palavra in separa_palavras(frase)]

    wal = sum(len(palavra) for palavra in palavras) / len(palavras)
    ttr = n_palavras_diferentes(palavras) / len(palavras)
    hlr = n_palavras_unicas(palavras) / len(palavras)
    sal = sum(len(sentenca) for sentenca in sentencas) / len(sentencas)
    sac = len(frases) / len(sentencas)
    pal = sum(len(frase) for frase in frases) / len(frases)

    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''Avalia os textos e retorna o número do texto mais similar ao da assinatura de COH-PIAH.'''
    similaridade_minima = float('inf')
    texto_infectado = 0

    for i, texto in enumerate(textos, start=1):
        ass_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(ass_texto, ass_cp)

        if similaridade < similaridade_minima:
            similaridade_minima = similaridade
            texto_infectado = i

    return texto_infectado
