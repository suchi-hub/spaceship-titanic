import kaggle
import os
import zipfile

print(os.path.abspath(__file__))
kaggle competitions download -c spaceship-titanic
os.chdir
with zipfile.ZipFile('sd') as zf:
    zf.extractall()
