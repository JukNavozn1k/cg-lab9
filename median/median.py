import numpy as np
from PIL import Image

def median_filter(image, kernel_size):
    # Convert the image to a numpy array
    image_array = np.array(image)

    # Create a padded version of the image array
    padded_image = np.pad(image_array, kernel_size, 'reflect')

    # Create an empty array to store the output image
    output_image = np.empty_like(image_array)

    # Iterate over the image array and apply the median filter
    for i in range(kernel_size, padded_image.shape[0] - kernel_size):
        for j in range(kernel_size, padded_image.shape[1] - kernel_size):
            # Extract the current kernel
            kernel = padded_image[i - kernel_size:i + kernel_size + 1, j - kernel_size:j + kernel_size + 1]

            # Get the median value of the kernel
            median = np.median(kernel)

            # Set the output pixel value to the median value
            output_image[i - kernel_size, j - kernel_size] = median

    # Convert the output image array back to an image and return it
    return Image.fromarray(output_image)

def load_image(filename):
    # Load the image from the file and return it
    return Image.open(filename)

def save_image(image, filename):
    # Save the image to the file
    image.save(filename)

# Load the image from a file
image = load_image('input.jpg')

# Apply the median filter to the image
filtered_image = median_filter(image, 3)

# Save the filtered image to a file
save_image(filtered_image, 'output.jpg')
