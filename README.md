# Baby-Vibes-Pytorch-Fastai-Raspberry-pi-4b

Pytorch Baby-moods Happy/Crying Image Classifier built using fastai, Python-flask, javascript, html, css, bootstrap and deployed on Raspberry Pi 4 

## Prerequisites

- Raspberry Pi 4
   - In order to check if the given wheel file (or any wheel file for Raspberry Pi for a specific Python package) is compatible with          your RPi’s processor architecture, type in the following:
   
      ``` uname -a ```
      
   - If you get the compatible version of processor architecture in terminal as armv7l, continue with the installation.
   
- Python 3.7

## Installation

``` 
python3 -m virtualenv env
source env/bin/activate 
```

### Install dependencies first:

```
sudo apt install libopenblas-dev libblas-dev m4 cmake cython python3-dev python3-yaml python3-setuptools python3-wheel python3-pillow python3-numpy 
```
Download [torch-1.3](https://wintics-opensource.s3.eu-west-3.amazonaws.com/torch-1.3.0a0%2Bdeadc27-cp37-cp37m-linux_armv7l.whl) and [torchvision-0.4](https://drive.google.com/uc?export=download&id=1nhk7PKDUzcmGGwnx7PK7iW3__2fOJVl1) wheel files.

### Install torch, torchvision and Fastai

```
pip3 install torch-1.3.0a0+deadc27-cp37-cp37m-linux_armv7l.whl
pip3 install torchvision-0.4.0a0+d31eafa-cp37-cp37m-linux_armv7l.whl
pip3 install fastai --no-deps 
```

It is possible that after installation when trying to import torch the following error may occur:

```
Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
   File "/usr/lib/python3.6/site-packages/torch/__init__.py", line 45, in <module>
     from torch._C import *
ModuleNotFoundError: No module named 'torch._C' 
```

Please refer [this](https://github.com/pytorch/pytorch/issues/574#issuecomment-278879701) for understanding the fix.

Your path may look like this if your are following along using the same project_folder and env variables:

```
$ cd pi/home/env/lib/python3.7/site-packages/torch
```

Inside this folder you will find two files with names like this:

```
_CXXXXXXXX.so
_dlXXXXXXXX.so
(XXXXXXX represents just any name)
```

Rename these files to below format:
```
_C.so
_dl.so
```
To test if everything was installed correctly, log into your python terminal and run the commands:

```
$ python3.7

>>> import torch
>>> import torchvision
>>> import fastai

```
Now you are ready to install project specific requirements - 

``` pip3 install requirements.txt ```



