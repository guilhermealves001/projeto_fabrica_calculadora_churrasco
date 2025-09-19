# Crie uma função para calcular o total de carnes e bebidas para um churrasco
convi = int(input("Digite o número de covidados: "))

def calcular_bebidas(convi, cons_pessoal = 800, volume_garrafa = 2.25):
    total_ml = convi * cons_pessoal
    total_litro = total_ml/1000
    garrafas = int(total_litro//volume_garrafa)
    if total_litro % volume_garrafa > 0:
        garrafas += 1
    return total_litro, garrafas

#resultado = calcular_bebidas(convi)
#print(resultado)

def calcular_carne(convi, consumo_carne = 400):
    total_gramas = convi * consumo_carne
    total_kg = total_gramas / 1000
    return total_kg

litros, garrafas = calcular_bebidas(convi)
carne_kg = calcular_carne(convi)

print("/n___Quantidade total para churrasco")
print(f"Número de convidados: {convi}")
print(f"Refrigerantes necessários: {litros:.2f} litros")
print(f"Garrafas de 2,5L: {garrafas} unidades")
print(f"carne necessária: {carne_kg:.2f} Kg")