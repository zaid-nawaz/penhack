import os 
import shutil

def find_files(filename, search_path):

    result = []

    for root , dir, files in os.walk(search_path):

        if filename in files:

            result.append(os.path.join(root,filename))

    return result

search_path_list = ['C:','D:','E:','F:','G:']
for i in range(5):

    fileaddress = find_files('conormaynard.txt',search_path_list[i])

    for i in range(len(fileaddress)):

        f = open(fileaddress[i],'r')

        shutil.copy(src=fileaddress[i],dst='I:/original'+fileaddress[i][0] + str(i) + '.txt')
        
        f.close()
