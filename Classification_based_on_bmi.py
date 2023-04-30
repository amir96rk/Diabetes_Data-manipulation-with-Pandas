def proportion_of_weight_range():
        import pandas as pd
        #load dataset
        df = pd.read_csv('diabetes_prediction_dataset.csv')

        #rename the columns of the dataset to lower case
        df = df.rename(lambda x : x.lower().strip(),axis=1)

        df_lenght = len(df) # outputs 100000

        #Selecting BMI groups with bit masking

        #If BMI is 18.5 to 24.9, it falls within the Healthy Weight range.
        healthy_weight = df[(df['bmi'] >= 18.5) & (df['bmi'] <= 24.9)]

        #If your BMI is 25.0 to 29.9, it falls within the overweight range. 
        over_weight = df[(df['bmi'] >= 25) & (df['bmi'] <= 29.9)]

        #If your BMI is 30.0 or higher, it falls within the obese range.
        obese = healthy_weight = df[(df['bmi'] >= 30)]
        
        output_dic = {"Total range " : df_lenght,
                    "Healthy Weight range":len(healthy_weight)/df_lenght, 
                    "Overweight range":len(over_weight)/df_lenght,
                    "Obese range":len(obese)/df_lenght}
        return output_dic

proportion_of_weight_range()