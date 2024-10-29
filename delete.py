import os
import re


#####################################################
# change this section
emperor="Hadrian"
remove_obverse = False
#####################################################

folder_path = f'{emperor}_images'

# loop through each photo:
for filename in os.listdir(folder_path):
    # check, if the picture is in .jpg format and if it is named as in download.py
    if filename.endswith('.jpg') and re.match(r'image_\d+_\d+\.jpg', filename):
        # get last digit
        last_digit = int(filename[-5])
        
        # check if last digit is even or odd
        if last_digit % 2 == remove_obverse:
            # remove file
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
