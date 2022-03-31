valor = float(input("Digite o valor da compra: "))

if valor > 200:
    desconto = valor * 1.20
    valorTot =  (2* valor) - desconto 
    print(f"O valor da sua compra com o desconto de 20% é R${valorTot:.2f}")

else:
    print(f"O valor da sua compra é R${valor:.2f}")