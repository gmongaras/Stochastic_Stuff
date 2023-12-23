import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from io import BytesIO
import imageio

def optimized_funct_to_gif(n, step=0.001):
    # Triangle wavelet function
    def triangle_function(time):
        # Vectorized conditionals
        condition1 = (0 <= time) & (time < 0.5)
        condition2 = (0.5 <= time) & (time <= 1)
        return 2 * time * condition1 + 2 * (1 - time) * condition2

    # We only go from 0 to 1
    times_ = np.arange(0, 1, step=step)
    
    # Values start as all zeros
    values_total = np.zeros_like(times_)
        
    # n is defined by n = 2**j + k
    # Create a sequence of j and k values for this n
    j_vals = []
    k_vals = []
    cur_j = 0
    cur_k = 0
    for i in range(0, n+1):
        j_vals.append(cur_j)
        k_vals.append(cur_k)
        
        if 2**cur_j + cur_k == 2**(cur_j+1) - 1:
            cur_j += 1
            cur_k = 0
        else:  
            cur_k += 1
            
            
    # Iterate over the j and k values
    for j, k in zip(j_vals, k_vals):
        n = 2**j + k
        time = (2**j) * times_ - k
        values = triangle_function(time)
        
        # Handle special case when n == 0
        if n == 0:
            values = time
            
        # Scale the values
        values = values * (0.5 * (2**(-j/2)))
        
        # Scale by Gaussian random variable
        values = values * np.random.normal()
        
        # Add the values to the total
        values_total += values
    
        
        
    # Plot the total values
    fig, ax = plt.subplots()
    ax.plot(times_, values_total)
    plt.show()
    
    
optimized_funct_to_gif(2**10)