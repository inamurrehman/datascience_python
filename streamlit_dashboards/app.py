from requests import options
import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# make containers
header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Kashti ke app')
    st.text('In this project we will work on kashti dataset')

with data_sets:
    st.header('Kashti doob gaye')
    st.text('we will work with titanic datasets')
    # import data
    df = sns.load_dataset('titanic')
    df = df.dropna()
    st.write(df.head(10))

    st.subheader('Kinay aadmy thy kashti me')
    st.bar_chart(df['sex'].value_counts())

    # Other charts
    st.subheader('class ke hisab se firq')
    st.bar_chart(df['class'].value_counts())

    # Barcharts
    st.bar_chart(df['age'].sample(10)) #

with features:
    st.header('These are our app features')
    st.text('Dealing with features')
    st.markdown('1. **Feature 1:** This will till us something')
    st.markdown('2. **Feature 2:** This will till us something')

with model_training:
    st.header('Kashti walon ka kia bana - model training')
    st.text('We will use different model for testing')
    # Making column, selection and display
    input, display = st.columns(2)

    # First column has selection
    max_depth = input.slider('How many people do you know', min_value=10, max_value = 100, value =20, step= 5)
    
# N_estimators
n_estimators = input.selectbox('How many trees should be there in a RF', options = [50,100,200,300, 'No limit'])

# Adding list of features
input.write(df.columns)

# Input features from users
input_features = input.text_input('Which feature we should use?')

# Machine Learning model
model = RandomForestRegressor(max_depth=max_depth, n_estimators= n_estimators)
# Condition 
if n_estimators == 'No limit':
    model = RandomForestRegressor(max_depth= max_depth)
else:
    model = RandomForestRegressor(max_depth= max_depth, n_estimators= n_estimators)
    
# Defining X and y
X = df[[input_features]]
y = df[['fare']]

# Fit model
model.fit(X,y)
pred = model.predict(y)



# Display metices
display.subheader('Mean absolute error of the model is:')
display.write(mean_absolute_error(y, pred))
display.subheader('Mean squered error of the model is:')
display.write(mean_squared_error(y, pred))
display.subheader('R squared error of the model is:')
display.write(r2_score(y, pred))

