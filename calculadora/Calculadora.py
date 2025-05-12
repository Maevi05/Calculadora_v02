def calcular_valor(num1, num2, operacao):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operacao == '+':
            return num1 + num2
        elif operacao == '-':
            return num1 - num2
        elif operacao == '*':
            return num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero.")
            return num1 / num2
        elif operacao == '^':
            return num1 ** num2
        else:
            raise ValueError("Operação inválida.")
    except ValueError as e:
        raise e

if __name__ == '__main__':
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    operacao = input("Digite a operação (+, -, *, /, ^): ")

    try:
        resultado = calcular_valor(num1, num2, operacao)
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(f"Erro: {e}")
