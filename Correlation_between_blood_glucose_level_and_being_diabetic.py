def corr_dia_glucose():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    
    df = pd.read_csv('diabetes_prediction_dataset.csv')
    
    # For droping NaN parametrs of both column from whole dataframe
    df = df[~df["blood_glucose_level"].isna() & ~df["diabetes"].isna()]
    
    # get corrolation and p_value 
    corr, pval=stats.pearsonr(df["blood_glucose_level"], df["diabetes"])
    
    return 'Corrolation between Blood glucose level and Being Diabetic is {0:.4f} and P_value is {1:.4f}'.format(corr,pval)
  
  #returns 'Corrolation between Blood glucose level and Being Diabetic is  0.4196 and P_value is 0.0000'
  #So there is a Positive MeaningFul relation between High Blood glucose level and Being Diabetic.
