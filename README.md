# File monitoring script for imagery processing
The program is aimed at automating the process of checking that all the imagery files (ERS, mapinfo, PNG,etc) associated with the tilenames contained in a textfile (provided to the user) are present in the zip folder (in specific directory where imagery files are uploaded). 

It makes extensive use of python lists, loops, file handling and error handling.

It logs the tilenames not found and number of files found for each of the tilenames in the zip folder.

