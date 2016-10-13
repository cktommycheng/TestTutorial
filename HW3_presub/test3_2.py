# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:08:59 2016

@author: Tshark
"""

import matplotlib.pyplot as plot
import pandas as pd
import numpy as np
import math
import gzip
import urllib.request
import os 

    
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/census-income-mld/census-income.data.gz"
ftpstream = urllib.request.urlopen(url)
census_cols = ['AAGE','ACLSWKR','ADTIND','ADTOCC','AGI','AHGA','AHRSPAY','AHSCOL','AMARITL','AMJIND','AMJOCC','ARACE',
               'AREORGN','ASEX','AUNMEM','AUNTYPE','AWKSTAT','CAPGAIN','CAPLOSS','DIVVAL','FEDTAX','FILESTAT','GRINREG',
               'GRINST','HHDFMX','HHDREL','MARSUPWT','MIGMTR1','MIGMTR3','MIGMTR4','MIGSAME','MIGSUN','NOEMP','PARENT',
               'PEARNVAL','PEFNTVTY','PEMNTVTY','PENATVTY','PRCITSHP','PTOTVAL','SEOTR','TAXINC','VETQVA','VETYN','WKSWORK']
with gzip.open(ftpstream) as KDD:
    census = pd.read_csv(KDD, names = census_cols)



ab_cols = ['Sex', 'Length', 'Diameter', 'Height', 'WholeWt', 'ShuckedWt', 'VisceraWt', 'ShellWt', 'Rings']
abalone = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data", names = ab_cols)
diamonds = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv', skiprows=1, names= ['carat', 'colour','clarity','certification', 'price'])
#KDD = pd.read_csv("KDD.txt")


diamonds_num = diamonds.ix[:,0]
abalone_num = abalone.ix[:,1]

#separate out the set of the numerical columns from the dataset diamonds
carats = diamonds.ix[:,0]
price = diamonds.ix[:,4]



#separate out the set of the numerical column from the dataset abalone
length = abalone.ix[:,1]
diameter = abalone.ix[:,2]
height = abalone.ix[:,3]
wholeWt = abalone.ix[:,4]
shuckedWt = abalone.ix[:,5]
visceraWt = abalone.ix[:,6]
shellWt = abalone.ix[:,7]
rings = abalone.ix[:,8]

#separate out the set of numerical columns from the dataset KDD
ages = KDD.ix[:,0]



#Freedman-Diaconis rule
def optbinwith(n, a, b, iqr):
    h = 2 * iqr * n**(-1/3)
    ran = a - b
    bins = ran / h
    return bins


def split_dist(data):
    summary = data.describe()
    q1 = summary['25%']
    q3 = summary['75%']
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    upper_outliers = data.where(data > upper_bound).dropna()
    lower_outliers = data.where(data < lower_bound).dropna()
    middle = data.where(data <= upper_bound).dropna()
    middle = middle.where(middle >= lower_bound).dropna()
    
    if lower_outliers.size !=0:
        lowerbins = optbinwith(lower_outliers.size, float(lower_outliers.max()), float(lower_outliers.min()), float(iqr))
        plot.figure()
        lower_outliers.plot.hist(bins= round(lowerbins)).set_title('Lowerbound outliers');
    if middle.size!= 0:
        midbins = optbinwith(float(middle.size), float(middle.max()), float(middle.min()), float(iqr))
        plot.figure()
        middle.plot.hist(bins= round(midbins)).set_title('Core distribution')
    if upper_outliers.size !=0 :
        upperbins = optbinwith(upper_outliers.size, float(upper_outliers.max()), float(upper_outliers.min()), float(iqr))
        plot.figure()
        upper_outliers.plot.hist(bins= round(upperbins)).set_title('Upperbound outliers')
    
    plot.figure()
    data.plot.box()
    





#split_dist(ages)
#split_dist(shellWt)
#print(shellWt)


