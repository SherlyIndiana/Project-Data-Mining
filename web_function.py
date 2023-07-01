#import module
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick
import sklearn
import imblearn
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from imblearn.over_sampling import SMOTE
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import f1_score, accuracy_score, recall_score, precision_score, roc_auc_score

@st.cache_data()
def load_data():
    #load dataset
    df = pd.read_csv('Marketing-Deposito.csv')

    x = df[["age","job","marital","education","default","balance","housing","loan","contact","duration","campaign"]]
    y = df[["subscribed"]]

    return df, x, y

@st.cache_data()
def train_model(x,y):
    nb_params = {"var_smoothing": np.logspace(0, -9, num = 100)}
    model = GridSearchCV(GaussianNB(), 
                   param_grid = nb_params, 
                   cv = 10, 
                   scoring = 'f1')

    model.fit(x,y)
    score = model.score(x,y)
    return model, score

def predict(x, y, features):
    model, score = train_model(x,y)
    prediction = model.predict(np.array(features).reshape(1,-1))

    return prediction, score