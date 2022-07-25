import pandas as pd

def calculate_demographic_data(print_data = True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df.loc[df['education'] == 'Bachelors'].shape[0] * 100 / df.shape[0] 
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    adv_edu = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')].shape[0]
    df1 = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    adv_edu_more = df1.loc[(df1['salary'] == '>50K')].shape[0]
    percentage_adv_edu = adv_edu_more * 100  / adv_edu
    # What percentage of people without advanced education make more than 50K?
    not_adv_edu = df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')].shape[0]
    df2 = df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    not_adv_edu_more = df2.loc[(df2['salary'] == '>50K')].shape[0]
    percentage_not_adv_edu = not_adv_edu_more * 100  / not_adv_edu
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    total_rows = df.shape[0]
    higher_education = (adv_edu * 100) / total_rows
    lower_education = (not_adv_edu * 100) / total_rows
    # percentage with salary >50K
    higher_education_rich = adv_edu_more * 100 / total_rows
    lower_education_rich = not_adv_edu_more * 100 / total_rows
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = (df['hours-per-week']).min()
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (df['hours-per-week'] == 1).sum()
    rich_percentage = df.loc[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')].shape[0] * 100 / num_min_workers
    # What country has the highest percentage of people that earn >50K?
    serie_1 = df.loc[df['salary'] == '>50K', 'native-country'].value_counts()
    serie_2 = df['native-country'].value_counts()
    
    list = []
    for i in range(0, len(serie_1)):
      list.append(serie_1.index[i])  
    
    dict1 = {}
    dict2 = {}
    dict3 = {}

    for i in list: 
      dict1[i] = serie_2[i]
      dict2[i] = serie_1[i]
      dict3[i] = (dict2[i] * 100 / dict1[i])

    highest_earning_country = (df.loc[df['salary'] == '>50K', 'native-country'].value_counts()).index[0]
    highest_earning_country_percentage = max(dict3, key = dict3.get)
    
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K'), 'occupation'].value_counts().index[0]

    
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }