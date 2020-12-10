"""
Demo slide.
"""

from mplslide import FONT, new_slide, slide_heading


def slides():
    """
    Create demo slide.
    """
    fig = new_slide()

    slide_heading(fig, 'Demos')

    props = dict(fontproperties=FONT, fontsize=56, alpha=0.7,
                 horizontalalignment='center')

    fig.text(0.5, 0.5, 'Animation, Widgets, and More',
             **props)

    return fig
