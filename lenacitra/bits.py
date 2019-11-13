# konversi ascii to bit
frasa = "Samarinda 2019"
for ch in frasa:
    bits = format(ord(ch), '08b')
    print(ch, '\t', ord(ch), '\t', bits)
    for bit in bits:
        print(bit, end=' -- ')

    print("\n\n")