#/bin/bash
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
done

#step 3, add SBATCH lines, then re-add the script.
echo "#!/bin/bash -l" >> $script_file
echo "#SBATCH --job-name=$(basename 'script_file')" >> $script_file
echo "#SBATCH --output=$(basename 'script_file').out" >> $script_file
echo "#SBATCH --partition=standard" >> $script_file
echo "#SBATCH --account=grdi_genarcc" >> $script_file
echo "#SBATCH --time=12:00:00" >> $script_file
echo "#SBATCH --ntasks=1" >> $script_file
echo "#SBATCH --cpus-per-task=1" >> $script_file
echo "#SBATCH --comment=\"Submitted job\"" >> $script_file # Probably should change the comment.
echo >> $script_file

cat $temp_file >> $script_file
rm $temp_file

echo "Default SBATCH lines added."
