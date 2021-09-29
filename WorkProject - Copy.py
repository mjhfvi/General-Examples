# get list of file from a folder, filer by name. filter by time, keep only 4 last files and remove everything else

import glob, os, time, sys

#VariableFromCMD = sys.argv[1]
FolderPath  = "C:\\repository\\Projects\\WorkingFilesTime\\"
NamePatternList = ["bin", "logs", "pdb", "src"]
FileExtension = "*.zip"

def DeleteFiles(NamePatternList):
    print("\nRemoving" + " " + NamePatternList + " " + "File: \n")
    FilterFiles = sorted(glob.glob(FolderPath + "*" + NamePatternList + FileExtension))
    #FilterFiles.sort(key=os.path.getmtime)
    for FileName in FilterFiles[5:99]:
        file_path = os.path.join(FolderPath, FileName)
        print(FileName)
        # os.remove(FileName)

for x in range(len(NamePatternList)):
    DeleteFiles(NamePatternList[x])
    print(NamePatternList[x])