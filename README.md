# File monitoring script for imagery processing
The program is aimed at automating the process of checking that all the imagery files (ERS, mapinfo, PNG,etc) associated with the tilenames contained in a textfile (provided to the user) are present in the zip folder (in specific directory where imagery files are uploaded).
It makes extensive use of python lists, loops, file handling and error handling.
It logs the tilenames not found and number of files found for each of the tilenames in a log file called FilesNF_log.txt. Everytime the program is run, the logs are appended in this file with information of date, textfile used and folder used.

Instructions on using the script:

1) Please enter full path of the zip folder
2) Please enter the full path of the text file
3) Program executed successfully! please check the log file

The program implements error handling for the cases when the folder path or text file path entered is not valid.

It throws the error:  
The zip folder does not exist. Please check the filename entered and make sure to add the correct file extension  
or  
The file does not exist. Please check the filename entered and make sure to add the correct file extension

In case there is some other issue with execution it throws the error:  
Oops!Something went wrong. Please check the file names entered and re run the program

