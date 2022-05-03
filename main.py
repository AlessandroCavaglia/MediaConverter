import os
import subprocess


def getListOfFiles(dirName):    #Function found on the web
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

#Function that uses the ffprobe console command to give the X and Y resolution
def getResolution(file):
    resolution = str(subprocess.Popen(
        "ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 \'" + file+"\'", shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0])
    if resolution=="" or "x" not in resolution:
        return(0,0)
    resolution = resolution.replace("b", "")
    resolution = resolution.replace("\\n", "")
    resolution = resolution.replace("'", "")
    x=int(resolution.split("x")[0])
    y=int(resolution.split("x")[1])
    return (x,y)

#Function that converts the file to 1920x1080 then removes the old file
def convertTo1080(file):
    splittedFile=file.split("/")
    splittedFile[-1]="NEW_"+splittedFile[-1]
    outputFile=""
    for part in splittedFile:
        outputFile=outputFile+part+"/"
    outputFile = outputFile[:-1]

    child = subprocess.Popen("ffmpeg -i '"+file+"' -vf scale=1920:1080 '"+outputFile+"' -threads 10",
        shell=True,
       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    streamdata = child.communicate()[0]
    rc = child.returncode
    if rc==0 or rc=='0' or rc=="0":
        (resolutionX, resolutionY) = getResolution(outputFile)
        print("New resolution: " + str(resolutionX) + " " + str(resolutionY))
        if resolutionX==1920 and resolutionY==1080:
            print("Removing file "+file)
            removeCommand = str(subprocess.Popen(
               "rm \'"+file+"\'",
                shell=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0])
            print("Renaming file "+outputFile+" to "+file)
            moveCommand = str(subprocess.Popen(
            "mv \'" + outputFile + "\' \'"+file+"\'",
            shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0])
        else:
            print("Wrong resolution of the new Output found, cleaning")
            print("Removing file " + file)
            removeCommand = str(subprocess.Popen(
                "rm \'" + outputFile + "\'",
                shell=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0])
    else:
        print("Error during conversion, cleaning")
        print("Removing file " + file)
        removeCommand = str(subprocess.Popen(
            "rm \'" + outputFile + "\'",
            shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0])

if __name__ == '__main__':
    files = getListOfFiles("series")
    for file in files:
        print(file)
        (resolutionX,resolutionY) = getResolution(file)
        print(str(resolutionX)+" "+str(resolutionY))
        if resolutionX>1920 and resolutionY>1080 and resolutionX%1920==0 and resolutionY%1080==0:
            print("Converting to 1920x1080:")
            convertTo1080(file)
            print("Conversion ended")


