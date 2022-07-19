from sqlalchemy import true
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

@st.cache
def datacache():
    return pd.read_csv('data/Iris.csv')

with header:
    st.title('Welcome to my first Project')
    st.text('this is my fist streamlit web app project  ......')

with dataset:
    st.header('Welcome to dataset')
    iris = datacache()


    fig, ax = plt.subplots(1,1)
    sns.kdeplot(data = iris.drop('Id', axis = 1), shade = true)
    st.pyplot(fig)

with features:
    st.header('Welcome to features')
    st.text('this is my fist streamlit web app project  ......')
    st.markdown('* **SepalLengthCm** : tells the Sepal Length')
    st.markdown('* **SepalWidthCm** : tells the Sepal Width')
    st.markdown('* **PetalLengthCm** : tells the Petal Length')
    st.markdown('* **PetalWidthCm** : tells the Petal Width')


with model_training:
    st.header('Welcome to model_training')
    st.text('this is my fist streamlit web app project  ......')

    se_col, disp_col = st.columns(2)
    max_depth = se_col.slider('what should be the max depth of the model', min_value = 10, max_value = 100, value = 30, step = 10)
    n_estmators = se_col.selectbox('how many trees wanted', options = [100,200,300,400,500],index = 0)
    input_feat = se_col.text_input('which feature to chose as input', 'SepalLengthCm')

    disp_col.subheader('mean abs error')
    disp_col.write('0 precent')
    disp_col.subheader('mean squared error')
    disp_col.write('0 precent')
    disp_col.subheader('root mean squared error')
    disp_col.write('0 precent')



