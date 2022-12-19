from PIL import Image
import numpy as np

def find_edges(image):
  # Convert the image to a grayscale array
  image_array = np.array(image.convert('L'))

  # Create an empty output array with the same dimensions as the input
  output_array = np.zeros_like(image_array)

  # Define the kernel for the Sobel operator
  kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
  kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

  # Loop over each pixel in the image
  for y in range(1, image_array.shape[0] - 1):
    for x in range(1, image_array.shape[1] - 1):
      # Apply the Sobel operator to the 3x3 neighborhood around the pixel
      gx = np.sum(kernel_x * image_array[y-1:y+2, x-1:x+2])
      gy = np.sum(kernel_y * image_array[y-1:y+2, x-1:x+2])

      # Calculate the gradient magnitude
      gradient = np.sqrt(gx**2 + gy**2)

      # Clip the gradient value to the range [0, 255]
      gradient = np.clip(gradient, 0, 255)

      # Set the output pixel value to the gradient magnitude
      output_array[y, x] = gradient

  # Convert the output array back to an image and return it
  return Image.fromarray(output_array)

# Test the function
image = Image.open('input.jpg')
edges = find_edges(image)
edges.save("output.jpg")
