import os #operating system

products = []
#讀取檔案
if os.path.isfile('products.csv'): #檢查檔案存在與否
	print('yeah! 找到檔案了')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品, 價格' in line:
				continue
			name, price = line.strip().split(',') #按行處理資料&按行儲存
			products.append([name, price])
	print(products)
else:
	print('找不到檔案......')

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	p = []
	p.append(name)
	p.append(price)
	#可以寫成 p = [name, price] 就是#7-#9
	products.append(p) #大清單內的每個小清單, 切割成兩組資料
print(products)

#若print(products[0][0]) = 印出大清單第零格裡面的小清單的第零格儲存格印出來

#印出所有購買紀錄
for p in products:
	print(p) #印出清單中的每一個小東西
	print(p[0], '的價格', p[1]) #印出每一個小清單的第0格 & 第1格

#寫入檔案
with open('products.csv', 'w', encoding ='utf-8' ) as f: #寫入檔案!!!
	f.write('商品, 價格\n') #adding columns & rectify Grabled
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')