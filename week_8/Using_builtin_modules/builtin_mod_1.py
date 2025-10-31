import math
from datetime import datetime

sqrt_value = math.sqrt(4)
print(f"square root of 4: {sqrt_value}")

circle_area = math.pi * (5**2)
print(f"Area of circle with radius 5: {circle_area:.2f}")


now = datetime.now()
print(f"Current date and time: {now}")

formatted_date = now.strftime('%Y-%m-%d %H-%M-%S')
print(f"Formatted: {formatted_date}")