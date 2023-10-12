import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
import os
import glymur

# Load an image
image_originale = cv2.imread(r"c:\Users\Jean Janssen\Desktop\keyssh\INF8770\TP2\RGB.jpg")
original_image = glymur.Jp2k(r"c:\Users\Jean Janssen\Desktop\keyssh\INF8770\TP2\RGB.jpg")

# Compression JPEG
jpeg_filename = "image_compressed.jpg"
_, jpeg_data = cv2.imencode(".jpg", image_originale, [cv2.IMWRITE_JPEG_QUALITY, 90])
with open(jpeg_filename, "wb") as f:
    f.write(jpeg_data)

# Create a JP2 image with compression options
compression_options = {'rate': 20}  # Adjust the rate for the desired compression level
compressed_image = glymur.Jp2k('jp2k_filename.jp2', data=original_image, **compression_options)

# Use Glymur to read the JPEG2000 image
image_jp2k = glymur.Jp2k(jp2k_filename)

# Calculate the PSNR (Peak Signal-to-Noise Ratio)
psnr_jpeg = psnr(image_originale, cv2.imread(jpeg_filename))
psnr_jpeg2000 = psnr(image_originale, cv2.imread(jp2k_filename))

# Calculate the SSIM (Structural Similarity Index)
ssim_jpeg = ssim(image_originale, cv2.imread(jpeg_filename), win_size=3)
ssim_jpeg2000 = ssim(image_originale, cv2.imread(jp2k_filename), win_size=3)

# Calculate file sizes and compression ratios
size_jpeg = os.path.getsize(jpeg_filename)
size_jpeg2000 = os.path.getsize(jp2k_filename)
compression_ratio_jpeg = os.path.getsize(r"c:\Users\Jean Janssen\Desktop\keyssh\INF8770\TP2\RGB.jpg") / size_jpeg
compression_ratio_jpeg2000 = os.path.getsize(r"c:\Users\Jean Janssen\Desktop\keyssh\INF8770\TP2\RGB.jpg") / size_jpeg2000

# Display or print the results
print("PSNR JPEG:", psnr_jpeg)
print("PSNR JPEG2000:", psnr_jpeg2000)
print("SSIM JPEG:", ssim_jpeg)
print("SSIM JPEG2000:", ssim_jpeg2000)
print("Compression Ratio JPEG:", compression_ratio_jpeg)
print("Compression Ratio JPEG2000:", compression_ratio_jpeg2000)
