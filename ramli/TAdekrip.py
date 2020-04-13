# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:58:55 2019

@author: AhmadRam
"""
import libtext as my

fileteks = '/root/PycharmProject/PemrogamanTingkatLanjut/ramli/TAcypher.txt'
cypher = my.readTextFile(fileteks)
# cypher=reverse
kun=10
bit=['0','0','0','0','0','0','0','0']
jmlbit=plain=''
for ch in cypher:
    bits = format(ord(ch), '08b')

    for i in range(8):
        bit[i]=bits[(8-((kun-i)%8))%8]
        jmlbit+=bit[i]
    huruf=jmlbit
    test=chr(int(huruf,2))
    plain+=test
    jmlbit=''
#reverse susunan teks
reverse=my.reverse(plain)
print("Cyphertext\t=",cypher)
print("Plaintext\t=",reverse)