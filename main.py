import pygame as pg
import os
from pathlib import Path
source_path = Path(__file__).resolve() #promena directory-a na working directory
source_dir = source_path.parent
os.chdir(source_dir)
pg.init()
