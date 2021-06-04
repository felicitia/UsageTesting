#!/bin/bash
#
#SBATCH --job-name=v2s_signin
#SBATCH --output=signin_%j.txt  # output file
#SBATCH -e signin_%j.err        # File to which STDERR will be written
#SBATCH --partition=2080ti-long    # Partition to submit to 
#SBATCH --gres=gpu:1
#SBATCH --ntasks=1
#SBATCH --time=7-00:00:00         # Maximum runtime in D-HH:MM
#SBATCH --mem=48GB

exec_v2s --config="/mnt/nfs/work1/brun/yixuezhao/video2scenario/config_files/v2s_config_signin.json"