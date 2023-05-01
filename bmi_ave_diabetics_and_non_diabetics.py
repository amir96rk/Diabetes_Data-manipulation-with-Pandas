# In this function, we want to get the average bmi of the people with diabetes and without diabetes
def average_bmi_groups():
        import pandas as pd
        #load dataset
        df = pd.read_csv('diabetes_prediction_dataset.csv')

        #rename the columns of the dataset to lower case
        df = df.rename(lambda x : x.lower().strip(),axis=1)
        
        #select people with diabetes and without diabetes
        diabetics = df[df['diabetes'] == 1]
        non_diabetics = df[df['diabetes'] == 0]
        
        #get average bmi of the groups
        #fillna() is used to replace any possible missing values to 0
        dia_ave = diabetics['bmi'].fillna(0).mean()
        non_dia_ave = non_diabetics['bmi'].fillna(0).mean()
        
        
        output = 'Average BMI index of people with diabetes is {0:.4f} and without diabetes is {1:.4f}'.format(dia_ave,non_dia_ave)
        
        return output
        #returns : 'Average BMI index of people with diabetes is 31.9884 and without diabetes is 26.8872'
