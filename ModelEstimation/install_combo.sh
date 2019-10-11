#!/bin/bash
pip install cython --user
pip install six --user
pip install matplotlib --user
git clone https://github.com/tsudalab/combo.git
cd combo
python2 setup.py install --user
