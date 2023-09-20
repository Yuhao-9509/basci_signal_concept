# Gradient
# We all know that we can calculate the rate of change of a function when the function is differentiable.The value of rate of change can calculated by \frac{f(x_0+\delta_x)-f(x_0)}{\delta_x}.
# Here are examples of how you can use the Greaient formula in Python.

# We define a function to calculate the gradient using the forward difference method and consider periodic boundary conditions.
#------------------------------------------------------------------------
# Method 1: Using Toeplitz Matrix Multiplication
def Gra_fordiff_1(data):
    data_lens = len(data)
    # a0 and a1 are the zero axis and the first axis respectively
    a0 = np.array([-1]+[0]*(data_lens-2)+[1]).reshape(-1,1)
    a1 = np.array([-1]+[1]+[0]*(data_lens-2)).reshape(-1,1)
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
# We also can define a function to calculate the gradient using the center difference method and consider periodic boundary conditions.
def Gra_cendiff_1(data):
    data_lens = len(data)
    a0 = np.array([-2]+[1]+[0]*(data_lens-3)+[1])
    a1 = np.array([-2]+[1]+[0]*(data_lens-3)+[1]).reshape(-1,1)
    # Generate a toeplitz array
    D = toeplitz(a0,a1)
    Gra_dx = D.dot(data)
    return(Gra_dx)

def Gra_cendiff_2(data):
    data_lens = len(data)
    Gra_dx = [0]*data_lens
    for i in range(1,data_lens-1):
        Gra_dx[i] =  data[i-1] - 2*data[i]+data[i+1]
    Gra_dx[0] = data[data_lens-1]-2*data[0]+data[1]
    Gra_dx[data_lens-1] = data[data_lens-2]-2*data[data_lens-1]+data[0]
    return(Gra_dx)
#------------------------------------------------------------------------


