import glob, os, time, sys, fnmatch, re

FolderPath  = "C:\\repository\\GeneralExamples\\WorkingFilesTime\\" 
NamePatternList = ["bin", "logs", "pdb", "src"]
FileExtension = ".zip"
FilePath01 = glob.glob(FolderPath + "*")
SortList = []
list01 = []
ToDelete = []

for x in FilePath01:
    if re.split('-', x)[4] == "bin" + FileExtension:        # find files with bin in the name
        print("Found File: ", x)                            # print file after found bin in the name
        list01.append(x)                                    # appand the file to list01
        SortList.append(re.split('-', x)[3])                # appand only the 3 value after the "-" to the Sortlist
        SortList.sort()
        
for i in SortList:
    FindValue = list(filter(lambda x: i in x, list01))      # check if file name in Sortlist is in list01
    ToDelete.append(FindValue)                              # add value from FindValue it to todeletelist
print("\nList Files to Delete :", ToDelete)                 # print ToDelete list for test

for u in ToDelete:
    os.remove(u)
    print("\n----------------------------")
    print("Files To Removing :", ToDelete[0:99])

print("files remain after detele: ", ToDelete)

