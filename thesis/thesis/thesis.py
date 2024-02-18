# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:25:09 2024

@author: Deeksha
"""

import os
os.chdir('C:/thesis')

import pandas as pd

# read in the files.
norm_demographics = pd.read_csv('dwi_covariates.csv',
                                sep= ",",
                                index_col = 0)
norm_features = pd.read_csv('DWI_FA.csv',
                            sep=",",
                            index_col = 0)

# check columns through print [there are other better options]
print(norm_demographics)
print(norm_features)

# find overlap in terms of participants between norm_sample_features and
# norm_sample_demographics

norm_demographics_features = pd.concat([norm_demographics, norm_features],
                                       axis = 1,
                                       join = 'inner') # inner checks overlap
                                                       # outer combines
print(norm_demographics_features)

covariate_normsample = norm_demographics_features[['sex',
                                                   'age']]

covariate_normsample.to_csv('covariate_normsample.txt',
                            sep = ' ',
                            header = False,
                            index = False)

# perpare features_normsample for relevant hyppocampal subfields
features_normsample = norm__features[['ACR',
                                                 'ALIC',
                                                 'CGC',
                                                 'CGH']]

features_normsample.to_csv('features_normsample.txt',
                           sep = ' ',
                           header = False,
                           index = False)

print('hai')