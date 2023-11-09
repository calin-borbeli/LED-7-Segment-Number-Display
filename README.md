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
