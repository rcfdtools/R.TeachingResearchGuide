# -*- coding: UTF-8 -*-
# Parabolic trajectory projectile motion - Markdown example
# https://github.com/rcfdtools

# Libraries
import math

# Variables
g = 9.806   # Gravity, m/s²
theta = 60  # θ, inclination angle, °
u = 9.43646034373488 # Initial projectile velocity, m/s
markdown_file = open('ParabolicSample.md','w+') # w+ create the file if it doesn't exist.
projectile_txt = 'Projectile refers to an object that is in flight after being thrown or projected. In a projectile motion, the only acceleration acting is in the vertical direction which is acceleration due to gravity (g). Equations of motion, therefore, can be applied separately in X-axis and Y-axis to find the unknown parameters.[^1]'

# Calculations
file_header = ('### Parabolic trajectory projectile motion - Markdown example\n\n'
               '%s\n\n#### Variables\n\n'
               '* g, gravity acceleration, m/s²: %f\n'
               '* theta, inclination angle, °: %f\n'
               '* u, initial projectile velocity, m/s: %f'
               '\n\n#### Results table' %(projectile_txt, g,theta,u)
              )
print(file_header)
markdown_file.write(file_header)
theta_rad = theta * math.pi / 180
table_header = '\n\n| x | y |\n'
print(table_header)
markdown_file.write(table_header)
table_row_sep = '|---|---|\n'
print(table_row_sep)
markdown_file.write(table_row_sep)
for x in range (0, 750, 50):
    y = x * math.tan(theta_rad) - (g / (2 * (u ** 2 * math.cos(theta_rad)) ** 2)) * x ** 2
    table_row = ('| %d | %f |\n' %(x,y))
    print(table_row)
    markdown_file.write(table_row)

markdown_file.write('\n[^1]: https://www.toppr.com/guides/physics/motion-in-a-plane/projectile-motion/')