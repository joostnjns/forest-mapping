"""
Utilities used by example notebooks
"""
from typing import Any, Optional, Tuple
import numpy.typing as npt

import matplotlib.pyplot as plt
import numpy as np


def plot_image(
    image: npt.NDArray[np.int32], factor: float = 1.0, clip_range: Optional[Tuple[float, float]] = None, **kwargs: Any
) -> None:
    """Utility function for plotting RGB images."""
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
    if clip_range is not None:
        ax.imshow(np.clip(image * factor, *clip_range), **kwargs)
    else:
        ax.imshow(image * factor, **kwargs)
    ax.set_xticks([])
    ax.set_yticks([])
    
def get_stats_from_img(image:npt.NDArray[np.int32]) -> tuple[npt.NDArray[np.int32], npt.NDArray[np.int32]]:
    """
    Calculate minimal and maximal value from each band in the image.
    
    Args:
        image (nd.array): containing multiple bands, with the channel/band in the second axis
    Returns:
        Tuple (of nd.array): of minimal and maximal values
    """
    min_vals = np.min(image, axis=(0,1))
    max_vals = np.max(image, axis=(0,1))
    return min_vals, max_vals

def min_max_scaling(image: npt.NDArray[np.int32], min_values: npt.NDArray[np.int32], max_values: npt.NDArray[np.int32]) -> npt.NDArray[np.float32]:
    """
    Scale the image values to the range [0, 1] for each band using given minimum and maximum values.

    Args:
        image (NDArray[np.int32]): Multi-band image array of shape (height, width, num_bands).
        min_values (NDArray[np.int32]): Minimum values for each band, shape (num_bands,).
        max_values (NDArray[np.int32]): Maximum values for each band, shape (num_bands,).

    Returns:
        NDArray[np.float32]: Scaled image array with values in the range [0, 1].
    """
    # Ensure min and max values are not equal to avoid division by zero
    max_values[max_values == min_values] = min_values[max_values == min_values] + 1

    # Scale the image values for each band
    scaled_image = (image.astype(np.float32) - min_values) / (max_values - min_values)

    return scaled_image
