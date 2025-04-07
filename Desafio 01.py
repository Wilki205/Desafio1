eh01 = int(input("Hora: "))
em01 = int(input("Minuto: "))
eh02 = int(input("Hora: "))
em02 = int(input("Minuto: "))

somah = eh01 + eh02
somam = em01 + em02

if somam >= 60:
    somah += somam // 60
    somam = somam % 60

somah = somah % 24

if somah % 12 == 0:
    hora12 = 12
else:
    hora12 = somah % 12

print(f"Saída às {hora12:02d}:{somam:02d}")
