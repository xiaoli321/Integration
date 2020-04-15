# Numerical Integration #

## Introduction ##
A class with various methods of computing numerical integrals.

Currently the avaiable methods are lower rectangle, composite trapzoid, Simpson's method, and Monte Carlo.

## Example ##

Computing integral of exp(x) on the interval [0,1] using Simpson's method.

```
>>>import numpy as np
>>>res = Integrate(np.exp, 0, 1, "simpson", n = 1000)
>>>res
1.71523140531859

```

Note the Integrate class and methods are all fully vectorized, thus the integrand must also be vectorized. 
