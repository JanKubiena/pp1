x = int(input("Podaj koordynat x: "))
y = int(input("Podaj koordynat y: "))

if x > 0 and y > 0:
    print(f"Point P({x}, {y}) is in 1st quadrant of the coordinate system")
elif x < 0 and y > 0:
    print(f"Point P({x}, {y}) is in 2nd quadrant of the coordinate system")
elif x > 0 and y < 0:
    print(f"Point P({x}, {y}) is in 3rd quadrant of the coordinate system")
elif x < 0 and y < 0:
     print(f"Point P({x}, {y}) is in 4th quadrant of the coordinate system")
else:
    print(f"Point P({x}, {y}) is in the middle quadrant of the coordinate system")