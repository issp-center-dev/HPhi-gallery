Spectrum calculation for 12-site one-dimeinsional Heisenberg chain model.

The Hamiltonian is given by

<a href="https://www.codecogs.com/eqnedit.php?latex={\cal&space;H&space;}&space;=&space;J\sum_{i=0}^{11}&space;\hat{S}_i&space;\cdot&space;\hat{S}_{i&plus;1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\cal&space;H&space;}&space;=&space;J\sum_{i=0}^{11}&space;\hat{S}_i&space;\cdot&space;\hat{S}_{i&plus;1}" title="{\cal H } = J\sum_{i=0}^{11} \hat{S}_i \cdot \hat{S}_{i+1}" /></a> ,

where 

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{S}_0&space;=&space;\hat{S}_{12}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{S}_0&space;=&space;\hat{S}_{12}" title="\hat{S}_0 = \hat{S}_{12}" /></a> .

The spectrum function can be calculated by following  steps.

1. Calculate the ground state.
2. Define excitation operators in the ``pair.def`` file.
3. Calculate spectrum function.

See the manual for details. To simply do above steps, we prepare the script file ``spinchain_example.py``. In the following, we show the procedure to obtain the specrum function by using the script file.


1. Execute the script file (``spinchain_example.py``)


    ``` 
    $ python spinchain_example.py
    ```


2. Plot ``spectrum.dat`` by gnuplot.

	``` 
    $ gnuplot
    $ set yrange [0:5]
    $ set pm3d map
    $ splot "./spectrum.dat" using 1:2:3
    ```
    
    You can see the following figure.
![Figure](Figure.pdf "Spectrum function for S=1/2 Heisenberg model. Horizontal and vertical axises correspond to the index of wave vector and frequency, respectively.")
    

    
Authour: Kazuyoshi Yoshimi (ISSP, Univ. of Tokyo), Date: 2018/01/01
