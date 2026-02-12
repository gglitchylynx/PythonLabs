import cv2
import numpy as np
from datetime import datetime


def video_processing():
    cap = cv2.VideoCapture(0)
    down_points = (640, 480)

    fly_img = cv2.imread("fly64.png", cv2.IMREAD_UNCHANGED)
    fly_w = fly_img.shape[1] // 2
    fly_h = fly_img.shape[0] // 2

    flip_counter = 0
    is_flipped = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        h, w = frame.shape[:2]

        x1, y1 = w // 2 - 75, h // 2 - 75
        x2, y2 = x1 + 150, y1 + 150
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(frame, "CENTER", (x1 + 40, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        marker_in_center = False

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            (x, y), r = cv2.minEnclosingCircle(c)
            x = int(x)
            y = int(y)
            r = int(r)

            if r > 20:
                cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
                cv2.circle(frame, (x, y), 3, (0, 255, 255), -1)
                cv2.putText(frame, f"({x}, {y})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                if x1 <= x <= x2 and y1 <= y <= y2:
                    marker_in_center = True

                xf = x - fly_w
                yf = y - fly_h
                if xf >= 0 and yf >= 0 and xf + fly_w * 2 < frame.shape[1] and yf + fly_h * 2 < frame.shape[0]:
                    if fly_img.shape[2] == 4:
                        alpha = fly_img[:, :, 3] / 255.0
                        for c in range(3):
                            frame[yf:yf + fly_h * 2, xf:xf + fly_w * 2, c] = (1 - alpha) * frame[yf:yf + fly_h * 2,
                                                                                           xf:xf + fly_w * 2,
                                                                                           c] + alpha * fly_img[:, :, c]

        if marker_in_center:
            if not is_flipped:
                is_flipped = True
                flip_counter += 1
                print(f"Переворот #{flip_counter} - {datetime.now().strftime('%H:%M:%S')}")
            frame = cv2.flip(frame, 1)
        else:
            is_flipped = False

        cv2.putText(frame, f"Flips: {flip_counter}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        cv2.putText(frame, f"Status: {'FLIPPED' if is_flipped else 'NORMAL'}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0, 255, 255) if is_flipped else (0, 255, 0), 2)

        cv2.imshow('Variant 10 - Flip on center + Fly', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Всего переворотов: {flip_counter}")


if __name__ == '__main__':
    video_processing()