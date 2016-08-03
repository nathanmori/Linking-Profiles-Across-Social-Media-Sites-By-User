# -*- coding: utf-8 -*-

# Author: Nathan Mori <nathanmori@gmail.com>

import numpy as np
from scipy.sparse.linalg import norm
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pdb


class all(object):
    """"""

    def __init__(self):
        """"""

        pass

    def fit(self, (df_X_train, X_train_github, X_train_meetup,
                   X_train_github_tfidf, X_train_meetup_tfidf), y=None):
        """"""

        return self

    def transform(self, (df_X, X_github, X_meetup, X_github_tfidf,
                         X_meetup_tfidf)):
        """"""

        df_X['text_sim'] = [cosine_similarity(x1, x2)[0,0] for x1, x2 in
                                  zip(X_github, X_meetup)]
        df_X['text_sim_tfidf'] = [cosine_similarity(x1, x2)[0,0] for x1, x2 in
                                  zip(X_github_tfidf, X_meetup_tfidf)]

        df_X['text_norm_github'] = [norm(x) for x in X_github]
        df_X['text_norm_meetup'] = [norm(x) for x in X_meetup]
        df_X['DIFF:text_norm'] = df_X['text_norm_github'] - \
                                 df_X['text_norm_meetup']

        df_X['text_norm_github_tfidf'] = [norm(x) for x in X_github_tfidf]
        df_X['text_norm_meetup_tfidf'] = [norm(x) for x in X_meetup_tfidf]
        df_X['DIFF:text_norm_tfidf'] = df_X['text_norm_github_tfidf'] - \
                                       df_X['text_norm_meetup_tfidf']

        df_X['text_dot'] = [np.dot(x1, x2.T)[0][0,0] for x1, x2
                                                    in zip(X_github, X_meetup)]
        df_X['text_dot_tfidf'] = [np.dot(x1, x2.T)[0][0,0] for x1, x2
                                        in zip(X_github_tfidf, X_meetup_tfidf)]

        return df_X