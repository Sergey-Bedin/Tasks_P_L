import sys
import math

def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        center_line = file.readline().strip()
        radius_line = file.readline().strip()
        center = tuple(map(float, center_line.split()))
        radius = float(radius_line)
    return center, radius

def read_dots(file_path):
    with open(file_path, 'r') as file:
        dots = [tuple(map(float, line.strip().split())) for line in file]
    return dots

def dot_position(center, radius, dot):
    distance_squared = (dot[0] - center[0])**2 + (dot[1] - center[1])**2
    radius_squared = radius**2
    
    if math.isclose(distance_squared, radius_squared):
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2

def main():
    if len(sys.argv) != 3:
        print("Usage: python Task2.py circle.txt dot.txt")
        sys.exit(1)
    
    circle_file = sys.argv[1]
    dots_file = sys.argv[2]
    
    try:
        center, radius = read_circle_data(circle_file)
        dots = read_dots(dots_file)
        
        for dot in dots:
            position = dot_position(center, radius, dot)
            print(position)
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

