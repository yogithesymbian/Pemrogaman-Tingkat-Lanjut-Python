from color import ColorPrint as warna
import csvlib as my

warna.print_pass("Hello Mr X ....")

# text = input("Masukan Pesan :")
text = "samarinda~~~"
key = 2


def encryption():
    hasilEnc = ""
    for ch in text:
        encrypt = ord(ch) + key
        encrypt = encrypt%128
        # if encrypt > 126:
        #     encrypt = 32 + encrypt % 127
        hasilEnc = hasilEnc + chr(encrypt)

    print("\nEncryption : ", hasilEnc)
    return hasilEnc

def decryption(text1):
    hasilDec = ""
    for ch in text1:
        decrypt = ord(ch) - key
        decrypt = decrypt%128
        # if decrypt > 126:
        #     decrypt = 126 - decrypt %127
        hasilDec = hasilDec + chr(decrypt)

    print("\nDecryption : ", hasilDec)

def start():
    print("\nteks asli : ", text)
    # encryption()
    hasil = encryption()
    decryption(hasil)
    # print("\nDecryption : ", hasilDec)


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt as err:
        print(
            "\n[!] By ...: thanks for use my code (c) 2019 github.com/yogithesymbian")
        sys.exit(0)