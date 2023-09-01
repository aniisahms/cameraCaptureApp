import os
import cv2 #OpenCV
import time

def capture_image():
    # Inisialisasi objek kamera
    camera = cv2.VideoCapture(0)  # 0 menandakan kamera utama

    if not camera.isOpened():
        print("Kamera tidak dapat diakses")
        return

    # Baca frame dari kamera
    ret, frame = camera.read()

    if ret:
        # Direktori penyimpanan gambar
        save_directory = "capturedimg"

        # Pastikan direktori penyimpanan ada
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # Current timestamp
        timestamp = int(time.time())

        # Buat nama file unik dengan timestamp
        image_filename = os.path.join(save_directory, f"captured_image_{timestamp}.jpg")

        # Simpan gambar ke file
        cv2.imwrite(image_filename, frame)
        print(f"Gambar telah disimpan sebagai {image_filename}")

    else:
        print("Gagal membaca frame dari kamera")

    # Release kamera
    camera.release()

if __name__ == "__main__":
    capture_image()