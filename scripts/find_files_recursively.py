import fnmatch
import os

PATH = './'
PATTERN = '*.py'

def get_file_names(filepath,pattern):
    matched = []
    if os.path.exists(filepath):
        for root,dirnames,filenames in os.walk(filepath):
            for filename in fnmatch.filter(filenames,pattern):
                matched.append(os.path.join(filename))
        if matched:
            print("found {} files:".format(len(matched)))
            output_files(matched)
        else:
            print("no files matched")
    else:
        print("sorry that path does not exist ")


def output_files(matched):
    for filename in matched:
        print(filename)

    
if __name__=='__main__':
    get_file_names(PATH,PATTERN)
    
