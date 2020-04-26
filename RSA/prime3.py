__author__ = "Yogi Arif Widodo"
__copyright__ = "(C) 2019"
__version__ = "0.1"
__email__ = "yogirenbox33@gmail.com"
__status__ = "Development"
__codename__ = 'Pemrograman-Tingkat-Lanjut-Python'
__source__ = "https://github.com/yogithesymbian/Pemrograman-Tingkat-Lanjut-Python"
__info__ = "URL scodeid"





for num in range(1,100 + 1):
    if num > 1: # pada saat num = 2 | if 2 > 1
        for i in range(2,num): # pas di line ini
            eliminasi = num % i
            if eliminasi == 0: # kodingan ini tidak di jalankan ? kenapa ?
                break  # kodingan ini tidak di jalankan ?
        else:  # kok langsung lari ke sini
            print(num) # dan mencetak angka 2
        # karena for ini range(2,2)

        # 7 line