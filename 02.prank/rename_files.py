import os

def rename_files():
    #(1) get files names from a folder
    file_list = os.listdir(r"/home/leonardo/Work/udacity.com/programming-foundations-with-python/02.prank/prank/prank");
    saved_path = os.getcwd()
    print ("Current working directory is " + saved_path)
    os.chdir("/home/leonardo/Work/udacity.com/programming-foundations-with-python/02.prank/prank/prank");

    #(2) for each file, rename it
    for file in file_list:
        os.rename(file, file.translate(None, "0123456789"))

    os.chdir(saved_path);
    
    
rename_files()
