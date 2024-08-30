def calculate_distance(x, y):

    return (x**2 + y**2) ** 0.5

x, y = 0, 0

movements = [
    ("UP", 5),
    ("DOWN", 3),
    ("LEFT", 3),
    ("RIGHT", 2)
]

for direction, steps in movements:
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

distance = calculate_distance(x, y)

rounded_distance = round(distance)

print(f"Final position: ({x}, {y})")
print(f"Distance from the origin: {rounded_distance}")
