#pip install pyit2fls
from pyit2fls import IT2FS, trapezoid_mf, tri_mf, gaussian_mf

from numpy import linspace
Trap_Set = IT2FS(linspace(0.,1.,100), trapezoid_mf, [0, 0.4, 0.6, 1., 1.])
Trap_Set.plot(filename="Trap_Set")
Tri_Set = IT2FS(linspace(0.,1.,100), tri_mf, [0, 0.6, 1., 1.])
Tri_Set.plot(filename="Tri_Set")
Gauss_Set = IT2FS(linspace(0., 1., 100), gaussian_mf, [0.5, 0.23, 1])
Gauss_Set.plot(filename="Gauss_Set")