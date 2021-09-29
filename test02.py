import glob, os, time, sys, argparse, fnmatch

FolderPath  = "C:\\repository\\Projects\\WorkingFiles\\"
NamePatternList = ["bin", "logs", "pdb", "src"]
FileExtension = "*.zip"

filtertest = glob.glob(FolderPath + "*" + "-" + "66*" + ".zip")

filtertime = sorted(fil)
print(filtertest)




def DeleteFiles(NamePatternList):
    print("\nRemoving" + " " + NamePatternList + " " + "File: \n")
    FilterFiles = glob.glob(FolderPath + "*" + NamePatternList + FileExtension)
    FilterFiles.sort(key=os.path.getmtime)
    for file_name in FilterFiles[5:99]:
        file_path = os.path.join(FolderPath, file_name)
        print(file_name)
