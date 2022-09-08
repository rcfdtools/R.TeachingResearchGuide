# -*- coding: UTF-8 -*-
# Parabolic trajectory projectile motion - Markdown sample
# https://github.com/rcfdtools

# Libraries
import math

# Variables
g = 9.806   # Gravity, m/s²
tetta = 60  # θ, inclination angle, °
u = 9.43646034373488 # Initial projectile velocity, m/s
markdown_file = open('ParabolicSample.md','w+') # w+ create the file if it doesn't exist.

# Calculations
file_header = ('### Parabolic trajectory projectile motion - Markdown sample\n\n'
      '* g, gravity acceleration, m/s²: %f\n'
      '* tetta, inclination angle, °: %f\n'
      '* u, initial projectile velocity, m/s: %f' %(g,tetta,u)
      )
print(file_header)
markdown_file.write(file_header)
tetta_rad = tetta * math.pi / 180
table_header = '\n\n| x | y |\n'
print(table_header)
markdown_file.write(table_header)
table_row_sep = '|---|---|\n'
print(table_row_sep)
markdown_file.write(table_row_sep)
for x in range (0, 750, 50):
    y = x * math.tan(tetta_rad) - (g / (2 * (u ** 2 * math.cos(tetta_rad)) ** 2)) * x ** 2
    table_row = ('| %d | %f |\n' %(x,y))
    print(table_row)
    markdown_file.write(table_row)


