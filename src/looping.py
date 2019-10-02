
colors = ['rEd', 'gReeN', 'bLUE', 'oRaNGe']

# for color in colors:
#     print_this = color.title()
#     print(f"The color we got was {print_this}")

# for num in range(1,11, 4):
#     result = num ** num
#     print(f"This result is {result}")


# for index, color in enumerate(colors):
#     print_this = color.title()
#     print(f"The color we got was {print_this} at position {index}")

hex_colors = {
    "Red": "#FF",
    "Green": "#008",
    "Blue": "#0000FF",
}

for index, color in hex_colors.items():
    val = hex_colors[index] # hex_colors.get(color)
    print(f"The value of this color is {index}, and the hex value is {color}")