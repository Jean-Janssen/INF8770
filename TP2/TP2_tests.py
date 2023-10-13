import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
import os
import glymur

# Load an image
image_originale = cv2.imread(r"/home/jeanjanssen/INF8770/INF8770/TP2/RGB.jpg")
test_image = cv2.imread(r"/home/jeanjanssen/INF8770/INF8770/TP2/RGB.jp2")
jp2_image_originale = glymur.Jp2k(r"/home/jeanjanssen/INF8770/INF8770/TP2/RGB.jp2")

# Compression JPEG
compression_quality = 90  # Adjust the quality value as needed
jpeg_filename = "image_compressed.jpg"
cv2.imwrite(jpeg_filename, image_originale, [int(cv2.IMWRITE_JPEG_QUALITY), compression_quality])


# Create a JP2 image with compression options
# compression_options = {'rate': 20}  # Adjust the rate for the desired compression level
jp2k_filename = "output_image.jp2"
compression_ratios  = [5.0]
compressed_image = glymur.Jp2k(jp2k_filename, data=jp2_image_originale, cratios=compression_ratios, colorspace='rgb')

# Calculate the PSNR (Peak Signal-to-Noise Ratio)
psnr_jpeg = psnr(image_originale, cv2.imread(jpeg_filename))
psnr_jpeg2000 = psnr(test_image, cv2.imread(jp2k_filename))

# Calculate the SSIM (Structural Similarity Index)
ssim_jpeg = ssim(image_originale, cv2.imread(jpeg_filename), win_size=3)
ssim_jpeg2000 = ssim(test_image, cv2.imread(jp2k_filename), win_size=3)

# Calculate file sizes and compression ratios
compression_ratio_jpeg =  os.path.getsize(r"/home/jeanjanssen/INF8770/INF8770/TP2/RGB.jpg")/os.path.getsize(jpeg_filename)
compression_ratio_jpeg2000 = os.path.getsize(r"/home/jeanjanssen/INF8770/INF8770/TP2/RGB.jp2")/os.path.getsize(jp2k_filename) 


# Display or print the results
print("PSNR JPEG:", psnr_jpeg)
print("PSNR JPEG2000:", psnr_jpeg2000)
print("SSIM JPEG:", ssim_jpeg)
print("SSIM JPEG2000:", ssim_jpeg2000)
print("Compression Ratio JPEG:", compression_ratio_jpeg)
print("Compression Ratio JPEG2000:", compression_ratio_jpeg2000)
