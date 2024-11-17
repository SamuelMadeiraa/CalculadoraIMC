def calcular_imc(peso, altura):
    """Calcula o IMC baseado no peso e altura."""
    return peso / (altura ** 2)
def classificar_imc(imc):
    """Classifica o IMC em categorias."""
    if imc < 18.05:
        return 'Abaixo do peso ideal'
    elif 18.05 <= imc <= 24.9:
        return 'Peso normal'
    elif 25 <= imc < 29.9:
        return 'Sobrepeso'
    elif 30 <= imc < 34.9:
        return 'Obesidade grau I'
    elif 35 <= imc < 39.9:
        return 'Obesidade grau II'
    else:
        return 'Obesidade mórbida'
