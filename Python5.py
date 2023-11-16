#iterate over folder to get the list of files in each folder
import os

def listOfFilesInFolder(folderpath):
    try:
        files=os.listdir(folderpath)
        return files,None
    except FileNotFoundError:
        return None,"Folder Not Found"
    except PermissionError:
        return None,"Permission Denied"
        

def main():
    folders=input("Please enter the list of folders separated with spaces ").split()
    for folder in folders:
        files,errorMessage = listOfFilesInFolder(folder)
        if files:
            print(files)
        else:
            print(f"Error in {folder}: {errorMessage}")

if __name__== "__main__":
    main()
    