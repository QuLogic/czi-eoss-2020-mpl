Matplotlib Presentation for CZI EOSS 2020
=========================================

This repository contains code to create the presentation for the Matplotlib
presentation at the CZI EOSS Meeting 2020.

If you want to view the resulting PDF directly, you can [find a generated copy
in the release](https://github.com/QuLogic/czi-eoss-2020-mpl/releases).

Requirements
------------

* Python 3.7+
* NumPy
* Matplotlib >= 3.4.0
* A git checkout of the `matplotlib` source code, to produce the timeline.
* The Carlito font.

Optionally, you may also make available:

* The font to match the Matplotlib logo, Calibri.
* [`qpdf`](http://qpdf.sourceforge.net/), to linearize the final PDF.

Building
--------

The slides can be created by running:

```bash
$ ./make.py /path/to/matplotlib/checkout
```

which will produce `slides.pdf` directly from Matplotlib and
`czi-eoss-2020-mpl.pdf` as either a copy or a linearized version, depending on
whether `qpdf` is installed.

Overview
--------

Some general setup is contained in `mplslide.py`, namely setting slide size,
picking the font (Calibri and Carlito), and headings and other shortcut
functions. Other styling is mostly consistent, but usually set in the
individual files.

All slides are produced in the remaining Python files:

* `timeline.py`: A timeline of releases.
* `feature33.py`: Feature highlights for Matplotlib 3.3.0.
* `feature34.py`: Feature highlights for Matplotlib 3.4.0.
* `mine.py`: My work.
* `demo.py`: Demo slide page.
