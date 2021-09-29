import glob, os, time, sys, fnmatch, re

FolderPath  = "C:\\repository\\Projects\\WorkingFilesTime\\"
NamePatternList = ["bin", "logs", "pdb", "src"]
FileExtension = ".zip"
FilePath01 = glob.glob(FolderPath + "*")
ToDelete = []

for x in FilePath01:
    if re.split('-', x)[4] == "bin" + FileExtension:
        print("Found File: ", x)
        # sorting = sorted(re.split('-', x)[2])
        list01 = sorted(ToDelete, key=lambda x: x.split("-")[2])
        ToDelete.append(x)
        print("\n\nprinting list", list01)

print("\n----------------------------")
print("Files To Removing :", ToDelete[2:99])




