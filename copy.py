# -*- coding: utf-8 -*-   
  
import os,shutil
  
def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.MOV':  
                L.append(os.path.join(root, file))
    return L 

def copy_search_file(srcDir, desDir):
    ls = os.listdir(srcDir)
    for line in ls:
        filePath = os.path.join(srcDir, line)
        if os.path.isfile(filePath):
            print(filePath)
            shutil.copy(filePath, desDir)

X=[]
src = 'C:\\Users\\Tappan\\Desktop\\photo\\Takeout\\Google Photos\\'
dest = 'D:\\pt'
X = file_name(src)
for i in X:
    print(i)
    shutil.copy(i,dest)

