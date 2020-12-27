from __future__ import print_function
import argparse
import joblib
import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    
    # hyperparameters for scikit-learn model
    parser.add_argument('--param_kernel', type=str, default='rbf') # kernel
    parser.add_argument('--param_C', type=int, default=1) # regularization parameter
    
    # SageMaker specific arguments. defaults are set in the environment variables.
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    parser.add_argument('--test', type=str, default=os.environ['SM_CHANNEL_TEST'])

    args = parser.parse_args()

    # take the set of files and read them all into a single pandas dataframe
    input_files_train = [os.path.join(args.train, file) for file in os.listdir(args.train)]
    if len(input_files_train) == 0:
        raise ValueError(('There are no files in {}.\n' +
                          'This usually indicates that the channel ({}) was incorrectly specified,\n' +
                          'the data specification in S3 was incorrectly specified or the role specified\n' +
                          'does not have permission to access the data.').format(args.train, "train"))
        
    # take the set of files and read them all into a single pandas dataframe
    input_files_test = [os.path.join(args.test, file) for file in os.listdir(args.test)]
    if len(input_files_test) == 0:
        raise ValueError(('There are no files in {}.\n' +
                          'This usually indicates that the channel ({}) was incorrectly specified,\n' +
                          'the data specification in S3 was incorrectly specified or the role specified\n' +
                          'does not have permission to access the data.').format(args.test, "train"))
        
    raw_data = [pd.read_csv(file, header=None, engine="python") for file in input_files_train]
    train_data = pd.concat(raw_data)
    
    raw_data = [pd.read_csv(file, header=None, engine="python") for file in input_files_test]
    test_data = pd.concat(raw_data)

    # labels are in the first column, features in rest columns
    train_y = train_data.iloc[:, 0]
    train_X = train_data.iloc[:, 1:]
    
    # labels are in the first column, features in rest columnsd
    test_y = test_data.iloc[:, 0]
    test_X = test_data.iloc[:, 1:]

    # scikit-learn usual model definition
    clf = LogisticRegression(random_state = 1, max_iter = 1000)
    
    # model fit
    clf.fit(train_X, train_y)
    
    # model predict on test data
    pred_y = clf.predict(test_X)
    
    # accuracy as comparison between prediction and test data
    accuracy_metrics_score = accuracy_score(test_y, pred_y)
    
    # print out accuracy from cross validation
    print('test-accuracy: {}'.format(accuracy_metrics_score))

    # dump model for use in model_fn function for predictions
    joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))
    

def model_fn(model_dir):
    """Deserialized and return fitted model
    
    Note that this should have the same name as the serialized model in the main method
    """
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf

