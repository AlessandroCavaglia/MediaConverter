# Python media converter

This project aims to solve a specific problem, i have legaly obtained files on my web server that i like to access
whit JellyFin, some files are 4K resolution and have some HEVC encoding that my ipad AIR can't seem to work with.
## Objectives

Create a script that looks for media files, check if resolution is greater than 1920x1080 and converts it in that resolution,
then checks for the format and if it is HEVC converts it   in a format that my i pad air can work with (H264). 
All the conversion is done with ffmpeg via command line so you don't have to install python libraries.
The project is ment to be run only on linux because it uses heavily the command line to simplify my work.
## Project Overview
This program is pretty simple, it searches all file in the folder and subfolder given, converts all 4K content to 1080
and all the HEVC to H624, then sleeps for X given seconds and tries again. That is used because if you add more
content it can automatically detect it and convert it to the chosen resolution.
## Execution
The execution is pretty simple, in the code you set the number of thread that you wanna use, the delay
and the folder that you wanna look inside (These are the first three constant) and you run it simply with
python, important you must have ffmpeg on your system.
I suggest to install this script on your linux machine as a service so it can run automatically
## License
[AGPL-3.0](https://choosealicense.com/licenses/agpl-3.0/)