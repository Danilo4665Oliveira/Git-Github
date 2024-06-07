num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o primeiro número: "))

operacao = input("Digite a opeação que deseja realizar (+,-,*,/): ")

if operacao == '+':
    print(num1+num2)
elif operacao == '-':
    print(abs(num1-num2))
elif operacao == '*':
    print(num1*num2)
elif operacao == '/':
    print(num1/num2)
else:
    print("Operação inválida")