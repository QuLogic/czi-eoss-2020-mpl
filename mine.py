"""
Lesser-maintained parts
"""

import numpy as np
from matplotlib.image import imread

from mplslide import new_slide, slide_heading


CODE = dict(fontfamily='monospace', fontsize=40, verticalalignment='top',
            alpha=0.7)


def mine():
    """
    Create slide for my work.
    """

    fig = new_slide()
    slide_heading(fig, 'Lesser-maintained parts')

    theta = np.linspace(0, 2*np.pi)
    x = np.cos(theta - np.pi/2)
    y = np.sin(theta - np.pi/2)
    z = theta

    ax = fig.add_subplot(1, 2, 1, projection='3d')
    markerline, stemlines, baseline = ax.stem(
        x, y, z, linefmt='grey', markerfmt='D', bottom=np.pi)
    markerline.set_markerfacecolor('none')

    ax = fig.add_subplot(1, 2, 2)
    ax.axis('off')
    ax.imshow(imread('webagg.png'))

    yield fig


def slides():
    """
    Return slides for this section.
    """
    return (
        *mine(),
    )
