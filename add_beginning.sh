#!/bin/bash -l
PATH=/bin:/usr/bin ; export PATH
umask 022

#Morgan Bakelmun

#Copying and pasting the SBATCH commands at the start of your script can be annoying,
#especially if you always use the same defaults. So instead, this script will
#add it in for you.

#the first and only argument, the file name.
file=$1

#TODO: Error handling when there is no argument or more than one.

#step 1, make sure that the argument is a valid extension.
if [[ "$file" != *.sh && "$file" != *.txt ]]; then
	echo "Invalid file extension. You can only add this to .sh and .txt files"
	exit 1
fi
#TODO: verify that the SBATCH lines aren't already there. If they are, remove them.

#step 2, save everything that is already written in the script.
info=$(cat $1)

#step 3, add SBATCH lines. Note that this temporarily removes the file contents.

echo "#!/bin/bash -l" > $file
#TODO: job name is script name, excluding extension
echo "#SBATCH --job-name=" >> $file
#TODO: output is job-name + .out
echo "#SBATCH --output=" >> $file
echo "#SBATCH --partition=standard" >> $file
echo "#SBATCH --account=grdi_genarcc"  >> $file
echo "#SBATCH --time=12:00:00" >> $file
echo "#SBATCH --ntasks=1" >> $file
echo "#SBATCH --cpus-per-task=1" >> $file
echo "#SBATCH --comment=\"Submitted job\"" >> $file # Probably should change the comment.

#step 4, re-add the things written in the script.
echo -e "\n$info" >> $file
