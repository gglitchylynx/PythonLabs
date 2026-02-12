import cv2
import os


VARIANT = 10
IMAGE_PATH = f'images/variant-{VARIANT}.jpg'

def task1_threshold_filter():
    if not os.path.exists(IMAGE_PATH):
        print(f"Ошибка: Файл {IMAGE_PATH} не найден!")
    else:
        img = cv2.imread(IMAGE_PATH)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    threshold_value = 150
    max_value = 255
    ret, thresh = cv2.threshold(gray, threshold_value, max_value, cv2.THRESH_BINARY)
    
    cv2.imshow('Original Image', img)
    cv2.imshow(f'Threshold {threshold_value}', thresh)
    
    output_path = f'variant_{VARIANT}_threshold.jpg'
    cv2.imwrite(output_path, thresh)
    print(f"Изображение сохранено: {output_path}")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return thresh

if __name__ == "__main__":
    task1_threshold_filter()