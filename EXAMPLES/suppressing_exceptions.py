#!/usr/bin/env python
from contextlib import suppress
import os

FILE_NAME = 'wombat_dossier.txt'

with suppress(FileNotFoundError):  # <1>
    os.remove(FILE_NAME) # <2>
