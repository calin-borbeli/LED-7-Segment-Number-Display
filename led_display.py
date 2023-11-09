# Define the 7 LED segments on/off state for each digit in a list
# where 0 is a segment turned off and 1 is turned on.
# Each digit will be displayed on 5 rows

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
    global digit_state
    # Each digit will be displayed on 5 rows
    # Create a list of 5 empty rows
    rows = ["" for row in range(5)]
    # Run through each row of the 5 LED display rows
    for digit in digits:  # Run through each digit
        # Create an array of empty segments for each row
        segments = [[" ", "   ", " "] for row in range(5)]
        d = int(digit)
        # Check the digit state and update the segment state
        if digit_state[d][0] == "1":
            segments[0][1] = "---"
        if digit_state[d][1] == "1":
            segments[1][0] = "|"
        if digit_state[d][2] == "1":
            segments[1][2] = "|"
        if digit_state[d][3] == "1":
            segments[2][1] = "---"
        if digit_state[d][4] == "1":
            segments[3][0] = "|"
        if digit_state[d][5] == "1":
            segments[3][2] = "|"
        if digit_state[d][6] == "1":
            segments[4][1] = "---"
        # Join the segments for each individual row
        for row in range(5):
            rows[row] += "  " + "".join(segments[row])
    # Print individual rows
    for row in rows:
        print(row)


# Request the user to enter the digits to be displayed and assign it to a variable:
digits = input("Enter digits to be displayed: ")

# Check that the user input contains only digits
while not digits.isdigit():
    print("Please enter only digits")
    digits = input("Enter digits to be displayed: ")
else:
    # Run the funtion to display the digits:
    led_display(digits)
