# LED-7-Segment-Number-Display-Python-Essentials-2-Lab

A program which is able to simulate the work of a seven-display device, although we're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark) - like this example for 1234567890:


        ---    ---           ---    ---    ---    ---    ---    ---   
    |      |      |  |   |  |      |          |  |   |  |   |  |   |  
        ---    ---    ---    ---    ---           ---    ---
    |  |          |      |      |  |   |      |  |   |      |  |   |  
        ---    ---           ---    ---           ---    ---    ---   
