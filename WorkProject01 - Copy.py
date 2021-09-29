# get list of file from a folder, filer by name. filter by time, keep only 4 last files and remove everything else

import glob, os, time, sys

FolderPath  = "C:\\repository\\Projects\\WorkingFiles\\"
NamePatternList = ["bin", "logs", "pdb", "src"]
FileExtension = "*.zip"

def DeleteFiles(NamePatternList):
    print("\nRemoving" + " " + NamePatternList + " " + "File: \n")
    FilterFiles = glob.glob(FolderPath + "*" + NamePatternList + FileExtension)
    FilterFiles.sort(key=os.path.getmtime)
    for file_name in FilterFiles[5:99]:
        file_path = os.path.join(FolderPath, file_name)
        print(file_name)
        os.remove(file_name)

for x in range(len(NamePatternList)):
    DeleteFiles(NamePatternList[x])
    print(NamePatternList[x])