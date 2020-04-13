# konversi ascii to bit
frasa = "Samarinda 2019"
for ch in frasa:
    bits = format(ord(ch), '08b') # to binary from dec
    print(ch, '\t', ord(ch), '\t', bits) # char
    for bit in bits:
        print(bit, end=' -- ') # binary

    print("\n\n")