..
.. Copyright (c) 2018 by Camilo-HG. All Rights Reserved.
..


Example 1
=========

Let's start with the most simple example code. We will create a **"library"**
with two simple functions:

- **func_addition:** performs the addition of two numbers.
- **func_subtraction:** performs the subtraction of two numbers.

In addition, we create a script which **imports** the previous
functions for building a simple **calculator** (which obviously can only
perform the addition or the subtraction of two numbers).

Pre - Documentation process
---------------------------

First we need to creat directory for de project::

  $ mkdir Example_1

Next, inside ``/Example_1`` we need to create a directory which
will contain all doc files (the documentation directory)::

  $ mkdir docs

It is recommended to separate the codes in another directory::

  $ mkdir codes

To get started, ``cd`` into the documentation directory ``docs`` and type::

  $ sphinx-quickstart

It will launch the **Sphinx quickstart utility**. Next values are recommended::

  Welcome to the Sphinx 1.6.6 quickstart utility.

  Please enter values for the following settings (just press Enter to
  accept a default value, if one is given in brackets).

  Enter the root path for documentation.
  > Root path for the documentation [.]: <ENTER>
  (...)
  > Separate source and build directories (y/n) [n]: y
  (...)
  > Name prefix for templates and static dir [_]: <ENTER>
  (...)
  > Project name: ProjectName
  > Author name(s): AuthorName
  (...)
  > Project version []: ProjectVersion
  > Project release [0.0.1]: <ENTER>
  (...)
  > Project language [en]: <ENTER>
  (...)
  > Source file suffix [.rst]: <ENTER>
  (...)
  > Name of your master document (without suffix) [index]: <ENTER>
  (...)
  > Do you want to use the epub builder (y/n) [n]: <ENTER>

  Please indicate if you want to use one of the following Sphinx extensions:
  > autodoc: automatically insert docstrings from modules (y/n) [n]: y
  > doctest: automatically test code snippets in doctest blocks (y/n) [n]: <ENTER>
  > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
  > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: <ENTER>
  > coverage: checks for documentation coverage (y/n) [n]: <ENTER>
  > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: <ENTER>
  > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
  > ifconfig: conditional inclusion of content based on config values (y/n) [n]: y
  > viewcode: include links to the source code of documented Python objects (y/n) [n]: <ENTER>
  > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: <ENTER>

  A Makefile and a Windows command file can be generated for you so that you
  only have to run e.g. `make html' instead of invoking sphinx-build
  directly.
  > Create Makefile? (y/n) [y]: <ENTER>
  > Create Windows command file? (y/n) [y]: <ENTER>

  Creating file ./source/conf.py.
  Creating file ./source/index.rst.
  Creating file ./Makefile.
  Creating file ./make.bat.

  Finished: An initial directory structure has been created.

  You should now populate your master file ./source/index.rst and create other documentation
  source files. Use the Makefile to build the docs, like so:
     make builder
  where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

Then, the directory tree looks like::

  Example_1
  ├── codes
  └── docs
      ├── build
      ├── make.bat
      ├── Makefile
      └── source
          ├── conf.py
          ├── index.rst
          ├── _static
          └── _templates

  6 directories, 4 files

Note that the next ``Sphinx extensions`` were enabled:

- autodoc
- intersphinx
- mathjax
- ifconfig

And the current directory, ``/docs``, was enabled as *root path for the documentation*::

  > Root path for the documentation [.]: <ENTER>

Nevertheless, we also want to include the  ``/codes`` directory so the
codes will be documented too.
To ensure that ``sphinx-build`` can import your package and generate
the documentation correctly, simply uncomment this line near the top
of the **configuration file:** ``conf.py`` and add the *path* where
both ``/codes`` and ``/docs`` are located::

  # If extensions (or modules to document with autodoc) are in another directory,
  # add these directories to sys.path here. If the directory is relative to the
  # documentation root, use os.path.abspath to make it absolute, like shown here.
  #
  # import os
  # import sys
  # sys.path.insert(0, os.path.abspath('.'))

Afterwards, the modified lines will look like::

  # If extensions (or modules to document with autodoc) are in another directory,
  # add these directories to sys.path here. If the directory is relative to the
  # documentation root, use os.path.abspath to make it absolute, like shown here.
  #
  import os
  import sys
  #sys.path.insert(0, os.path.abspath('.'))
  sys.path.insert(0, os.path.abspath('../..'))

Another thing, is that our documentation must have a ``README.rst`` where we
briefly explain **what is the code for**, **installation**, **code requeriments**
(libraries required), **code execution example** and any other important information
needed to run the code.
This readme has to be located in the *root path for the documentation*
directory preferently::

  Example_1
  ├── README.rst
  ├── codes
  └── docs
      ├── build
      ├── make.bat
      ├── Makefile
      └── source
          ├── conf.py
          ├── index.rst
          ├── _static
          └── _templates


HTML configuration
------------------

Sphinx supports changing the appearance of its HTML output via `themes <http://www.sphinx-doc.org/es/stable/theming.html>`_. Take a look for a list of
builtin themes.

Default theme is **alabaster**, in ``conf.py``::

  # -- Options for HTML output ----------------------------------------------

  # The theme to use for HTML and HTML Help pages.  See the documentation for
  # a list of builtin themes.
  #
  html_theme = 'alabaster'

If you want to use another theme, change::

  html_theme = 'theme_name'

I'm using ``html_theme = 'nature'``. In addition, you must **disable** next
lines::

  # This is required for the alabaster theme
  # refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
  html_sidebars = {
      '**': [
          'relations.html',  # needs 'show_related': True theme option to display
          'searchbox.html',
      ]
  }

Now, if you explore `conf.py documentation<http://www.sphinx-doc.org/en/stable/config.html>`_
you'll find the different ways you can customize Sphinx behavior. In order to
change behavior, you must add some variables to ``conf.py``. I explore to change
HTML output adding next variables below ``# -- Options for HTMLHelp output``.

-  **add_module_names :** A boolean that decides whether module names are
prepended to all object names (for object types where a “module” of some
kind is defined), e.g. for py:function directives. Default = **True**.
- **html_show_sourcelink:** If true (and html_copy_source is true as well),
links to the reST sources will be added to the sidebar. Default = **True**.
- **html_logo:** If given, this must be the name of an image file
(path relative to the configuration directory) that is the logo of the docs.
It is placed at the top of the sidebar; its width should therefore not exceed
200 pixels. The image file will be copied to the ``_static`` directory of the
output HTML, but only if the file does not already exist there.
Default = **None**.

Next values were adopted::

  add_module_names = False
  html_show_sourcelink = False
  html_logo = chg-logo_small.png


.. Explicar lo que toca hacer con el readme

.. poner la directiva para comenzar las funciones y para terminarlas (explicar lo de |)

.. un simple enter no rompe la línea. Debe darse doble enter.
