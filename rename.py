import os.path, time
from os import listdir
from os.path import isfile, join
from datetime import datetime
from os.path import getmtime


path = input("Enter Your Folder's Path: ")
extn = input("Enter The Extension of File with dot(.) : ")
allfiles = [f for f in listdir(path) if isfile(join(path, f))]
##print(allfiles)

for j in range(len(allfiles)):
    allfiles[j] = path + allfiles[j]

print('\n')
print(allfiles)

alltime = []

for x in range(len(allfiles)):
    ##print(time.ctime(os.path.getmtime(allfiles[x])))
    alltime.append(datetime.fromtimestamp(getmtime(allfiles[x])).strftime(' {%d~%m~%Y} {%I;%M %p}.MP4'))
    ##print(datetime.fromtimestamp(getmtime(allfiles[x])).strftime(' [%m-%d-%Y] (%I;%M %p).MP4'))



for k in range(len(allfiles)):

    alltime[k] = allfiles[k] + alltime[k]
    alltime[k] = alltime[k].replace(extn,'',1)
    alltime[k] = alltime[k].replace(".MP4","",1)

print(allfiles)
print(alltime)


for i in range(len(allfiles)):
    os.rename(allfiles[i], alltime[i])

print("Renamed Successfully....👍")
