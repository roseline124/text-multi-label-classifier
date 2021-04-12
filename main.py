from typing import Optional

from fastapi import FastAPI
from classifier import text_multi_label_classifier
import pandas as pd

app = FastAPI()
clf, feature_transformer, multilabel = text_multi_label_classifier.classifier()


@app.get("/")
async def read_root():
    return {"msg": "World"}


@app.get("/tags")
async def read_post_tags(title: Optional[str] = None, tags: Optional[str] = None):
    df_test = pd.DataFrame(
        {'title': [title], 'external_tags': [tags]})
    Xt = feature_transformer.transform(df_test)
    result = multilabel.inverse_transform(clf.predict(Xt))
    tags = [*result[0]]  # unpack [('tag1', 'tag2')] -> ['tag1', 'tag2']
    return {"tags": tags}
