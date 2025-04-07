eh01, em01, eh02, em02 = int(input("Hora: ")), int(input("Minuto: ")), int(input("Hora: ")), int(input("Minuto: "))
print(f"Saída às {(eh01 + eh02 + (em01 + em02) // 60) % 12:02d}:{(em01 + em02) % 60:02d}")
