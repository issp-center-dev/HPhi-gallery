#!/bin/sh
#QSUB -queue i18cpu
#QSUB -node  16
#QSUB -mpi   128
#QSUB -omp   3
#QSUB -place pack
#QSUB -over false
#PBS -l walltime=00:30:00
#PBS -N HPhi
cd ${PBS_O_WORKDIR}
source /home/issp/materiapps/HPhi/HPhivars.sh 
date
for ((i=1;i<=27;i+=2)); do
cp -r org Sz$i
cd ./Sz$i
 echo "2Sz = $i " >> stan.in
 mpijob HPhi -s stan.in
cd ..
done
date
python mag.py
