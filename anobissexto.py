# Crie um programa que receba um ano e verifique se ele é bissexto. Um ano é bissexto se for divisível por 4, exc
ano = int(input("insira um ano: "))

if ano %400==0:
    print ("bissexto")
elif ano %100==0:
        print ("não é bissexto")
elif ano %4==0:
        print ("bissexto")
else:
    print ("não é bissexto")