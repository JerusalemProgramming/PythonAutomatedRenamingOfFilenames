## THIS PYTHON FILE NEEDS TO BE RUN WITHIN THE IMAGES FOLDER WITH JPG/JPEG IMAGES WHOSE
## ..FILENAMES NEED RENAMED TO NUMERICAL SEQUENCE (1.jpg, 2.jpg, 3.jpg, 4.jpg... etc.)

## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

import re, glob, os, pathlib

## BEGIN DEFINE FUNCTIONS
## BEGIN DEFINE FUNCTIONS
## BEGIN DEFINE FUNCTIONS

def fn_RenameFiles(files, pattern, replacement):

    ## DECLARE VARIABLES
    ## SET COUNTER FOR LATER USE
    i = 1

    ## BEGIN FOR LOOP
    ## BEGIN FOR LOOP
    ## BEGIN FOR LOOP
    
    ## FOR EACH PATHNAME IN 
    for pathname in glob.glob(files):

        ## PATHNAME
        #print("pathname =", pathname) ## TEST OUTPUT

        ## BASENAME
        basename = os.path.basename(pathname)
        #print("basename =", basename) ## TEST OUTPUT

        ## IF PATHNAME EQUALS BASENAME...
        if pathname == basename:

            ##...THEN TEST OUTPUT - THIS SHOULD ALWAYS PRINT TRUE
            print("pathname == basename:  TRUE")
            print("pathname string =", pathname) ## STRING FILENAME IN DIRECTORY
            print("basename string =", basename) ## STRING FILENAME IN DIRECTORY

        ## ELSE IF PATHNAME DOES NOT EQUAL BASENAME...
        else:

            ##...TEN TEST OUTPUT
            print("pathname == basename:  FALSE")
            print("pathname string =", pathname) ## STRING FILENAME IN DIRECTORY
            print("basename string =", basename) ## STRING FILENAME IN DIRECTORY

        ## CALCULATE NEW FILENAME WITH REGULAR EXPRESSIONS   
        NewFilename = re.sub(pattern, replacement, basename)

        ## TEST OUTPUT
        print("NewFilename =", NewFilename)
        

        ## IF NEWFILENAME DOES NOT EQUAL BASENAME...
        if NewFilename != basename:

            ##...THEN RENAME THE PATHNAME WITH NEWFILENAME
            os.rename(pathname, os.path.join(os.path.dirname(pathname), NewFilename))
            
        ## ELSE DOES THIS CONDTION EVER GET TRIGGERED?
        else:
            print("DOES THIS CONDITION EVER GET TRIGGERED?")


    ## END FOR LOOP
    ## END FOR LOOP
    ## END FOR LOOP

    ## TEST OUTPUT - LIST OF FILENAMES IN DIRECTORY
    print("glob.glob(files) =", glob.glob(files))
    

    ## BEGIN FOR LOOP
    ## BEGIN FOR LOOP
    ## BEGIN FOR LOOP

    ## FOR EACH FILE IN glob.glob(files)
    for each in glob.glob(files):

    ## FILE PATH TO DIRECTORY OF IMAGES
        ## FILE PATH OF CURRENT WORKING DIRECTORY WITH IMAGES = e.g. C:\RootFolder\images
        filepath = os.path.abspath('') ## = os.getcwd()
        
        ## TEST OUTPUT - FILE PATH OF CURRENT WORKING DIRECTORY
        print("FILE PATH OF CURRENT WORKING DIRECTORY =", filepath)

        ## RENAME FILES IN CWD; JOIN EMPTY STRING FILEPATH + STRING OF INTEGER OF CURRENT COUNTER + STRING OF .JPG 
        os.rename(os.path.join(filepath, each), os.path.join(filepath, str(i)+'.jpg'))

        ## INCREASE COUNTER
        i = i+1

    ## END FOR LOOP
    ## END FOR LOOP
    ## END FOR LOOP

    ## TEST OUTPUT - LIST OF FILENAMES IN DIRECTORY
    print("glob.glob(files) =", glob.glob(files))

    ## TEST OUTPUT - GAME OVER
    print("GAME OVER.  GO CHECK YOUR IMAGE FOLDER")
    
    
## END DEFINE FUNCTIONS
## END DEFINE FUNCTIONS
## END DEFINE FUNCTIONS

### BEGIN MAIN PROGRAM
### BEGIN MAIN PROGRAM
### BEGIN MAIN PROGRAM
    

## CALL FUNCTION        
fn_RenameFiles("*.jpg", r"^(.*)\.jpg$", r"new(\1).jpg")

### END MAIN PROGRAM
### END MAIN PROGRAM
### END MAIN PROGRAM
        
