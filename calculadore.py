def calculadora ():

    while True:
        try:


            print("=== Calculadora ===")


            numero_1 = float(input("Digite o primeiro numero: "))

            operacao = str(input("Digite a operação desejada (+), (-), (*), (/): "))

            numero_2 = float(input("Digite o segundo numero: "))


            if operacao == "+":
                resultado = numero_1 + numero_2
                break
            elif operacao == "-":
                resultado = numero_1 - numero_2
                print(f"{numero_1} - {numero_2} = {resultado}")
                break
            elif operacao == "*":
                resultado = numero_1 * numero_2
                print(f"{numero_1} * {numero_2} = {resultado}")
                break
            elif operacao == "/":
                resultado = numero_1 / numero_2
                print(f"{numero_1} / {numero_2} = {resultado}")
                break
            else:
                ("Digite um valor valido")

        except ValueError:
            print("Voce não Digitou um valor correto")



calculadora()