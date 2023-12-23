import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from io import BytesIO
import imageio

def optimized_funct_to_gif(j, step=0.1, gif_name='function_animation.gif', fps=1):
    def triangle_function(time):
        # Vectorized conditionals
        condition1 = (0 <= time) & (time < 0.5)
        condition2 = (0.5 <= time) & (time <= 1)
        return 2 * time * condition1 + 2 * (1 - time) * condition2

    times_ = np.arange(0, 1, step=step)
    images = []

    for k in tqdm(range(2**j)):
        time = (2**j) * times_ - k
        values = triangle_function(time)
        
        # Handle special case when n == 0
        n = 2**j + k
        if n == 0:
            values = time

        fig, ax = plt.subplots()  # Use subplots for better memory management
        ax.plot(times_, values, label=f'n={n}')
        ax.legend()

        # Save plot to a BytesIO object
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close(fig)  # Close the figure to free memory
        buf.seek(0)
        images.append(imageio.imread(buf))
        buf.close()

    # Create a GIF
    imageio.mimsave(gif_name, images, fps=fps)