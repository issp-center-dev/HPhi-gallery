#!/bin/sh
#QSUB -queue i18cpu
#QSUB -node  16
#QSUB -mpi   64
#QSUB -omp   6
#QSUB -place pack
#QSUB -over false
#PBS -l walltime=00:30:00
#PBS -N HPhi
cd ${PBS_O_WORKDIR}
 #. /etc/profile.d/modules.sh
#module list > a
#module list

source /home/issp/materiapps/HPhi/HPhivars.sh 
date
 mpijob HPhi -s stan.in
date
