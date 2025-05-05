import pandas as pd
import streamlit as st
from joblib import load
from sklearn.metrics import accuracy_score

model = load('sleep_quality_predictor.joblib')

try:
  x_test = pd.read_csv()
  y_test = pd.read_csv()
  y_test = y_test.squeeze()
  show_accuracy = True
except:
  show_accuracy = False