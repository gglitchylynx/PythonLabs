import cv2
import os


HAAR_CASCADE_PATH = 'haarcascade_plate_number.xml'

def task2_track_marker():
    if not os.path.exists(HAAR_CASCADE_PATH):
        print(f"Ошибка: Файл {HAAR_CASCADE_PATH} не найден!")
        return

    plate_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)
    min_area = 500

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Ошибка: Не удалось открыть камеру!")
        return

    print("Задание 2: Отслеживание метки")
    print("Нажмите 'q' для выхода")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        plates = plate_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in plates:
            area = w * h
            if area > min_area:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                center_x = x + w // 2
                center_y = y + h // 2
                cv2.circle(frame, (center_x, center_y), 5, (0, 255, 255), -1)

        cv2.imshow("Task 2 - Marker Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    task2_track_marker()