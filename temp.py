import csv
from PIL import Image, ImageDraw #Подключим необходимые библиотеки. 

image = Image.open("temp.jpg") #Открываем изображение. (должен находится в папке с проектом)
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
width = image.size[0] #Определяем ширину. 
height = image.size[1] #Определяем высоту. 	
pix = image.load() #Выгружаем значения пикселей.
width1 = 1520 #с какого пикселя начнем отсчет
width2 = 1630 #каким закончим
height1 = height/2 # искомая линия
path = "output.csv"# название таблицы
    
for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			draw.point((i, j), (S, S, S))

image.save("chb.png", "JPEG")#чб изображение
del draw
newImage = image.crop((width1,height1,width2,height1+1))# Вырезаем нужную полоску
newImage.save("strip.png", "JPEG")

pix = newImage.load()
print()
print(newImage.size[0])#пишем в консоль сколько пикселей получилось

with open(path, "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    for i in range(newImage.size[0]):
        n = - pix[i, 0][2] + 256
        writer.writerow((n,))
