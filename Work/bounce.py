# bounce.py
# A rubber ball is dropped from a height of 100 meters and each time it hits the ground, 
# it bounces back up to 3/5 the height it fell. 
# Write a program bounce.py that prints a table showing the height of the first 10 bounces.
# Exercise 1.5

height_start = 100.0;

for i in range(1,11):
    height_start = round(height_start *0.60,4);
    print(i,height_start);
    
