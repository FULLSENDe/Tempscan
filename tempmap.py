import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

T_min = 16.9  # минимальная температура
T_max = 22.3  # максимальная температура


img = cv2.imread('im2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

temp = T_min + (gray.astype(np.float32) / 255) * (T_max - T_min)


temp = np.round(temp, 1)


df = pd.DataFrame(temp)


df.to_excel('pixel_temperatures.xlsx', index=False, header=False)

df = pd.read_excel('pixel_temperatures.xlsx', header=None)

plt.imshow(df.values, cmap='jet')
plt.colorbar(label='Температура °C')
plt.title("Проверочная тепловая карта из Excel")
plt.show()
print("Файл pixel_temperatures.xlsx успешно создан.")