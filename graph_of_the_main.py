import matplotlib as pyplot
from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt
medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
urlretrieve(medical_charges_url,'medical.csv')
medical_df = pd.read_csv('medical.csv')
print(medical_df)
plt.rcparams['font size'] =14
plt.rcparams['figure.figsize'] = (10,6)
plt.rcparams['figure facecolour'] =00000000
fig =plt.hist(x=medical_df.age,bins=47)
plt.title('Distribution of age')
