"""
Feature highlights for Matplotlib 3.4.0.
"""

import numpy as np

from mplslide import FONT, TITLE_COLOUR, new_slide, slide_heading, annotate_pr_author


CODE = dict(fontfamily='monospace', fontsize=40, verticalalignment='top',
            alpha=0.7)


def example_plot(ax, fontsize=12, hide_labels=False):
    pc = ax.pcolormesh(np.random.randn(30, 30), vmin=-2.5, vmax=2.5)
    if not hide_labels:
        ax.set_xlabel('x-label', fontsize=fontsize)
        ax.set_ylabel('y-label', fontsize=fontsize)
        ax.set_title('Title', fontsize=fontsize)
    return pc


def subfigure():
    """
    Create slide for feature highlight of SubFigures.
    """

    real_fig = new_slide(constrained_layout=True)
    slide_heading(real_fig, '3.4 Feature: SubFigures')

    bottom, fig, top = real_fig.subfigures(3, 1, height_ratios=[1.5, 6, 1])
    bottom.set_facecolor('none')
    top.set_facecolor('none')

    subfigs = fig.subfigures(1, 2, wspace=0.07)

    subfigs[0].set_facecolor('coral')
    subfigs[0].suptitle('subfigs[0]')

    subfigs[1].set_facecolor('coral')
    subfigs[1].suptitle('subfigs[1]')

    subfigsnest = subfigs[0].subfigures(2, 1, height_ratios=[1, 1.4])
    subfigsnest[0].suptitle('subfigsnest[0]')
    subfigsnest[0].set_facecolor('r')
    axsnest0 = subfigsnest[0].subplots(1, 2, sharey=True)
    for ax in axsnest0:
        pc = example_plot(ax, hide_labels=True)
    subfigsnest[0].colorbar(pc, ax=axsnest0)

    subfigsnest[1].suptitle('subfigsnest[1]')
    subfigsnest[1].set_facecolor('g')
    axsnest1 = subfigsnest[1].subplots(3, 1, sharex=True)
    for ax in axsnest1:
        ax.plot(np.arange(10))

    axs_right = subfigs[1].subplots(2, 2)
    for ax in axs_right.flat:
        ax.plot(np.arange(10))

    annotate_pr_author(real_fig, 'jklymak', pr=18356)

    yield real_fig


def slides():
    """
    Return slides for this section.
    """
    return (
        *subfigure(),
    )
