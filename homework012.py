import pandas as pd
df = pd.read_csv('survey_results_public.csv')
while True:
    user_choice = input("Please choose:\n1.Hobbyist\n2.Age\n3.Country\n4.CurrencyDesc\n0.Exit\n--> ")
    if user_choice == '1':
        print('---------Hobbyist---------')
        a = df.loc[df['MainBranch'] == 'I am a developer by profession']
        a1 = a.loc[df['Hobbyist'] == 'Yes']
        a2 = a.loc[df['Hobbyist'] == 'No']
        print('Yes:', a1.count()[2])
        print('No:', a2.count()[2])
    elif user_choice == '2':
        print('---------Age---------')
        pd.set_option('display.max_columns', 8)
        b = df.loc[df['MainBranch'] == 'I am a developer by profession']
        print('Min:', b.min()[2])
        print('Max:', b.max()[2])
        print('Average:', b.sum()[2] // b['Respondent'].count())
    elif user_choice == '3':
        print('---------Country---------')
        print(df['Country'].value_counts())
    elif user_choice == '4':
        print('---------CurrencyDesc---------')
        print(df['CurrencyDesc'].value_counts())
    elif user_choice == '0':
        quit()
    else:
        print('Choice is out of range!')