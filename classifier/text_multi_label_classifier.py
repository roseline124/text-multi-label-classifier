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

# for db query
from queries import get_tag_targets_doc
from settings import PostgresConfiguration

pg = PostgresConfiguration()


def classifier():
    """
    return classifier, feature_transformer
    """

    # fetch data
    print('🔥 get target data...')
    df = pd.read_sql(get_tag_targets_doc, pg.postgres_db_path)

    # preprocess: one-hot encoding + get target data
    print('🧹 preprocess: one-hot encoding...')
    df = df.rename(index=str, columns={"targets": "tags"})
    multilabel = preprocessing.MultiLabelBinarizer()
    y = multilabel.fit_transform(df['tags'])

    # transform with feature pipelines
    print('⛏ get feature transformer and transform data...')
    transformer = feature_transformer.text_transformer(
        df, [('title', 'title'), ('external_tags', 'tags')], tokenizer, transformer_weights={'tags': 7, 'title': 1})

    transformer.fit(df)
    X = transformer.transform(df)

    # classify
    print('🏭 build classification model...')

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0)

    sgd = SGDClassifier(loss="modified_huber", max_iter=1000,
                        tol=1e-3, n_iter_no_change=10, n_jobs=-1)
    clf = OneVsRestClassifier(sgd)
    clf.fit(X_train, y_train)

    print('🏁 finish building classifier!')
    return clf, transformer, multilabel
