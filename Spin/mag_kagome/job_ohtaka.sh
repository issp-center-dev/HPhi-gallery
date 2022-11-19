#!/bin/bash
#SBATCH -J kagome
#SBATCH -p i8cpu
#SBATCH --time=00:30:00
#SBATCH -N 4
#SBATCH -n 128
#SBATCH -c 4
#SBATCH -o log.%j
#SBATCH -e log.%j

export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}
source /home/issp/materiapps/intel/hphi/hphivars.sh

MPI="srun "
HPhi="HPhi "

echo -n "[s] All  "
date 
for ((i=1;i<=27;i+=2)); do
cp -r org Sz$i
cd ./Sz$i
 echo "2Sz = $i " >> stan.in
 echo -n "  [s] Sz$i   "
 date
 ${MPI} ${HPhi} -s stan.in
 echo -n "  [e] Sz$i   "
 date
cd ..
done
echo -n "[e] All"
date
python3 mag.py
