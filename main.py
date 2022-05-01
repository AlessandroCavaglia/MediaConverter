import os
import subprocess


def getListOfFiles(dirName):
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

def getResolution(file):
    resolution = str(subprocess.Popen(
        "ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 \'" + file+"\'", shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0])
    resolution = resolution.replace("b", "")
    resolution = resolution.replace("\\n", "")
    resolution = resolution.replace("'", "")
    x=int(resolution.split("x")[0])
    y=int(resolution.split("x")[1])
    return (x,y)

def convertTo1080(file):
    conversionCommand = str(subprocess.Popen(
        "ffmpeg -i \'"+file+"\' -map 0 -c:v libx264 -crf 18 -vf format=yuv420p -c:a copy \'NEW_"+file+"\' -threads 10",
        shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0])
    print(conversionCommand)
    #removeCommand = str(subprocess.Popen(
    #    "rm \'"+file+"\'",
    #    shell=True,
    #    stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0])
    #moveCommand = str(subprocess.Popen(
    #    "mv \'NEW_" + file + "\' \'"+file+"\'",
    #    shell=True,
    #    stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0])

if __name__ == '__main__':
    files = getListOfFiles("series")
    for file in files:
        print(file)
        (resolutionX,resolutionY) = getResolution(file)
        print(str(resolutionX)+" "+str(resolutionY))
        if resolutionX>1920 and resolutionY>1080 and resolutionX%1920==0 and resolutionY%1080==0:
            print("Converting to 1920x1080:")
            #convertTo1080(file)
            print("Conversion ended")







