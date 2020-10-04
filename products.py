products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name) 
	p.append(price)
	products.append(p) #簡化寫法: products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是: ', p[1])

with open('products.csv', 'w', endcoding='utf-8') as f: #endcoding這行為防止中文字發生亂碼
	f.write('商品,價格\n')
	for p in products: #for loop
		f.write(p[0] + ',' + p[1] + '\n' )