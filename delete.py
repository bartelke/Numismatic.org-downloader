import os
import re

#####################################################
# change this section
emperor = "Hadrian"
clean_only = False # if true, script will only remove trash photos
remove_obverse = False # if true, it will remove obverse side of the coins, 
                       # if false - reverse (valid only when clean_only is set to false)
#####################################################

folder_path = f'{emperor}_images'

# ending of the files containing other things than a coins (other website elements)
specific_endings = {'_0', '_40', '_41', '_42', '_43', '_44', '_45'}

# loop through each photo:
for filename in os.listdir(folder_path):
    # check if the picture is in .jpg format and if it is named as in download.py
    if filename.endswith('.jpg') and re.match(r'image_\d+_\d+\.jpg', filename):
        # get last digit to determine even/odd if needed
        last_digit = int(filename[-5])

        # check if last digit is even or odd
        if (last_digit % 2 == remove_obverse) and not clean_only:
            # remove file
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            continue  # skip to the next file after deleting

        # check if filename ends with one of the specific endings
        for ending in specific_endings:
            if filename.endswith(f"{ending}.jpg"):
                file_path = os.path.join(folder_path, filename)
                os.remove(file_path)
                break  # stop checking other endings if a match is found
