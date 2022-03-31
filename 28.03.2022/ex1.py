idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("não-eleitor")
elif idade >= 18 and idade <= 65:
    print("eleitor obrigatório")

else:
    print("eleitor facultativo")
