# LED-7-Segment-Number-Display-Python-Essentials-2-Lab

A program which is able to simulate the work of a seven-display device, although we're going to use single LEDs instead of segments.

Each digit is constructed from 7 segments.

The segments can be constructed from different characters and they can be changed in the source code.
Personally, I think that the best is to have the horizontal segments (top, middle and bottom) as 3 dashes and the vertical segments as the pipe character.

This is an example for 1234567890:


        ---    ---           ---    ---    ---    ---    ---    ---   
    |      |      |  |   |  |      |          |  |   |  |   |  |   |  
        ---    ---    ---    ---    ---           ---    ---
    |  |          |      |      |  |   |      |  |   |      |  |   |  
        ---    ---           ---    ---           ---    ---    ---   

I defined the 7 LED segments (a,b,c,d,e,f,g) on/off state for each digit in a list
where 0 is a segment turned off and 1 is turned on.

The traditional order of the segments is going clockwise from the top
as it makes sense in a physical LED. Say the a,b,c,d,e,f,g segments would like so:
```
   a
 f   b
   g
 e   c
   d
```
However, the order I used is from the top to bottom and left to right
as it makes more sense for programming. Say a,b,c,d,e,f,g like so:
```
   a
 b   c
   d
 e   f
   g
```
As a result the digit state of the corresponding segments can be represented like so:
```
     abcdefg    # corresponding segments
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
```
The program creates an empty array/matrix of 5 rows and 3 columns for each digit and uses the digits state list to update the state for the segments based on the digit.
