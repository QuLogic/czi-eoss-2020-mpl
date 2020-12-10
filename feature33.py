"""
Feature highlights for Matplotlib 3.3.0.
"""

from mplslide import new_slide, slide_heading, annotate_pr_author


CODE = dict(fontfamily='monospace', fontsize=40, verticalalignment='top',
            alpha=0.7)


def identify_axes(ax_dict):
    """
    Mark Axes using their name passed to ``subplot_mosaic``.
    """
    kw = dict(ha='center', va='center', fontsize=48, color='darkgrey')
    for k, ax in ax_dict.items():
        ax.text(0.5, 0.5, k, transform=ax.transAxes, **kw)


def mosaic():
    """
    Create slide for feature highlight of subplot_mosaic.
    """

    example1 = """
    '''
    A.C
    BBB
    .D.
    '''"""
    example2 = """[
    ['.', 'histx'],
    ['histy', 'scat'],
]"""

    for text in [example1, example2]:
        fig = new_slide()

        slide_heading(fig, '3.3 Feature: subplot_mosaic')

        fig.text(0.05, 0.8, f'plt.figure().subplot_mosaic({text})', **CODE)

        ax_dict = fig.subplot_mosaic(eval(text.lstrip()),
                                     # Don't overlay title and code.
                                     gridspec_kw={'left': 0.3, 'top': 0.7,
                                                  'right': 0.97})
        identify_axes(ax_dict)

        annotate_pr_author(fig, 'tacaswell', pr=16603)

        yield fig


def slides():
    """
    Return slides for this section.
    """
    return (
        *mosaic(),
    )
