import os
import cv2
import numpy as np

# Define the data directory containing your original images
data_dir = "C:/Users/naren/OneDrive/Desktop/Telkom/Semester_7/PTA/Dataset/GRADE_2/HP_Biru_Ternate"

# Define the output directory for brightness-augmented images
brightness_dir = os.path.join(data_dir, "Brightness_Augmented")
os.makedirs(brightness_dir, exist_ok=True)

# Define the brightness factors (e.g., 0.5 for darker, 1.5 for brighter)
brightness_factors = [0.5, 0.8, 1.2, 1.5]

# Function to adjust brightness
def adjust_brightness(image, factor):
    # Convert to a floating-point array to avoid overflow
    img_float = image.astype(np.float32)

    # Scale the pixel values by the brightness factor
    bright_img = np.clip(img_float * factor, 0, 255).astype(np.uint8)

    return bright_img

# Loop through the original images
for filename in os.listdir(data_dir):
    # Skip non-image files
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue

    # Get the full image path
    image_path = os.path.join(data_dir, filename)

    # Load the image
    img = cv2.imread(image_path)

    # Apply each brightness factor
    for factor in brightness_factors:
        # Adjust the brightness
        bright_img = adjust_brightness(img, factor)

        # Get filename without extension
        base_filename, ext = os.path.splitext(filename)

        # Create the output filename with the brightness factor suffix
        output_filename = os.path.join(
            brightness_dir, f"{base_filename}_brightness_{factor:.1f}{ext}"
        )

        # Save the augmented image
        cv2.imwrite(output_filename, bright_img)

print("Brightness augmentation completed!")
