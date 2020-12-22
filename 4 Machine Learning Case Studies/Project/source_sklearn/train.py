from __future__ import print_function
import argparse
import os
import pandas as pd
import joblib
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score

# Provided model load function
def model_fn(model_dir):
    """Load model from the model_dir. This is the same model that is saved
    in the main if statement.
    """
    print("Loading model.")
    
    # load using joblib
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    print("Done loading model.")
    
    return model

if __name__ == '__main__':
    
    # All of the model parameters and training parameters are sent as arguments
    # when this script is executed, during a training job
    
    # Here we set up an argument parser to easily access the parameters
    parser = argparse.ArgumentParser()

    # SageMaker parameters, like the directories for training data and saving models; set automatically
    # Do not need to change
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--data-dir', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    
    # hyperparameters for scikit-learn model
    parser.add_argument('--param_cv', type=int, default=5) # cross validation fold
    
    # args holds all passed-in arguments
    args = parser.parse_args()

    # Read in csv training file
    training_dir = args.data_dir
    train_data = pd.read_csv(os.path.join(training_dir, "train.csv"), header=None, names=None)

    # Labels are in the first column
    train_y = train_data.iloc[:,0]
    train_x = train_data.iloc[:,1:]
    
    # scikit-learn usual model definition
    clf = GaussianNB()
    
    # calculate accuracy based on cross validation
    accuracy_scores = cross_val_score(clf, train_x, train_y, cv=args.param_cv)
    
    # fit on full training data
    clf.fit(train_x, train_y)
    
    # print out accuracy from cross validation
    print('use {}-fold cross validation score'.format(args.param_cv))
    print('accuracy: {}'.format(accuracy_scores.mean()))

    # Save the trained model
    joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))
