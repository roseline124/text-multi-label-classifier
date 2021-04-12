# -*- coding: utf-8 -*-
import pandas as pd
import re

from sklearn import preprocessing
from os import path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.multiclass import OneVsRestClassifier

from . import feature_transformer
from .tokenizer.custom_tokenizer import tokenizer


def classifier():
    """
    return classifier, feature_transformer
    """

    # fetch data
    print('🔥 get target data...')
    df = pd.read_csv(path.abspath('./data/posts_target.csv'), index_col=0)

    # preprocess: one-hot encoding + get target data
    print('🧹 preprocess: one-hot encoding...')
    df['tags'] = df['targets'].apply(lambda x: re.sub('{|}', '', x).split(','))
    multilabel = preprocessing.MultiLabelBinarizer()
    y = multilabel.fit_transform(df['tags'])

    # transform with feature pipelines
    print('⛏ get feature transformer and transform data...')
    transformer = feature_transformer.text_transformer(
        df, [('title', 'title'), ('external_tags', 'tags')], tokenizer)

    transformer.fit(df)
    X = transformer.transform(df)

    # classify
    print('🏭 build classification model...')

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0)

    sgd = SGDClassifier(max_iter=1000, tol=1e-3,
                        n_iter_no_change=10, n_jobs=-1)
    clf = OneVsRestClassifier(sgd)
    clf.fit(X_train, y_train)

    print('🏁 finish building classifier!')
    return clf, transformer, multilabel
