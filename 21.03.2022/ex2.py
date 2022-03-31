turno = input("Digite o turno em que você trabalha (M|T|N): ")
horas = int(input("Digite a quantidade de horas que você trabalha: "))

if turno.upper()== "N":
    valor = 45
    salario = horas * valor
    print(f"Seu salário é igual a R${salario:.2f}")

else:
    valor = 37.50
    salario = horas * valor
    print(f"Seu salário é igual a R${salario:.2f}")

