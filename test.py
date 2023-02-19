import pandas as pd

df = pd.read_csv('DemographicPy/adult.data.csv')

raza = pd.Series(df['race'].value_counts());
#print(raza)

mean_xy = df.loc[df['sex'] == 'Male','age'].mean();
average_age_men_test = round(mean_xy,1)

