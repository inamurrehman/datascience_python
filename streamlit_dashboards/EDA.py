from doctest import Example
import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import profileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns

# Webapp Title

st.markdown(''' 
# Exploratory Data Analysis web Application
This app is developed is developed by cadanics youtube channel for EDA analysis 
''')

# How to upload a file from PC
with st.sidebar.header('Upload your dataset (.csv)'):
    uploaded_file = st.sidebar.file_uploader('Upload your file', type = ['csv'])
    df = sns.load_dataset('titanic')
    #st.sidebar.markdown['Example CSV file']#(df)

# Profiling report for pandas
if uploaded_file is not None:
    @st.cache       # cache the data to increase speed
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df= load_csv()
    pr = profileReport(df, explorative = True)
    st.header('** Input DF**')
    st.write(df)
    st.write('---')
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for the CSV file, upload it')
    if st.button('Press to use example data'):
        # Example dataset
        @st.cache
        def load_data():
            a = pd.DataFrame(np.random.rand(100,5),
                            columns= ['age', 'banana', 'codanics', 'Doutchland', 'Edar'])
            return a
        df = load_data()
        pr= profileReport(df, explorative = True)
        st.header('** Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pands Profiling Report**')
        st_profile_report(pr)
    