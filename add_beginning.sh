#!/bin/bash
PATH=/bin:/usr/bin ; export PATH
umask 022

#Morgan Bakelmun

#Copying and pasting the SBATCH commands at the start of your script can be annoying,
#especially if you always use the same defaults. So instead, this script will
#add it in for you.

#Error handling to make sure there is only one argument
if [ "$#" -ne 1 ]; then
  echo "Error: This script requires exactly one argument."
  echo "Usage: $0 <argument>"
  exit 1
fi

#the first and only argument, the script name.
script_file=$1

#step 1, make sure that the argument is a valid script.
if [ ! -f "$script_file" ]; then
  echo "Error: File '$script_file' not found."
  exit 1
fi

if [[ "$script_file" != *.sh && "$script_file" != *.txt ]]; then
	echo "Invalid file extension. You can only add this to .sh and .txt files"
	exit 1
fi
#step 2, make an empty file for storing the new script.
temp_file=$(mktemp)

#step 3, if the SBATCH lines already exist, remove them first.
# Flag to indicate whether we are done skipping SBATCH lines
skip_done=false

while IFS= read -r line; do
  if ! $skip_done; then
    if [[ "$line" == *"SBATCH"* || "$line" == "#!/bin/"* ]]; then
      continue
    fi
    skip_done=true
  fi
  echo "$line" >> "$temp_file"
done < "$script_file"

info=$(cat $1)

#step 3, add SBATCH lines, then re-add the script.
{
	echo "#!/bin/bash -l"
	echo "#SBATCH --job-name=$(basename 'script_file')"
	#TODO: output is job-name + .out
	echo "#SBATCH --output=$(basename 'script_file').out"
	echo "#SBATCH --partition=standard"
	echo "#SBATCH --account=grdi_genarcc"
	echo "#SBATCH --time=12:00:00"
	echo "#SBATCH --ntasks=1"
	echo "#SBATCH --cpus-per-task=1"
	echo "#SBATCH --comment=\"Submitted job\"" # Probably should change the comment.
	echo
	cat "$temp_file"
} > "$script_file"

rm $temp_file

