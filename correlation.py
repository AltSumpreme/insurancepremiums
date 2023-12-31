import seaborn as sns
medical_df.corr()

'''
      age	       bmi	    children	 charges
age	1.000000	0.109272	0.042469	0.299008
bmi	0.109272	1.000000	0.012759	0.198341
children 0.042469	0.012759	1.000000	0.067998
charges0.299008	0.198341	0.067998	1.000000
  '''
sns.heatmap(medical_df.corr(), cmap='Reds', annot=True)
sns.title('Correlation Matrix')
