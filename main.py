from fastapi import FastAPI
from schemas import Paper, paper_to_obj

app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/{paper}/{article}")
def get_article(paper: Paper, article: str):
    article = paper_to_obj[paper](article)
    response = {'headline': article.get_headline(), 'text': article.get_text(),
                'description': article.get_description()}
    return response


@app.get("/{paper}/{article}/description")
def get_article_text(paper: Paper, article: str):
    report_obj = get_article(paper, article)
    return report_obj['description']


@app.get("/{paper}/{article}/text")
def get_article_text(paper: Paper, article: str):
    report_obj = get_article(paper, article)
    return report_obj['text']


@app.get("/{paper}/{article}/headline")
def get_article_headline(paper: Paper, article: str):
    report_obj = get_article(paper, article)
    return report_obj['headline']
