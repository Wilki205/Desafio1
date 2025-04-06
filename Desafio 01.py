eh01 = int(input("Digite a hora da entrada: "))
em01 = int(input("Digite o minuto: "))
eh02 = int(input("Digite a hora da entrada: "))
em02 = int(input("Digite o minuto: "))

somah = eh01+eh02
somam = em01+em02

if somam >= 60:
        somah += somam // 60
        somam = somam % 60

somah = somah % 24

print (f"Saida as {somah:02d}:{somam:02d}")