import os
import shutil
import glob
import zipfile
__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

path = os.getcwd()
print("The current working directory is: %s" % path)


def clean_cache():
    try:
        shutil.rmtree('cache')
    except:
        pass
    dir = ("cache")
    if 'cache' in dir:
        for file in glob.glob("cache/*.*"):
            os.remove(file)
    if not os.path.exists('cache'):
        os.makedirs('cache')
    # else:
        # return ('cache allready exists, it is empty, move forwards')
clean_cache()


def cache_zip(zip_path, cache_path):
    zip_path = "%s" % path
    cache_path = "%s" % path
    
    filename = "zip_path/data.zip"
    zip_obj = zipfile.ZipFile("data.zip", "r")
    zip_obj.extractall("cache")
    zip_obj.close()
print(cache_zip("files", "cache"))


def cached_files():
    directory = "%s" % path
    os.path.abspath(path)
    cached_path_files = [os.path.join(r'cache', file)
                         for file in os.listdir(r'cache')]
    cached_files = [file for file in cached_path_files if os.path.isfile(file)]
    return cached_files
print(cached_files())


def cached_files():
    new_list = []
    for file in os.listdir(os.path.abspath("cache")):
        new_list.append(f"{os.path.abspath('cache')}\{file}")
    return new_list


def find_password(list):
    search_str = "password:"
    for file_name in list:
        f = open(file_name, "r")
        if search_str in f.read():
            print(file_name)
find_password(cached_files())


def find_password(cached_files):
    directory = "%s" % path
    with open(r'cache/601.txt', 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if "password" in line:
                return line[10:38]
    return False
print(find_password(cached_files))


#if __name__ == '__main__':
      #print(cache_zip("files", "cache"))
      #print(cached_files())
