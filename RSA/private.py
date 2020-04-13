p = 47
q = 71

n = p * q
flux = (p - 1) * (q - 1)
eKey = 79


# prima gen
lower = 1 
upper = 20
print("Bilangan prima antara",lower,"and",upper,":") 
# for num in range(lower,upper + 1): 
#     if num > 1: 
#         for i in range(2,num): 
#             if (num % i) == 0: 
#                 break 
#         else: 
#             print(num)

for num in range(lower , upper + 1):
    if num > 1:
        for i in range(2,num):
            if(num & i) == 0:
                break
        else:
            print(num)
        # bangkitkan key public (e)
        # if i relatif flux:
            
# bangkitkan nilai e tanpa random
# !bisa di  bagi 1 - 10 termasuk bilangan prima
# z = 5 % 2
# print(z)
# initNilai = 0
# if()
# print(p,q,n,flux)

#         for i in range(flux):
#             # print(i)
#             if i > 1:
#                 # print(i)
#                 if (eKey * i) % flux == 1:
#                     print("nilai",i)


# p = 1019 * 79
# print(p)
    