# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:20:11 2024

@author: tjmah
"""

# Textbook - https://inferentialthinking.com/chapters/intro.html

import numpy as np
from scipy.stats import chi2_contingency

# Give the contingency table with observed counts			

ct = np.array([[122, 203], [167, 118], [258, 178], [673, 212]])

# Do the test for independence

chi2_contingency(ct)