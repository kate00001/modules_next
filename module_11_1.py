from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

img = Image.open("9LOkvs-4PUg.jpg")
resized_img = img.resize((300, 300))
blurred_img = resized_img.filter(ImageFilter.BLUR)
blurred_img.save("example_processed.png")

print("Изображение обработано и сохранено.")

"""
Действительно, получилось,
даже по всем трем пунктам
"""


x = [8, 7, 6, 5, 4]
y = [0, 10, 30, 45, 65]

plt.plot(x, y, marker='o', linestyle=':', color='c', label="Моя тревожность")

plt.title("Иди уже спать")
plt.xlabel("Время сна")
plt.ylabel("Процент тревоги")
plt.legend()

plt.show()

"""
Все показал на симпатичном
бирюзовом графике, вопросов нет
"""