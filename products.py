products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price)
	#可以寫成 p = [name, price] 就是#7-#9
	products.append(p) #大清單內的每個小清單, 切割成兩組資料
print(products)

#若print(products[0][0]) = 印出大清單第零格裡面的小清單的第零格儲存格印出來