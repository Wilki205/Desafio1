#proble: Dados os valores de horarios abaixo, decifre a logica e faça um codigo para executar.

eh01 = int(input("digite hora da entrada: "))
em01 = int(input("digite minuto: "))
eh02 = int(input("digite hora da entrada: "))
em02 = int(input("digite minuto: "))

somahora = eh01+eh02
somamin = em01+em02

if somamin>=60:
    min = somamin-60
if somahora>=12:
    hora = somahora-12

print (f"{hora+1}:{min}")