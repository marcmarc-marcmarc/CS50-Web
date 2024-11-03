import zipfile
import os

with zipfile.ZipFile(f"wiki.zip", 'r') as zipref:
    zipref.extractall()