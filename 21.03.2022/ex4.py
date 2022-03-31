contaLuz = float(input("Digite o valor da sua conta de luz: "))
contaAg = float(input("Digite o valor da sua conta de água: "))
contaTel = float(input("Digite o valor da sua conta de telefone: "))
salario = float(input("Digite o valor do seu salário: "))

contasTotal = contaLuz + contaAg + contaTel
resto = salario - contasTotal


if salario < contasTotal:
    print("Salário insuficiente!")

else:
    print(f"Restará R${resto:.2f} do seu salário após pagar todas as contas")


