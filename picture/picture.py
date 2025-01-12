import cv2

def show_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    ret, frame = cap.read()
    if ret:
        cv2.imshow("picture.jpg", frame)

    cap.release()

if __name__ == '__main__':
    show_image()