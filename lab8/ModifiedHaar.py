import cv2
import os
from datetime import datetime


HAAR_CASCADE_PATH = 'haarcascade_plate_number.xml'

def create_centered_rectangle(frame):
    h, w = frame.shape[:2]
    center_x, center_y = w // 2, h // 2
    rect_size = 150
    
    x1 = center_x - rect_size // 2
    y1 = center_y - rect_size // 2
    x2 = x1 + rect_size
    y2 = y1 + rect_size
    
    return x1, y1, x2, y2

def flip_frame(frame):
    return cv2.flip(frame, 1)

def task3_track_with_flip():
    if not os.path.exists(HAAR_CASCADE_PATH):
        print(f"Ошибка: Файл {HAAR_CASCADE_PATH} не найден!")
        return

    plate_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)
    min_area = 500

    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Ошибка: Не удалось открыть камеру!")
        return
    
    flip_counter = 0
    is_flipped = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        x1, y1, x2, y2 = create_centered_rectangle(frame)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(frame, "Center Area 150x150", (x1, y1-10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        plates = plate_cascade.detectMultiScale(gray, 1.1, 4)
        
        marker_in_center = False

        for (x, y, w, h) in plates:
            area = w * h
            if area > min_area:
                center_x = x + w // 2
                center_y = y + h // 2

                if (x1 <= center_x <= x2) and (y1 <= center_y <= y2):
                    marker_in_center = True
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                else:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                cv2.circle(frame, (center_x, center_y), 5, (0, 255, 255), -1)

                cv2.putText(frame, f"({center_x}, {center_y})", 
                          (center_x + 10, center_y - 10), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        if marker_in_center:
            if not is_flipped:
                is_flipped = True
                flip_counter += 1
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Метка в центре! Переворот #{flip_counter}")

            frame = flip_frame(frame)
        else:
            is_flipped = False

        cv2.putText(frame, f"Flip counter: {flip_counter}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        cv2.putText(frame, f"Status: {'FLIPPED' if is_flipped else 'NORMAL'}", (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, 
                   (0, 255, 255) if is_flipped else (0, 255, 0), 2)
        
        cv2.imshow("Task 3 - Variant 10: Flip on center", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    print(f"\nПрограмма завершена. Всего переворотов: {flip_counter}")
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    task3_track_with_flip()