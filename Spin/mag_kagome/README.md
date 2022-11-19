Magnetization process in the Heisenberg model on kagome lattice (27 site)

`job_ohtaka.sh` -> job script for supercomputer @ issp (system B, ohtaka)

&emsp;  submitting job: `sbatch ./job_ohtaka.sh`

&emsp;  checking elapsed time: `cat ./log.*** |grep JST`

&emsp;  pre-installed HPhi is used: `source /home/issp/materiapps/intel/hphi/hphivars.sh`

`mag.py` -> python script for calculating magnetization process

`mag.plt` -> visualization by gnuplot `load "mag.plt"`. The result is shown below.

![スクリーンショット 2022-11-19 13 10 02](https://user-images.githubusercontent.com/4827946/202835405-9d6fee25-94c1-4ac6-ae1e-2e0ad5f79583.png)


Authour: Takahiro Misawa (ISSP, Univ. of Tokyo), Date: 2018/6/16

**[Update]** Author: Takahiro Misawa (BAQIS), Date: 2022/11/19
