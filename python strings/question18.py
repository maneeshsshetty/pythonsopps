amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount) 
amount1 = "32.054,23"

amount1 = amount1.replace('.', '#')   
amount1 = amount1.replace(',', '.')
amount1 = amount1.replace('#', ',') 
print(amount1)