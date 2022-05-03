# Python media converter

This project aims to solve a specific problem, i have legaly obtained files on my web server that i like to access
whit JellyFin, some files are 4K resolution and have some HVEC encoding that my ipad AIR can't seem to work with.
## Objectives

Create a script that looks for media files, check if resolution is greater than 1920x1080 and converts it in that resolution,
then checks for the format and if it is HVEC converts it   in a format that my i pad air can work with (H264). 
All the conversion is done with ffmpeg via command line so you don't have to install python libraries.
The project is ment to be run only on linux because it uses heavily the command line to simplify my work.
## Project Overview
ATM you can run the script and specify in the code the folder that you want to work with,
after that it looks for all files in a higher format than 1920x1080 and converts them in 1920x1080 creating a new file that starts with
NEW_{{Nameofthefile}} then deletes the old file and renames the new one to the old one
NEXT STEP : include media conversion from HVEC to H264
## License
[AGPL-3.0](https://choosealicense.com/licenses/agpl-3.0/)