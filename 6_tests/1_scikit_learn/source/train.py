from __future__ import print_function
import argparse
import joblib
import os
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()

    # hyperparameters for scikit-learn model
    parser.add_argument('--param_cv', type=int, default=5) # cross validation fold
    parser.add_argument('--param_n_neighbors', type=int, default=5) # number of neighbors
    parser.add_argument('--param_weights', type=str, default='uniform') # weight function used in prediction
    parser.add_argument('--param_p', type=int, default=2) # power parameter for the Minkowski metric
    
    # SageMaker specific arguments. defaults are set in the environment variables.
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])

    args = parser.parse_args()

    # take the set of files and read them all into a single pandas dataframe
    input_files = [os.path.join(args.train, file) for file in os.listdir(args.train)]
    if len(input_files) == 0:
        raise ValueError(('There are no files in {}.\n' +
                          'This usually indicates that the channel ({}) was incorrectly specified,\n' +
                          'the data specification in S3 was incorrectly specified or the role specified\n' +
                          'does not have permission to access the data.').format(args.train, "train"))
        
    raw_data = [pd.read_csv(file, header=None, engine="python") for file in input_files]
    train_data = pd.concat(raw_data)

    # labels are in the first column, features in rest columns
    train_y = train_data.iloc[:, 0]
    train_X = train_data.iloc[:, 1:]

    # scikit-learn usual model definition
    clf = KNeighborsClassifier(n_neighbors=args.param_n_neighbors, weights=args.param_weights, p=args.param_p)
    
    # calculate accuracy based on cross validation
    accuracy_scores = cross_val_score(clf, train_X, train_y, cv=args.param_cv)
    
    # fit on full training data
    clf.fit(train_X, train_y)
    
    # print out accuracy from cross validation
    print('use {}-fold cross validation score'.format(args.param_cv))
    print('accuracy: {}'.format(accuracy_scores.mean()))

    # dump model for use in model_fn function for predictions
    joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))
    

def model_fn(model_dir):
    """Deserialized and return fitted model
    
    Note that this should have the same name as the serialized model in the main method
    """
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf

