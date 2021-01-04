# Capstone Project: Detecting Fake News with Supervised Learning

Explanation of directories:

- [0_literature](https://github.com/benjaminperucco/udacity-nano-mle/tree/master/5_capstone_project/0_literature): Contains the benchmark literture. 
- [1_proposal](https://github.com/benjaminperucco/udacity-nano-mle/tree/master/5_capstone_project/1_proposal): Contains the initial project proposal.
- [2_project](https://github.com/benjaminperucco/udacity-nano-mle/tree/master/5_capstone_project/2_project): Contains the code to produce the results.
	- [0_download_fake_news_data.ipynb](https://github.com/benjaminperucco/udacity-nano-mle/tree/master/5_capstone_project/2_project/0_download_fake_news_data.ipynb): Downloads the data, performs the text processing and creates a clean csv dataset.
	- [1_feature_engineering.ipyn](https://github.com/benjaminperucco/udacity-nano-mle/tree/master/5_capstone_project/2_project/1_feature_engineering.ipynb): Transposes the text into numerical, structure features according to the TF and TF-IDF model.
	- [2_1_model_sklearn.ipynb](https://github.com/benjaminperucco/udacity-nano-mle/tree/master/5_capstone_project/2_project/2_1_model_sklearn.ipynb): Contains the sci-kit learn models (needs the [source](https://github.com/benjaminperucco/udacity-nano-mle/tree/master/5%20Capstone/2%20Project/source) directory as well).
	- [2_2_model_xgboost.ipynb](https://github.com/benjaminperucco/udacity-nano-mle/tree/master/5_capstone_project/2_project/2_2_model_xgboost.ipynb): Contains the XGBoost model deployed by available on the [Amazon SageMaker platform](https://aws.amazon.com/sagemaker).
	- [3_postprocessing.ipyn](https://github.com/benjaminperucco/udacity-nano-mle/tree/master/5_capstone_project/2_project/3_postprocessing.ipynb): Loads and displays all the model results.
	- [4_explorative_data_analysis.ipynb](https://github.com/benjaminperucco/udacity-nano-mle/tree/master/5_capstone_project/2_project/4_explorative_data_analysis.ipynb): Performs the explorative data analysis.
- [3_report](https://github.com/benjaminperucco/udacity-nano-mle/tree/master/5_capstone_project/3_report): Contains the final report.

Used platform:

- All Jupyter notebooks can be run on the [Amazon SageMaker platform](https://aws.amazon.com/sagemaker).

Data:

- Data is from [Fake and Real News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)
available on [kaggle.com](https://www.kaggle.com). Please create an API token to download
the data (see guide https://github.com/Kaggle/kaggle-api#api-credentials).
