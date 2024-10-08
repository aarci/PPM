# # This is our model
# # Data to Model : Position Vector of Centre of Mass (not at origin)
#                 : Moment of Inertia about Centre of Origin
#                 : Moment of Inertia about Centre of Mass (Parrellel Axis Theorem)
#                 : Potential Energy , Kinetic Energy

import numpy as np

R = 0.05    # Radius of disc
k = 0.086   # Weight of disc
m = 0.020   # Weight of particle
g = 9.81    # Gravitational constant
phi = input()

#Initial Conditions
O = np.array([0,0])     # Origin position vector
v_o = np.zeros(2)       # Origin initial velocity vector

Cm = np.array([(0), (m * R / 2*(k+m) )])    # Centre of mass position vector
v_cm = np

MI = ((k * R**2) / 4 ) * ( 2 + m / (k+m))   # Moment of Inertia about centre of mass
U = (- m * R * g * np.sin(phi)) / 2         # Potential Energy of System
T = # Kinetic Energy of System






