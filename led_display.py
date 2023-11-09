# Define the 7 LED segments on/off state for each digit in a list
# where 0 is a segment turned off and 1 is turned on.

# The traditional order of the segments is going clockwise from the top
# as it makes sense in a physical LED. Say a,b,c,d,e,f,g like so:
#   a
# f   b
#   g
# e   c
#   d

# However, the order I use is from the top to bottom and left to right
# as it makes more sense for programming. Say a,b,c,d,e,f,g like so:
#   a
# b   c
#   d
# e   f
#   g

# As a result the digit state can be represented like so:
digit_state = [
    "1110111",  # 0
    "0010010",  # 1
    "1011101",  # 2
    "1011011",  # 3
    "0101010",  # 4
    "1101011",  # 5
    "1101111",  # 6
    "1010010",  # 7
    "1111111",  # 8
    "1111011",  # 9
]


# Define the funtion to display the digits:
def led_display(digits):
    # Run through each digit
    for digit in digits:
        print(digit)


# Request the user to enter the digits to be displayed and assign it to a variable:
digits = input("Enter digits to be displayed: ")

# Check that the user input contains only digits
while not digits.isdigit():
    print("Please enter only digits")
    digits = input("Enter digits to be displayed: ")
else:
    # Run the funtion to display the digits:
    led_display(digits)
