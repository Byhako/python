..
.. Copyright (c) 2018 by Camilo-HG. All Rights Reserved.
..


.. _Sphinx: http://www.sphinx-doc.org/

Documenting with Sphinx - Examples
==================================

This repo was created in order to put on record the basic process for creating
a project with nicely documentation Sphinx_.

I follow some steps described in:

- `Documenting Your Project Using Sphinx <https://pythonhosted.org/an_example_pypi_project/sphinx.html>`_
- `Sam Nicholls brief guide <https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/>`_
- And the greatly `Tim Staley's mini-tutorial <https://github.com/timstaley/sphinx-example>`_

Instalation
===========

To install Sphinx_ using **conda** run::

  $ conda install -c anaconda sphinx

If you don't use **conda**, you can also try::

  $ easy_install sphinx

ReStructuredText
=================

In order to document using Sphinx_, you need to adopt any directive to write
documentation inside your code. This directive could be either **Markdown**
or **ReStructuredText**.

About **Markdown** (filename extensions: **.md**, **.markdown**):

- `Markdown Wikipedia <https://en.wikipedia.org/wiki/Markdown>`_
- `John Gruber's markdown tutorial <https://daringfireball.net/projects/markdown/syntax>`_
- `Daniel Greenfeld's markdown tutorial <http://markdown-guide.readthedocs.io/en/latest/>`_

About **ReStructuredText** (filename extension: **.rst**):

- `ReStructuredText Wikipedia <https://en.wikipedia.org/wiki/ReStructuredText>`_
- `ReStructuredText documentation <http://docutils.sourceforge.net/rst.html>`_
- `Quick ReStructuredText <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_
- `ReStructuredText cheatsheet <http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt>`_

Due to the fact that almost every example I found were written
using **ReStructuredText**, it's better to choose it for learning.

Documentation process
=====================

Every documentation example consists of a document where I recorded the step
by step process made and the files with the codes.

Hence, you can take a look to **Example_1-StepByStep.rst** in order to see the
process followed to produce **Example_1**.


http://www.sphinx-doc.org/en/stable/config.html