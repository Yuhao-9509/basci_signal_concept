# Gradient
# We all know that we can calculate the rate of change of a function when the function is differentiable.The value of rate of change can calculated by \frac{f(x_0+\delta_x)-f(x_0)}{\delta_x}.
# Here are examples of how you can use the Greaient formula in Python.

# We use forword difference to cucalate the gradient.
def diff_gene(data_lens):
    ax = np.array([-1]+[0]*(data_lens-2)+[1]).reshape(-1,1)
    ay = np.array([-1]+[1]+[0]*(data_lens-2)).reshape(-1,1)
    D = toeplitz(ax,ay)


