loja1 = {'iphone 12','iphone 11', 'iphone 12 pro max', 'iphone 12 pro', 'iphone 12 mini'}
loja2 = { 'iphone 11', 'iphone 12', 'Samsung s20', 'Samsung s21', 'Samsung s21 ultra'}

print(f'Modelos disponiveis {loja1.union(loja2)}')
print(f'Modelos disponiveis em ambas {loja1.intersection(loja2)}')