import glob, os, time, sys, fnmatch, re

FolderPath  = "C:\\repository\\GeneralExamples\\WorkingFilesTime\\" 
NamePatternList = ["bin", "logs", "pdb", "src"]
FileExtension = ".zip"
FilePath01 = glob.glob(FolderPath + "*")
SortList = []
list01 = []
list02 = []
ToDelete = []


for x in FilePath01:
    if re.split('-', x)[4] == "bin" + FileExtension:
        print("Found File: ", x)
        list02.append(x)
        SortList.append(re.split('-', x)[3])
        for y in list01:
            if(y in SortList):
                SortList.append(y)
                
for u in SortList:
    list = any(u in string for string in list02)
    if list == True:
        ToDelete.append(x)   # add def to fix it
        # os.remove(u[2:99]

print("\n\nthis is ToDelete", ToDelete)



# for u in ToDelete:
    # os.remove(u[2:99])
    # print("\n----------------------------")
    # print("Files To Removing :", ToDelete[0:99])



