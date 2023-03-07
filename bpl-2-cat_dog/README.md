[<- Back to course](https://github.com/GrandEchoWhiskey/fcc-machine_learning-boilerplates/README.md)

<p align="center"><a href="https://www.freecodecamp.org/learn/machine-learning-with-python/">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/course/fcc100.png" /><br>
</a></p>
<h1 align="center">Machine Learning with Python<br><br>Cat Dog</h1>

<p align="center"><a href="#">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/programming/python.png" />
</a></p>

### Getting Started:
Export this directory using SVN.
```
svn export https://github.com/GrandEchoWhiskey/fcc-machine_learning-boilerplates/trunk/bpl-1-rock_paper_scissors
```
Open `ipynb` file with [Google Colab](https://colab.research.google.com)

```ipynb
try:
  # This command only in Colab.
  %tensorflow_version 2.x
except Exception:
  pass
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D, BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint

import os
import numpy as np
import matplotlib.pyplot as plt
```