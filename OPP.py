import cv2
import numpy as np


#please change based on the pic. you want to select
image_path = r"C:/Users/Dhairya D/Downloads/Christ_Handing.jpg"

def detect_points(image):
  """
  This function attempts to detect potential points in a point-perspective painting.

  Args:
      image_path (str): Path to the image file.

  Returns:
      list: List of coordinates (x, y) for potential points.
  """
  

  # Apply image processing techniques like noise reduction and edge detection
  # (Replace these with your preferred techniques and parameters)
  # cv2.imshow('pic',image)
  image_blurred = cv2.GaussianBlur(image, (5, 5), 0)
  edges = cv2.Canny(image_blurred, 100, 150)
  
  # Find contours in the edge image
  contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  #print(contours)

  # Filter potential points based on size and circularity
  potential_points = []
  for contour in contours:
    area = cv2.contourArea(contour)
    #print(area)
    perimeter= cv2.arcLength(contour, True)
    print(perimeter)
    if perimeter < 1:
        perimeter = 20
    circularity = 4 * np.pi * area / (perimeter * perimeter)
    if 5 < area < 10  and 0.7 < circularity < 1.3000:  # Adjust thresholds as needed
      # Get the moments of the contour
      M = cv2.moments(contour)
      # Calculate the center of mass (centroid)
      cX = int(M["m10"] / M["m00"])
      cY = int(M["m01"] / M["m00"])
      potential_points.append((cX, cY))

  return potential_points

# Example usage
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#cv2.imshow('img', image)
points = detect_points(image)

# Display the image with detected points (uncomment if needed)
for point in points:
  cv2.circle(image, point, 5, (0, 0, 255), -1)
cv2.imshow("Image", image)
cv2.waitKey(0)

print("Potential points:", points)