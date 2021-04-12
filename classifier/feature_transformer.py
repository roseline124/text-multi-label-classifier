from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import FeatureUnion, Pipeline

from .tokenizer.custom_tokenizer import stopwords


def _to_unicode(column_name):
    """type casting to unicode for vectorizing with tfidf"""
    return FunctionTransformer(lambda x: x[column_name].values.astype('U'), validate=False)


def _text_pipeline(column_name, tokenizer):
    """each pipelines in second parameter must have transfrom method"""
    return Pipeline([
        ('type_casting', _to_unicode(column_name)),
        ('tfidf', TfidfVectorizer(tokenizer=tokenizer,
         max_features=10000, stop_words=stopwords))  # ngram_range=(1, 3) 일단 제외
    ])


def text_transformer(df, field_pairs, tokenizer):
    """
    vectorize text fields and union features. use like below example.

    transformer = text_transformer(df, field_pairs)
    transformer.fit(df)
    X = transformer.transform(df)

    <parmas>
    @df: dataframe
    @field_pairs: list of (original_field_name, target_field_name) set
    @tokenizer: tokenizer
    """
    feature_pipelines = []
    for original_field_name, target_field_name in field_pairs:
        pipeline = (target_field_name, _text_pipeline(
            original_field_name, tokenizer))
        feature_pipelines.append(pipeline)

    transformer = FeatureUnion(feature_pipelines)
    return transformer
