#!/bin/sh
#QSUB -queue i18cpu
#QSUB -node  1
#QSUB -mpi   1 
#QSUB -omp   1
#QSUB -place pack
#QSUB -over false
#PBS -l walltime=00:10:00
#PBS -N HPhi
source /home/issp/materiapps/hphi/hphivars.sh
cd ${PBS_O_WORKDIR}
python model_estimation.py
