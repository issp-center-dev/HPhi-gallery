Heisenberg dimer for general spin

<img src  <a href="https://www.codecogs.com/eqnedit.php?latex={\cal&space;H}&space;=&space;J&space;\hat{S}_{0}&space;\cdot&space;\hat{S}_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\cal&space;H}&space;=&space;J&space;\hat{S}_{0}&space;\cdot&space;\hat{S}_{1}" title="{\cal H} = J \hat{S}_{0} \cdot \hat{S}_{1}" /></a>


Change the value of ``2S`` in stan.in and check that the minimum and maximum eigenvalues become E\_{min} = -S(S+1) and E\_{max} =S^2.


1. Execute HPhi ( stan.in is the input file for S=1)


    ``` 
    $ HPhi -s stan.in
    ```


2. Check eigenvalues (output/Eigenvalue.dat)


    ```
 0 -2.0000000000
 1 -1.0000000000
 2 1.0000000000
    ```
    
    Authour: Kazuyoshi Yoshimi (ISSP, Univ. of Tokyo), Date: 2017/12/26
