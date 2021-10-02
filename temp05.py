'''
this script will take a list of files from a directory filter is by value in the file name, 
sort the list by the and will delete some of the files from the directory....
'''
import glob, os, sys, re

# CommandLine = sys.argv[1]                                   # add working directory from command line
# print("Working Directory: ", CommandLine )

FolderPath  = "C:\\repository\\GeneralExamples\\WorkingFilesTime\\" 
NamePatternList = ["bin", "logs", "pdb", "src"]
FileExtension = ".zip"
FilePath01 = glob.glob(FolderPath + "*")
SortList = []
list01 = []
ToDelete = []

def FilePattern(Pattern):
    for x in FilePath01:
        if re.split('-', x)[4] == Pattern + FileExtension:      # find files from the NamePatternList list
            print("Found File: ", x)                            # print file after found bin in the name
            list01.append(x)                                    # appand the file to list01
            SortList.append(re.split('-', x)[3])                # appand only the 3 value after the "-" to the Sortlist
            SortList.sort()

for i in NamePatternList:
    print(FilePattern(i))

for i in SortList:
    FindValue = list(filter(lambda x: i in x, list01))          # check if file name in Sortlist is in list01
    ToDelete.append(FindValue)                                  # add value from FindValue it to ToDelete list
print("\nList Files to Delete :", ToDelete)                     # print ToDelete list for test

for u in ToDelete[16:99]:                                       # select all value but the first 4 valuse in the ToDelete list
    print(os.remove(u[0]))                                      # remove file in the list

print("files remain after delete: ", ToDelete)                  # print list after the delete process