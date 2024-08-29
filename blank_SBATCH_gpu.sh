#!/bin/bash -l
#SBATCH --job-name=script
#SBATCH --output=script.out
#SBATCH --partition=gpu_a100
#SBATCH --account=grdi_genarcc__gpu_a100
#SBATCH --time=2:00:00
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=2
#SBATCH --gpus-per-node=1
#SBATCH --comment="Submitted job"

