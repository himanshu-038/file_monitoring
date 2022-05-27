#importing the required modules
import datetime
from zipfile import ZipFile
import os

#function to get a list of the tiles from the text file 
def getTiles(textfilename):
    f=open(textfilename)
    lines=f.readlines()                                     
    tiles=list()
    for x in lines:
        tiles.append(x.split()[0])                         
    
    tiles.pop(0)                                            
    f.close()
    return tiles

    
#function to get a list of the files in the zip folder
def getFiles(folder_path):
    zip=ZipFile(folder_path, "r") 
    files=zip.namelist()
    return files

#funtion to get the list of the tiles not present in the zip folder
def find(files, tiles):
    TilesNotFound=list()

    for tile in tiles:
        flag=False

        for file in files:
            if tile in file:
                flag=True
        
        if flag==False:
            TilesNotFound.append(tile)
    
    return TilesNotFound

#function to log into a textfile
def logit(tiles_nf,file_count,tiles):
    f=open("FilesNF_log.txt","a")                                                      #open FilesNF_log.txt in append mode
    d=datetime.datetime.now()                                                          #get the current date
    f.write("\n"+d.strftime("%c"))
    f.write("\ntext file used: "+textfile_path)
    f.write("\nfolder used: "+folder_path)
    f.write("\ntiles not found:\n")
    for t in tiles_nf:
        f.write(t+"\n")
    f.write("\nthe number of files found for each tilename as following:\n")
    for i in range(len(tiles)):
        f.write(tiles[i] + ": " + str(file_count[i]) + "\n")
    f.close()

#function to count the number of files found in the zip folder for each tile number in the text file
def fileCount(tiles, files):
    count=list()
    for tile in tiles:
        c=0
        for file in files:
            if tile in file:
                c+=1
        count.append(c)
    return count    



#folder_path="C:\\Users\himanhu.gupta\Desktop\Imagery_Automation\CWRS_VHR1_DUNL_6.zip"
#textfile_path="C:\\Users\himanhu.gupta\Desktop\Imagery_Automation\CWRS_VHR1_DUNL_meta_62_D0_latest45.txt"

while True:
    folder_path=input("please enter full path of the zip folder:")                #get full path of the zip folder from user
    #if not folder_path.endswith(".zip"):
        #folder_path=folder_path+".zip"
        #break
    if not os.path.isfile(folder_path):                                           #check if the folder exists
        print("The zip folder does not exist. Please check the filename entered and make sure to add the correct file extension")       
    else:
        break
 
while True:
    textfile_path=input("please enter the full path of the text file:")           #get full path of the text file from user
    #if not textfile_path.endswith(".txt"):
        #textfile_path=textfile_path+".txt"
        #break
    if not os.path.isfile(textfile_path):                              		  #check if the file exists
        print("The file does not exist. Please check the filename entered and make sure to add the correct file extension.")
    else:
        break

try:
    filelist=getFiles(folder_path)                                                #call get files function
    tilelist=getTiles(textfile_path)                                              #call get tiles function
    tiles_not_found=find(filelist,tilelist)                                       #call find function
    countlist=fileCount(tilelist,filelist)                                        #call fileCount function
    logit(tiles_not_found,countlist,tilelist)					  #call logit function

except:
    print("Oops!Something went wrong. Please check the file names entered and re run the program")       #if there is a problem with execution, throw error message

else:
    print("Program executed successfully! please check the log file")

input("press enter to exit")












