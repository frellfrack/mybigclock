# mybigclock
This is a Python program for a graphical clock application that uses the Pygame library to create a graphical user interface. The clock is designed to display hours, minutes, and seconds using three rotating hands. The clock face consists of a background image, numerals, and tick marks.

The myBigClock class is the main class that controls the behavior of the clock. It takes an options dictionary as input, which contains various parameters for configuring the clock, such as its size, color, and font.

The __init__() method initializes Pygame, sets the screen size, and loads the background image. It also creates three clock hands as instances of the base_object class defined in the my_object module. The mainLoop() method runs a loop that updates the clock every second. The updateClock() method updates the clock hands' positions, draws them on the screen, and displays the numerals, tick marks, and labels. The drawDial() and drawNumerals() methods are used to draw the tick marks and numerals on the clock face, respectively. The drawLabel() method is used to display the motto and date on the clock face.

The program uses several Python modules, including pygame, math, time, datetime, and a custom my_object module that contains the base_object class.

