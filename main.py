import cv2
import glob
import matplotlib.pyplot as plt
import math

# Load images from the directory
image_paths = sorted(glob.glob("images2/*"))

# Initialize list to store loaded images
image_list = []
for path in image_paths:
    image = cv2.imread(path)
    if image is None:
        print(f"Unable to load image: {path}")
        continue  # Skip images that couldn't be loaded
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_list.append(image_rgb)

# Count how many images were successfully loaded
image_count = len(image_list)

# Visualize the images if any were loaded
if image_count > 0:
    plt.figure(figsize=(30, 10))
    columns = 3
    rows = math.ceil(image_count / columns)
    
    for idx, image in enumerate(image_list):
        plt.subplot(rows, columns, idx + 1)
        plt.axis('off')
        plt.imshow(image)
    plt.show()
else:
    print("No images available for display.")

# Image stitching process (requires at least two images)
if image_count > 1:
    stitcher = cv2.Stitcher_create()
    stitch_status, stitched_image = stitcher.stitch(image_list)
    
    if stitch_status == cv2.Stitcher_OK:
        plt.figure(figsize=(30, 10))
        plt.imshow(stitched_image)
        plt.axis('off')
        plt.show()
    else:
        print("Image stitching process failed.")
else:
    print("At least two images are required for stitching.")
