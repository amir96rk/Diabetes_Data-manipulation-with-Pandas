# In this File, we want to get the ratio between Diabetic Smokers (current and former) and Diabetic non-Smokers in men and women.
def ratio_diabetic_smokers_non_smokers():
    import pandas as pd
    #load dataset
    df = pd.read_csv('diabetes_prediction_dataset.csv')
    
    #rename the columns of the dataset to lower case
    df = df.rename(lambda x : x.lower().strip(),axis=1)
    
    #First, we divide the dataframe to male and female section.
    male = df[df['gender']=='Male'] 
    female = df[df['gender']=='Female']

    #Second, we select male and female 'current' and 'former' smokers.
    male_smokers = (male['smoking_history'] == 'current') | (male['smoking_history'] == 'former')
    female_smokers = (female['smoking_history'] == 'current') | (female['smoking_history'] == 'former')
    
    #Then, we select male and female who have never smoked.
    male_non_smokers = (male['smoking_history'] == 'never')
    female_non_smokers =(female['smoking_history'] == 'never')
    
    #Next, we select diabetic and non diabetic male and female
    male_diabetic = (male['diabetes'] == 1)
    female_diabetic= (female['diabetes'] == 1)   
    
    #Now, we get the lenght of male and female diabetic smokers and non_smokers.
    male_dia_smo = len(male[male_smokers & male_diabetic])
    fema_dia_smo = len(female[female_smokers & female_diabetic])
    
    male_dia_non_smo = len(male[male_non_smokers & male_diabetic])
    fema_dia_non_smo = len(female[female_non_smokers & female_diabetic])
    
    # Finally, we output the ratio within a dictionary.
    output_dic = {}
    output_dic['Ratio between Diabetic Smokers (current and former) and Diabetic non-Smokers in Male'] = male_dia_smo / male_dia_non_smo
    output_dic['Ratio between Diabetic Smokers (current and former) and Diabetic non-Smokers in Female'] = fema_dia_smo / fema_dia_non_smo
    return output_dic
  
    # returns {'Ratio between Diabetic Smokers (current and former) and Diabetic non-Smokers in Male': 1.0699404761904763,
    #'Ratio between Diabetic Smokers (current and former) and Diabetic non-Smokers in Female': 0.5494505494505495}
    
    #So it seems that the number of Diabetic Smokers (current and former) and Diabetic non-Smokers in men is roughly equal,
    #However, the number of Diabetic Smokers (current and former) is approximately double comparing to thenumber of non-Smokers diabetic in women. 
