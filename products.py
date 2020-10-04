#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f: # for loop
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',')  #split(str) 切割 strip() 移除
		products.append([name, price])
print(products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是: ', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #endcoding='utf-8' 這為防止中文字發生亂碼
	f.write('商品, 價格\n')
	for p in products: #for loop
		f.write(p[0] + ',' + str(p[1]) + '\n' )