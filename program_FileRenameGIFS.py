## IMPORT MODULES
import os

## BEGIN DEFINE FUNCTION
def fn_RenameFilesByType(FileExtension, DirectoryTarget="images"):

    ## GET LOWERCASE FILE EXTENSION // STRIP DOT FROM LEFT SIDE OF FILE EXTENSION
    FileExtension = FileExtension.lower().lstrip('.')

    ## TEST PRINT OUTPUT
    print(f"FileExtension: {FileExtension}")
    
    ## GET ABSOLUTE PATH
    DirectoryTargetAbsolute = os.path.abspath(DirectoryTarget)

    ## GET LIST OF FILES IN TARGET DIRECTORY
    ListOfFileNames = [

        ## PART 1: ALL THIS IS ONE LIST COMPREHENSION STATEMENT...
        f for f in os.listdir(DirectoryTargetAbsolute)

        ## PART 2: ...YES, THIS TOO...
        if f.lower().endswith(f".{FileExtension}") and os.path.isfile(os.path.join(DirectoryTargetAbsolute, f))
    ]
    
    ## TEST PRINT OUTPUT
    print(f"ListOfFileNames: {ListOfFileNames}")

    ## SORT FILES
    ListOfFileNames.sort()

    ## TEST PRINT OUTPUT
    print(f"ListOfFileNames: {ListOfFileNames}")

    ## FIRST RENAME TO TEMPORARY FILE NAMES TO AVOID CONFLICTS
    TempFileMap = {}  ## Dictionary to map original -> temp name

    ## BEGIN TEMP RENAME LOOP
    for index, FileName in enumerate(ListOfFileNames):
        
        ## CREATE TEMPORARY FILE NAME
        TempFileName = f"__tempfile_{index}__.{FileExtension}"

        ## PATHS
        PathOld = os.path.join(DirectoryTargetAbsolute, FileName)
        PathTemp = os.path.join(DirectoryTargetAbsolute, TempFileName)

        ## RENAME TO TEMP
        os.rename(PathOld, PathTemp)

        ## SAVE MAPPING
        TempFileMap[TempFileName] = FileName

        ## TEST PRINT OUTPUT
        print(f"Temporarily Renamed: {FileName} -> {TempFileName}")

    ## RENAME FROM TEMP FILES TO FINAL SEQUENCE NAMES
    TempFilesSorted = sorted(TempFileMap.keys())

    ## BEGIN FINAL RENAME LOOP
    for i, TempFileName in enumerate(TempFilesSorted, start=1):

        ## CREATE FINAL FILE NAME
        FileNameNew = f"{i}.{FileExtension}"

        ## PATHS
        PathTemp = os.path.join(DirectoryTargetAbsolute, TempFileName)
        PathNew = os.path.join(DirectoryTargetAbsolute, FileNameNew)

        ## RENAME
        os.rename(PathTemp, PathNew)

        ## TEST PRINT OUTPUT
        print(f"Final Rename: {TempFileName} -> {FileNameNew}")

    ## TEST PRINT OUTPUT
    print(f"All .{FileExtension} files in '{DirectoryTarget}/' have been renamed.")

## END DEFINE FUNCTION

## BEGIN MAIN PROGRAM
if __name__ == "__main__":

    fn_RenameFilesByType("png")  ## gif, jpg, jpeg, png
