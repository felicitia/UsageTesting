#!/bin/bash
#
#SBATCH --job-name=v2s_search
#SBATCH --output=search_%j.txt  # output file
#SBATCH -e search_%j.err        # File to which STDERR will be written
#SBATCH --partition=titanx-long    # Partition to submit to 
#SBATCH --gres=gpu:1
#SBATCH --ntasks=1
#SBATCH --time=7-00:00:00         # Maximum runtime in D-HH:MM
#SBATCH --mem=64GB

exec_v2s --config="/mnt/nfs/work1/brun/yixuezhao/video2scenario/config_files/v2s_config_search.json"