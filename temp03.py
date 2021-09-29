import glob, os, time, sys, fnmatch, re

FolderPath  = "C:\\repository\\Projects\\WorkingFilesTime\\"
NamePatternList = ["bin", "logs", "pdb", "src"]
FileExtension = ".zip"
FilePath01 = glob.glob(FolderPath + "*")
ToDelete = []

def FilterFiles(Pattern):
    for x in FilePath01:
        if re.split('-', x)[2] == Pattern + FileExtension:
            print("this is a bin file:", x)
            ToDelete.append(x)
print("\n----------------------------")
print("Files To Removing :", ToDelete)

for y in FilterFiles:
    if y == 
#     FilterFiles(bin)
#     print(y)

