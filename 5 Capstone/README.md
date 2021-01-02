# Capstone Project: Detecting Fake News using Supervised Learning

Explanation of directory:

- 1 Proposal: Initial project proposal including literature.
- 2 Project: Relevant code to produce results.
	- [0_download_fake_news_data.ipynb](https://github.com/benjaminperucco/udacity-nano-mle/blob/master/5%20Capstone/2%20Project/0_download_fake_news_data.ipynb): Downloads the data, performs the text processing and creates a clean csv dataset.
	- [1_feature_engineering.ipyn](https://github.com/benjaminperucco/udacity-nano-mle/blob/master/5%20Capstone/2%20Project/1_feature_engineering.ipynb): Transpose the text into numerical, structure features according to the TF and TF-IDF model.
	- [2_1_model_sklearn.ipynb](https://github.com/benjaminperucco/udacity-nano-mle/blob/master/5%20Capstone/2%20Project/2_1_model_sklearn.ipynb): Contains the sci-kit learn models (needs the /source directory as well).
	- [2_2_model_xgboost.ipynb](https://github.com/benjaminperucco/udacity-nano-mle/blob/master/5%20Capstone/2%20Project/2_2_model_xgboost.ipynb): Contains the XGBoost model deployed by [Amazon SageMaker](https://aws.amazon.com/sagemaker).
	- [3_postprocessing.ipyn](https://github.com/benjaminperucco/udacity-nano-mle/blob/master/5%20Capstone/2%20Project/3_postprocessing.ipynb): Notebook to load and display all the model results.
	- [4_explorative_data_analysis.ipynb](https://github.com/benjaminperucco/udacity-nano-mle/blob/master/5%20Capstone/2%20Project/4_explorative_data_analysis.ipynb): Performs the explorative data analysis.
- 3 Report: Final report.

Used platform:

- All jupyter notebooks can be run on the [Amazon SageMaker platform](https://aws.amazon.com/sagemaker).

Data:

- Data is from [Fake and real news dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)
available on [kaggle.com](https://www.kaggle.com). Please download an API token to download
the data (see https://github.com/Kaggle/kaggle-api#api-credentials).
