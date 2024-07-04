#!/bin/bash -l
#SBATCH --job-name=$(basename "script_file")
#SBATCH --output=$(basename "script_file").out
#SBATCH --partition=standard
#SBATCH --account=grdi_genarcc
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --comment=\"Submitted job\"

