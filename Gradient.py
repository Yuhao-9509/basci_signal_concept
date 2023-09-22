# Gradient
# We all know that we can calculate the rate of change of a function when the function is differentiable.The value of rate of change can calculated by \frac{f(x_0+\delta_x)-f(x_0)}{\delta_x}.
# Here are examples of how you can use the Greaient formula in Python.

# We define a function to calculate the gradient using the forward difference method and consider periodic boundary conditions for 1D data.
# It's important to emphasize that 1D data has only one axis (axis 0), whereas 2D data has two axes (axis 0 and axis 1), and the behavior of the 0 axis in 2D data is distinct from that in 1D data.
#------------------------------------------------------------------------
# Method 1: Using Toeplitz Matrix Multiplication
def Gra_fordiff_1(data):
    data_lens = len(data)
    # a0 and a1 are the zero axis and the first axis respectively
    a0 = np.array([-1]+[0]*(data_lens-2)+[1])
    a1 = np.array([-1]+[1]+[0]*(data_lens-2))
    # Generate matrices for forward differences with periodic boundaries
    D = toeplitz(a0,a1)
    Gra_dx = D.dot(data)
    return(Gra_dx)

# Method 2: Using Loop Iteration
def Gra_fordiff_2(data):
    data_lens = len(data)
    Gra_dx = [0]*data_lens
    for i in range(data_lens-1):
        Gra_dx[i] =  data[i+1] - data[i]
    # Handle the periodic boundary condition
    Gra_dx[data_lens-1] = data[0]-data[data_lens-1]
    return(Gra_dx)

#------------------------------------------------------------------------
# We also can define a function to calculate the second order gradient.
def Sec_Gra_cendiff_1(data):
    data_lens = len(data)
    a0 = np.array([-2]+[1]+[0]*(data_lens-3)+[1])
    a1 = np.array([-2]+[1]+[0]*(data_lens-3)+[1]).reshape(-1,1)
    # Generate a toeplitz array
    Sec_D = toeplitz(a0,a1)
    Sec_Gra_dx = Sec_D.dot(data)
    return(Sec_Gra_dx)

def Sec_Gra_cendiff_2(data):
    data_lens = len(data)
    Gra_dx = [0]*data_lens
    for i in range(1,data_lens-1):
        Sec_Gra_dx[i] =  data[i-1] - 2*data[i]+data[i+1]
    Sec_Gra_dx[0] = data[data_lens-1]-2*data[0]+data[1]
    Sec_Gra_dx[data_lens-1] = data[data_lens-2]-2*data[data_lens-1]+data[0]
    return(Sec_Gra_dx)
#------------------------------------------------------------------------


# We define a function to calculate the gradient using the forward difference method and consider periodic boundary conditions for 2D data.
def Gra_fordiff_1(data_2d):
    Height , width = data_2d.shape
    
    # Generate matrices for forward differences with periodic boundaries in the x-direction
    a0 = np.array([-1]+[0]*(width-2)+[1])
    a1 = np.array([-1]+[1]+[0]*(width-2))
    D = toeplitz(a0,a1).T
    Gra_dx_2d = data_2d.dot(D)
    
    # Generate matrices for forward differences with periodic boundaries in the y-direction
    a0 = np.array([-1]+[0]*(Height-2)+[1])
    a1 = np.array([-1]+[1]+[0]*(Height-2))
    # Generate matrices for forward differences with periodic boundari
    D = toeplitz(a0,a1)
    Gra_dy_2d = D.dot(data_2d)
    return(Gra_dx_2d,Gra_dy_2d)


