

# IMAGE_SEQUENCE_RENAMER_v001.py

# The folowing module takes an image sequence and
# renames it to whatever the user inputs below.
# Instead of re-rendering the entire sequence,
# the module instead only takes a few seconds for it to implement
# the changes.


# HOW TO USE
# Follow the steps below and read of each of the comments.
# The only changes that need to be made by the user are found in
# STEPS 2, 3, 4 and 5 for the program to work.

# NOTES
# Ensure that the only the image sequence is in
# your specified directory and not files that fall outside
# the sequence.




################# STEP 1 ###############################################

# import the os module when dealing with files

import os

########################################################################




################# STEP 2 ###########################################################

# for the path, replace, 'place_path_here' with the filepath to the directory containing the
# image sequence (place the path within the quotation marks).

# as an example, your image sequence might be placed in a similar format to
# C:/my_project/shot_100/renders/my_project_comp/exr/
# where the folder, 'exr,' contains the image sequence,
# (in this case the image sequence is made up of exr files, but could also be png or jpegs etc.)
# Make sure that a backslash is at the the end of the file path.

path = "place_path_here"

# IMPORTANT - For Windows Users
# If planning on copying and pasting the filepath from Windows File Explorer
# or anything similar, Windows uses \ (back slashes) rather than
# / (forward slashes) in the path.
# Replace any \ with / after pasting, ensuring there is an / at the end of the path.

# NOTE - If using Linux or Mac then you do not need to replace the slashes.

####################################################################################






################# STEP 3 ###############################################

# for the prefix, replace, 'place_new_prefix_here,' with the
# new name of what you would like to rename the sequence to be,
# within the quotation marks.

# As an example, if your sequence starts  like this:
# my_comp_shot_100.1001.exr, my_comp_shot_100.1002.exr,...
# then your prefix is, my_comp_shot_100, which can be changed to
# a name of your choosing, such as, new_comp_shot_100.

new_prefix = "place_new_prefix_here"

#########################################################################





################# STEP 4 ###############################################

# for the start frame, replace, 'place_start_frame_here,' with the
# new frame start of your sequence,
# within the quotation marks.
# e.g. if you wanted your sequence to start from 1 rather than 1001
# than place 1 as the replacement.

start_frame = "place_start_frame_here"

########################################################################




################# STEP 5 ###############################################

# replace, 'place_file_extension_here,' with the
# file extension of your sequence
# within the quoatation marks.
# e.g. for an exr image sequence, it would be exr as the replacement
# for png files, it would be png as the replacement etc.

file_ext = "place_file_extension_here"

########################################################################





################# STEP 6 ###############################################

# stores a list of the files in the path in the variable [files].

# NOTE - it should not be necessary to make
# any adjustments to the lines of code below in order
# for the program to function

files = os.listdir(path)

########################################################################





################# STEP 7 ###############################################

# iterates over the files in the sequence
# and renames each one accordingly.

for i in range(len(files)):
    os.rename(path + files[i], f"{path}{new_prefix}.{i+int(start_frame)}.{file_ext}")

########################################################################

