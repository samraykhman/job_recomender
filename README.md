# python_job_classifier

**Objective**

The goal of the project was to classify jobs for programmers by whether or not Python is a required programming language to know. For people such as myself, who have not had a programmer job before, or anyone who is looking for a new job, such a classifier could be very useful since it could quickly filter and search for a job by certain qualifications. In order to classify the jobs correctly, I needed to create a baseline model and then more advanced models that would be able to classify a job based on the overview of the job posting.

**Explaining the Data**

For my project, I web scraped job postings from [stackoverflow.com's](https://stackoverflow.com/jobs)job post portal. At the time of my scraping there were 2,893 jobs, but after removing rows with empty description or language columns, I was left with about 2,100 rows. I proceeded to create the following features/columns, job titles which refers to the position name, description which is a brief explanation of a job’s characteristics (such as part-time vs. full-time, is remote an option, etc.), languages as in the required programming languages required for the job, overview which is general information about the job (expectations and other requirements), and the URL of the job posting itself. I used the languages column to create my target variable, if Python was listed as a required language or not. Additionally, I had a heavy class imbalance where jobs that did not require Python made up 81% of the dataset. To fix this, I incorporated ADASYN over-sampling on the minority class to balance the data. I chose to use ADASYN rather than SMOTE, because ADASYN is an improved version of SMOTE, which adds dimensionality and makes the relationship between the artificially-generated and regular points less linear. (I also incorporated SMOTE over-balancing to see how the models performed to SMOTE compared to ADASYN). My code for the web scraping, feature creation and target creation can be found in the [eda_nb](eda_nb.ipynb). My code for balancing the data can be found in the [modeling_nb](modeling_nb.ipynb).

**Methodology**

After creating my dataframe of about 2100 job postings and balancing the data, I set up a Tfidf Vectorizer train-test split, so that I would be able to pass in the Overview column as the predictor variable. I then set up a Dummy Classifier as a baseline model. I proceeded to run Gridsearches for Naive Bayes Classifier, Random Forest Classifier and XGBoost Classier with the unbalanced data, the SMOTE'd data and the ADASYN'd data. I decided to focus on accuracy score because my data is not sensitive and I wanted to see how well my models are able to predict the target variable. I also decided to take a look at the F1-score to get a harmonic mean of the recall and precision scores. My code for the modeling can be found in the [modeling_nb](modeling_nb.ipynb).

**Findings**

The unbalanced XGBoost model returned the best results (Accuracy Score: 0.8887, F1 Score: 0.6627); the reason I believe that the unbalanced XGBoost model did better than the balanced one is because it did a better job handling the imbalance than it did by predicting based off of generated fake data points. The confusion matrices below give a deeper insight, the unbalanced XGBoost has a more symmetrical distribution of false positives and false negatives:
[unbalanaced_xgboost_confusion_matrix](images/xgb_confusion.png) [ada_balanaced_xgboost_confusion_matrix](images/balanced_xgb_confusion.png)

**Given More Time**

I would have liked to incorporate n-grams, in order to check the importance of phrases and not just single words. I would have liked to set up a support vector machine model, to attempt to increase the performance of my final model. Lastly, I would like to set up a recommendation engine that would take qualifications, location, and some consumer preferences to return jobs in your area that match your requests.


[CSV files I used and/or created](csv_files)

[Images used in my presentation](images)

[Link to Google Slides presentation](https://docs.google.com/presentation/d/1r-DMCfJ3oSQ2Kb5SObMfPTGq_1ICDQ3GoZZpufD3XX8/edit#slide=id.p)
