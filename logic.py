"""
Andrea Russo AR23110010747
T09 Practical Task 2

"""
import math

# A program to calculate the height of a building based on the shadow length and sun elevation angle

# Ask the user for the length of the shadow in meters
shadow_length = float(input("Enter the length of the shadow in meters: "))

# Ask the user for the sun elevation angle in degrees
sun_elevation_angle = float(input("Enter the sun elevation angle in degrees: "))


# Calculate the height of the building
# The logical error is in converting degrees to radians incorrectly
building_height = shadow_length * math.tan(sun_elevation_angle)

# Display the result
print(f"The height of the building is approximately {building_height} meters")
