#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nome do Script: Teste.py
Descrição: Este script processa o arquivo CSV de dados de vendas,
realiza a limpeza e gera um relatório consolidado.
Autor: Guilherme Brandão
Data: 2025-08-21
Versão: 1.0
Licença: MIT
"""
## pra que serve uma docstring em python?

## segue abaixo exercício:

#  COMPREHENSIONS EM PYTHON 
# - List comprehension (básico, filtro, if-else inline, aninhado)
# - Set comprehension (deduplicação, normalização)
# - Dict comprehension (mapeamento, filtro, inversão segura)
# - Generator expression (convertendo para tupla)
#
# Dica importante:
# "tuple comprehension" não existe como sintaxe própria — usamos
# um *generator expression* dentro de tuple(...).

from collections import Counter

SENTINEL = object()

#  1) LIST: básico 
# Quadrados de 0 a 9 -> [0, 1, 4, ..., 81]
quadrados = ...

#  2) LIST: com filtro 
# Pares de 0 a 20 (inclusive)
pares_ate_20 = ...

#  3) LIST: if-else inline (no lugar do elemento) 
# Para n em 0..4, "par" se n % 2 == 0, senão "ímpar"
par_ou_impar = ...

#  4) LIST: aninhado (flatten + filtro) 
# Pegue apenas os > 0 e "achate" em uma lista única
listas = [[1, -1, 2], [0, 3, 4], [-2, 5]]
positivos = ...

#  5) LIST: transposição de matriz com 2 for 
# M = 2x3 -> MT = 3x2
M = [[1, 2, 3],
     [4, 5, 6]]
MT = ...

#  6) SET: deduplicação/normalização 
# Deixe tudo minúsculo e sem duplicatas
palavras = ["Maçã", "banana", "BANANA", "maçã", "Pêra"]
unicas_lower = ...

#  7) DICT: mapeamento + filtro 
# Mapeie nome -> tamanho somente se len>=4
nomes = ["Ana", "Bruno", "Clara", "Jo"]
tam_nomes = ...

#  8) DICT: inversão segura (mantendo apenas valores únicos) 
# d tem valores repetidos; inverta (valor->chave) somente se o valor ocorre 1x
d = {"a": 1, "b": 2, "c": 1, "d": 3}
contagem = Counter(d.values())
inv_unicos = ...

#  9) GENERATOR: para tupla 
# Gere primos em [2, 29] e converta para tupla com tuple(<generator>)
def is_prime(n: int) -> bool:
    if n < 2: return False
    if n % 2 == 0: return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

tupla_primos = ...

#  10) DICT: com enumerate 
# Mapeie índice iniciando em 1 -> quadrado do número (0..4)
idx_quadrados = ...

#  11) LIST: 2 for + condição final (ordem importa) 
# Todos os pares (i, j) com i,j em {1,2,3} em que i*j é par
pares_produto_par = ...

# ---------------- 12) LIST: diferença entre 'if' filtro x 'if-else' inline ----
# out_filtro: dobre somente positivos
# out_inline: dobre positivos e ponha 0 nos demais
nums = [-2, -1, 0, 1, 2]
out_filtro = ...
out_inline = ...


############################################################################### TESTES 
def _garanta(*vars_e_nomes):
    for v, nome in vars_e_nomes:
        assert v is not SENTINEL and v is not ..., f"Preencha a variável: {nome}"

def _testes():
    print(">> Rodando testes...")

    _garanta(
        (quadrados, "quadrados"),
        (pares_ate_20, "pares_ate_20"),
        (par_ou_impar, "par_ou_impar"),
        (positivos, "positivos"),
        (MT, "MT"),
        (unicas_lower, "unicas_lower"),
        (tam_nomes, "tam_nomes"),
        (inv_unicos, "inv_unicos"),
        (tupla_primos, "tupla_primos"),
        (idx_quadrados, "idx_quadrados"),
        (pares_produto_par, "pares_produto_par"),
        (out_filtro, "out_filtro"),
        (out_inline, "out_inline"),
    )

    # 1
    assert quadrados == [n*n for n in range(10)]
    # 2
    assert pares_ate_20 == list(range(0, 21, 2))
    # 3
    assert par_ou_impar == ["par", "ímpar", "par", "ímpar", "par"]
    # 4
    assert positivos == [1, 2, 3, 4, 5]
    # 5
    assert MT == [[1, 4], [2, 5], [3, 6]]
    # 6
    assert unicas_lower == {"maçã", "banana", "pêra"}
    # 7
    assert tam_nomes == {"Bruno": 5, "Clara": 5}
    # 8
    assert inv_unicos == {2: "b", 3: "d"}
    # 9
    assert isinstance(tupla_primos, tuple)
    assert tupla_primos == (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    # 10
    assert idx_quadrados == {1: 0, 2: 1, 3: 4, 4: 9, 5: 16}
    # 11
    esperado = [(1,2),(2,1),(2,2),(2,3),(3,2)]
    assert pares_produto_par == esperado
    # 12
    assert out_filtro == [2, 4]
    assert out_inline == [0, 0, 0, 2, 4]

    print("feito.")

_testes()
