# adocSplitScript

This repository contains a python script that splits one large adoc file into multiple files.

The splitting of the source file is based on the headings.

There are two scripts in the repository:

- **withoutHeader.py** -- The script creates files with no original headers, i.e., the resulting files contain no headers.
- **withHeader.py** -- It creates files that take into account the hierarchy of source file headers, i.e., the resulting files contain parent headers.
