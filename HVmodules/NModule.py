# Modulos
import sys
import os
import os.path as op
import random
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QObject, Qt
from PySide2.QtWidgets import QFileDialog,QWidget,QTreeWidgetItem,QMdiSubWindow,QTextEdit,QVBoxLayout,QTabWidget
import PySide2.QtCharts
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.ticker import MultipleLocator
import matplotlib.gridspec as gridspec
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np
from math import floor
import datetime
import time
import copy
from scipy import signal
from scipy import interpolate
import platform



