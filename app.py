import streamlit as st
import pickle
import numpy as np
import warnings 
warnings.filterwarnings('ignore')
st.set_page_config('laptop price predictor',page_icon='random')
#importing model
pipe=pickle.load(open('files/pipe.pkl','rb'))
df=pickle.load(open('files/df.pkl','rb'))
st.title("Laptop Price Predictor")
company=st.selectbox('Brand',df['Company'].unique())
ram=st.number_input("RAM(in GB)")
touchscreen=st.selectbox("Touch Screen",["No","Yes"])
screen_size=st.number_input("Screen size")
cpu=st.selectbox('CPU',df['Cpu name'].unique())
os=st.selectbox("Operating System",df['os'].unique())
gpu=st.selectbox("GPU",df['Gpu'].unique())
hdd=st.number_input("HDD (in GB)")
ssd=st.number_input("SSD (in GB)")
if st.button('Predict Price'):
    #query
    if touchscreen=='Yes':
        touchscreen=1
    else:
        touchscreen=0
    query=np.array([company,ram,gpu,touchscreen,cpu,hdd,ssd,os,screen_size])
    query=query.reshape(1,9)
    st.title("&#8377;"+str(int(np.exp(pipe.predict(query)[0]))))


