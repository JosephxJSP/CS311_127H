# 1650705682
# ณัฐนนท์ รุ่งพิรุณ

def cal_circle(radius):
    result = 3.14 * (radius * radius)
    return result

def cal_triangle(base, height):
    result = 0.5 * (base * height)
    return result

def cal_rectangle(width, length):
    result = width * length
    return result

isExits = False

while not isExits:
    print("\nC: Circle Area T: Triangle Area R: Rectangle Area E: Exit")
    input_menu = input("Enter menu : ")

    if input_menu.lower() == "c":
        input_radius = input("Enter radius : ")
        print("Circle area = ", cal_circle(int(input_radius)))
    elif input_menu.lower() == "t":
        input_base = input("Enter base : ")
        input_height = input("Enter height : ")
        print("Triangle area = ", cal_triangle(int(input_base), int(input_height)))
    elif input_menu.lower() == "r":
        input_width = input("Enter width : ")
        input_length = input("Enter length : ")
        print("Rectangle area = ", cal_rectangle(int(input_width), int(input_length)))
    elif input_menu.lower() == "e":
        print("Exit Program")
        isExits = True
    else:
        print("Invalid Menu Input!!!")