Hubbard model (half-filling, Sz=0)

<a href="https://www.codecogs.com/eqnedit.php?latex={\cal&space;H}&space;=&space;-t&space;(c_{0\sigma}^{\dag}c_{1\sigma}&space;&plus;&space;{\rm&space;h.c.})&plus;U(n_{0\uparrow}n_{0\downarrow}&plus;n_{1\uparrow}n_{1\downarrow})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\cal&space;H}&space;=&space;-t&space;(c_{0\sigma}^{\dag}c_{1\sigma}&space;&plus;&space;{\rm&space;h.c.})&plus;U(n_{0\uparrow}n_{0\downarrow}&plus;n_{1\uparrow}n_{1\downarrow})" title="{\cal H} = -t (c_{0\sigma}^{\dag}c_{1\sigma} + {\rm h.c.})+U(n_{0\uparrow}n_{0\downarrow}+n_{1\uparrow}n_{1\downarrow})" /></a></a>


Check the eigenvalues become 

<a href="https://www.codecogs.com/eqnedit.php?latex=E=0,&space;U,&space;\frac{U}{2}(1\pm\sqrt{1&plus;(4t/U^2)})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E=0,&space;U,&space;\frac{U}{2}(1\pm\sqrt{1&plus;(4t/U^2)})" title="E=0, U, \frac{U}{2}(1\pm\sqrt{1+(4t/U^2)})" /></a>


1. Execute HPhi 


    ``` 
    $ HPhi -s stan.in
    ```


2. Check eigenvalues (output/Eigenvalue.dat)


    ```
     0 -0.8284271247
     1 0.0000000000
     2 4.0000000000
     3 4.8284271247
    ```
    
Authour: Kazuyoshi Yoshimi (ISSP, Univ. of Tokyo), Date: 2017/12/26
