import pandas as pd 
dev_survey = pd.read_csv('./comma_seperated_values/dev_survey/survey_results_public.csv')

main_data = dev_survey.loc[:, ['ResponseId', 'LanguageHaveWorkedWith']]

from collections import Counter 

count = Counter()
for languages in main_data['LanguageHaveWorkedWith']:
    num_of_languages = str(languages).split(';')
    count.update(num_of_languages)

popular_languages = dict(count.most_common(10))
popular_languages.values()

from matplotlib import pyplot as plt
plt.style.use('ggplot')
plt.bar(popular_languages.keys(), popular_languages.values(), color = 'k', width=0.4)
plt.xlabel('Languages')

plt.title('Poplarity of languages')
plt.ylabel('Programmers using the language')
plt.grid(False)
plt.savefig('./images_from_matplotlib/bar_chart_languages')
plt.show()

