# ModelEstimation

This script provides model estamation using [COMmon Bayesian Optimization Library (COMBO)](https://ma.issp.u-tokyo.ac.jp/en/app/1433) and HPhi.

In this script, the L=12 one-dimensional Heisenberg model with <a href="https://www.codecogs.com/eqnedit.php?latex=J_1=1.0,&space;J_2=0.5,&space;J_3=0.3" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J_1=1.0,&space;J_2=0.5,&space;J_3=0.3" title="J_1=1.0, J_2=0.5, J_3=0.3" /></a>,

<a href="https://www.codecogs.com/eqnedit.php?latex={\cal&space;H}&space;=&space;\sum_{i=1}^{12}J_1&space;{\bf&space;S}_i\cdot&space;{\bf&space;S}_{i&plus;1}&plus;J_2{\bf&space;S}_i\cdot{\bf&space;S}_{i&plus;2}&plus;J_3{\bf&space;S}_i\cdot{\bf&space;S}_{i&plus;3}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\cal&space;H}&space;=&space;\sum_{i=1}^{12}J_1&space;{\bf&space;S}_i\cdot&space;{\bf&space;S}_{i&plus;1}&plus;J_2{\bf&space;S}_i\cdot{\bf&space;S}_{i&plus;2}&plus;J_3{\bf&space;S}_i\cdot{\bf&space;S}_{i&plus;3}" title="{\cal H} = \sum_{i=1}^{12}J_1 {\bf S}_i\cdot {\bf S}_{i+1}+J_2{\bf S}_i\cdot{\bf S}_{i+2}+J_3{\bf S}_i\cdot{\bf S}_{i+3}" /></a>,

is estimated where
<a href="https://www.codecogs.com/eqnedit.php?latex=i=1=13" target="_blank"><img src="https://latex.codecogs.com/gif.latex?i=1=13" title="i=1=13" /></a>.

The search grids for (J_1, J_2, J_3) are defined in increments of 0.2 from 0 to 2, respectivery. The pair (J_1, J_2, J_3) is estimated by fitting magnetization curve using baysian optimization.



1. Install COMBO (Note: you must use python2)

    ``$ sh ./install_combo.sh ``

2. Link HPhi to current directory.

    ``$ ln -s Path_to_HPhi .``

3. Execute command

    ``$ python ./model_estimation.py ``

After finishing calculations, you can obtain exact pair (J_1, J_2, J_3) = (1.0, 0.5, 0.3).

# [memo] how to use hphi-modeling on sekirei

1. Use install scripts in sekirei folder.

2. Install combo by typing following command

    ``$ cd sekirei`` 
    
    ``$ sh install_combo.sh``

3. Move to ``tamura/hphi-modeling`` directory

   ``$ cd ../../tamura/hphi-modeling``

4. Uncomment line 31 in ``model_estimation.py``

    ``# hphi_cond["mpi_command"] = "mpijob"``
    -> ``hphi_cond["mpi_command"] = "mpijob"``

5. Use job script sample_hphi_sekirei.sh in sekirei folder.

   ``$ cp ../../script/sekirei/sample_hphi_sekirei.sh .``
   
   ``$ qsub sample_hphi_sekirei.sh``
   

Authour: Kazuyoshi Yoshimi (ISSP, Univ. of Tokyo), Date: 2019/10/12
