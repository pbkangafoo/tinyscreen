# tinyscreen
 
## What is tinyscreen?

tinyscreen is a lightweight clone of screenfetch written in python for displaying system information on the command line. you can use custom theme files to easily adjust on your needs.

## Which information can tinyscreen display?

In the current version, tinyscreen is able to display following information using replacements in the theme file:
..*username - §U§
..*hostname - §H§
..*uptime - §UP§
..*cpu - §CPU§
..*system release - §R§
..*machine - §M§
..*distribution - §D§

## How to install tinyscreen?

In order to use tinyscreen, you don't need special rights, user rights are enough. Just place the tinyscreen.py in your home directory and put the theme file - like the test.txt - in the same directory. Edit .bashrc and add at the bottom "python tinyscreen.py -i test.txt" to make it start, once you launch the console.

## Screenshot

![Screenshot](https://github.com/pbkangafoo/tinyscreen/blob/main/tinyscreeen_screenshot.jpg "tinyscreen screenshot")
