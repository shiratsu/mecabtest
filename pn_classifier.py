#!/usr/bin/env python
#-*- coding:utf-8 -*-

### 使用するライブラリ
import MySQLdb
import pandas.io.sql as psql
import pandas as pd
import numpy as np
import MeCab
from sklearn import svm
from sklearn.grid_search import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
