#!/bin/bash -l
#SBATCH --job-name=script
#SBATCH --output=script.out
#SBATCH --partition=standard
#SBATCH --account=grdi_genarcc
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2000M
#SBATCH --comment="Submitted job"

