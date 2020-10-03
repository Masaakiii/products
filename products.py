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

print(products[0][0]) #第一個零為大清單的, 第二個零為小清單