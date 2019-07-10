#!/bin/bash
#SBATCH --partition=rhel6-veryshort
#SBATCH --ntasks=1
#SBATCH --mem=15G
#SBATCH --job-name=Ani


export HOME=/atlas/users/mmunozsa/

source /cvmfs/dampe.cern.ch/rhel6-64/etc/setup.sh
source ~/astro/bin/activate

python add_maps.py  ${1} ${2} ${3} 
#python ani_rate_avg_2.py ${1} ${2} ${3} ${4}
