import cv2
from matplotlib import pyplot as plt

imagen = cv2.imread('7.jpg', cv2.IMREAD_GRAYSCALE)
if imagen is None:
    print("No se pudo cargar la imagen. Asegúrate de especificar una ruta válida.")
else:
    bordes = cv2.Canny(imagen, 100, 200)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(imagen, cmap='gray')
    plt.title("Imagen Original")
    plt.axis("off")
    
    plt.subplot(1, 2, 2)
    plt.imshow(bordes, cmap='gray')
    plt.title("Detección de Bordes")
    plt.axis("off")
    
    plt.show()
