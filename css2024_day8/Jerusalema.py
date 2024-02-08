# Import packages and functions

import numpy as np
from scipy.stats import chi2_contingency

# Give the contingency table with observed counts			

ct = np.array([[28, 12], [16, 24]])

# Do the test for independence

chi2_contingency(ct)