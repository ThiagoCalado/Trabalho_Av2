valor_produto = float(input('Valor do produto: '))
taxa_imposto = int(input('Quanto de imposto: '))
por_taxa = taxa_imposto / 100
porcentagem_imposto = valor_produto * por_taxa
print(f'Valor do produto antes: {valor_produto}')
print(f'Taxa do imposto: {por_taxa}')
print(f'Valor do produto agora: {porcentagem_imposto}')