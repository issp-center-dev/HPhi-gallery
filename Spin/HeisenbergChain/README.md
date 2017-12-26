16-site Heisenberg chain

<a href="https://www.codecogs.com/eqnedit.php?latex={\cal&space;H}&space;=&space;J&space;\sum_{i=0}^{15}&space;{\hat&space;S}_i&space;\cdot&space;{\hat&space;S}_{i&plus;1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\cal&space;H}&space;=&space;J&space;\sum_{i=0}^{15}&space;{\hat&space;S}_i&space;\cdot&space;{\hat&space;S}_{i&plus;1}" title="{\cal H} = J \sum_{i=0}^{15} {\hat S}_i \cdot {\hat S}_{i+1}" /></a>

where 

<a href="https://www.codecogs.com/eqnedit.php?latex={\hat&space;S}_{16}=&space;{\hat&space;S}_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\hat&space;S}_{16}=&space;{\hat&space;S}_{0}" title="{\hat S}_{16}= {\hat S}_{0}" /></a>


1. Execute HPhi ( stan.in is the input file for S=1)


    ``` 
    $ HPhi -s stan.in
    ```


2. Check eigenvalues (output/zvo_energy.dat)


    ```
Energy  -7.1422963606167773
Doublon  0.0000000000000000
Sz  0.0000000000000000
    ```
    
    Authour: Kazuyoshi Yoshimi (ISSP, Univ. of Tokyo), Date: 2017/12/26
