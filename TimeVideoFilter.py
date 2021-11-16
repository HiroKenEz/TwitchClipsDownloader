import os
import shutil
from moviepy.editor import *

def GetClipPath():
    duration = 0
    Tag = [] #not active now
    StreamerLink = [] #not active now
    StreamerName = [] #not active now
    PathDownloadClip = r'YOUR PATH' #path for the location of the downloaded files, NEEDS TO BE EMPTY
    PathBestOf = r'YOUR FINAL PATH' #path after the filter
    BestofTime = 601 #duration of the best of in seconde (600 for 10 minute)
    NbrBestOfFolder = os.listdir(PathBestOf) #get all the folder in the final path

    folder = len(NbrBestOfFolder) #get the number of files in the final path to be able to create new ones with the correct number
    path = PathBestOf + "\BestOf N' " + str(folder) #path for new folder

    for dirpath, dirnames, filesnames in os.walk(PathDownloadClip): #take all file in download path
        for file in filesnames: #for all file ....
            if not os.path.exists(path): #create the first folder if he dont existe
                os.makedirs(path)
            if os.path.join(dirpath, file) == r"YOUR PATH AND \desktop.ini": # if he take a desktop.ini he skip him
                pass
            else:
                duration += VideoFileClip(os.path.join(dirpath, file)).duration #add the clip time to the combined duration
                shutil.copy(os.path.join(dirpath, file), path) # copy the clip
            if duration > BestofTime:
                NbrBestOfFolder = os.listdir(PathBestOf) #get all the folder in the final path
                folder = len(NbrBestOfFolder) #get the number of files in the final path to be able to create new ones with the correct number
                path = PathBestOf + "\BestOf N' " + str(folder)  #path for new folder
                duration = 0 #reset
                if not os.path.exists(path): #create a new folder  "if no exists"
                    os.makedirs(path)
    if duration < BestofTime and duration != 0:
        print("you need", BestofTime - duration, "s for have 10min") #if you don't have enough clips it tells you how many minutes you need to do a complete best of



