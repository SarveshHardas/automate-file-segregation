import os
import shutil

from_dir="F:\SARVESHH\maths project\presentation"
to_dir="F:/game/Python/Project/class 102"

list_of_files=os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
    root,ext=os.path.splitext(i)
    #print(root)
    #print(ext)

    if ext=="":
        continue
    
    if ext in [".txt",".doc",".docx",".pdf",".pptx"]:
        path1=from_dir+"/"+i
        path2=to_dir+"/"+"Document_files"
        path3=to_dir+"/"+"Document_files"+"/"+i
        
        if(os.path.exists(path2)):
            print("Moving "+i)
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("Moving "+i)
            shutil.move(path1,path3)