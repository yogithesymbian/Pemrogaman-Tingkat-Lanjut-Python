# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:58:55 2019

@author: AhmadRam
"""
import libtext as my

fileteks = '/root/PycharmProject/PemrogamanTingkatLanjut/ramli/TAplaintext.txt'
pesan = my.readTextFile(fileteks)
kun=10
bit=['0','0','0','0','0','0','0','0']
jmlbit=cypher=''
for ch in pesan:
    bits = format(ord(ch), '08b')

    for i in range(8):
        bit[i]=bits[(kun+i)%8]
        jmlbit+=bit[i]
    huruf=jmlbit
    test=chr(int(huruf,2))
    cypher+=test
    jmlbit=''
#reverse susunan teks
reverse=my.reverse(cypher)
print("Plaintext\t=",pesan)
print("Cyphertext\t=",reverse)

my.writeTextFile("/root/PycharmProject/PemrogamanTingkatLanjut/ramli/TAcypher.txt",reverse)