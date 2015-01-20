# How do I use the command "ls"
$> man ls
# "man" is abbreviation for "manual" - this displays the user 
# manual for the command.
# or, for a quick reference we can use 
$> rmdir --help
# --help works for all commands.

# List all files in current directory
$> ls
README.md terminal

# List all files in current directory, with details
$> ls -l
total 8
-rw-r--r--  1 magnew  staff   37 Jan 19 10:01 README.md
drwxr-xr-x  3 magnew  staff  102 Jan 19 10:02 terminal

# Empty the terminal window
$> clear
# or easier, hit Ctrl-L

# Create a new empty file called "myfile.txt"
$> touch myfile.txt

# Delete the file "myfile.txt"
$> rm myfile.txt
# Note that this deletes the file for good

# Create a new directory called "kvittr"
$> mkdir "kvittr"

# Delete the directory named "kvittr"
$> rmdir kvittr
# Note! For safety reasons this is only allowed if the kvittr 
# directory is empty.

# Delete a directory which is not empty, but we want to delete anyway
$> rm -rf kvittr
# Note that you cannot undo this, so use with care!

# Search for the string "world" in all files in the current directory
$> grep world * 

# Search for the string "world" in all files in the current directory
# and show which line the string is found
$> grep -n world * 

# Search for the string "world" in all files in the current directory 
# and all subdirectories
$> grep -r world * 

# Combine the two above with:
$> grep -rn world * 




