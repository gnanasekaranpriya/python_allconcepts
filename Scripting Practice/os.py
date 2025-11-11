import os
import shutil 

path = r'C:\Users\vgpsa\Python Projects\Data Analyst\Data Collection\Python Scripting'
print(os.listdir(path))

for filename in os.listdir(path): 
    filen, extension = os.path.splitext(filename)
    print(filen, extension)
    extension = extension[1:]
   
    if os.path.exists(path+'/'+extension): 
        shutil.move(path+'/'+filename, path+'/'+extension +'/'+filename)
    else: 
        os.makedirs(path + '/' + extension)
        shutil.move(path+'/'+filename, path+'/'+extension +'/'+filename)



