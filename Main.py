import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as np
 

st.set_page_config(page_title="Dashboard ", page_icon="📈", layout="wide")  
st.header("Percentile, 5 number summary, Categorical")
st.markdown("##")
 
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
     
df=pd.read_excel('data.xlsx', sheet_name='Sheet1')



tab1, tab2 = st.tabs(["My Excel Database","Sales By percentiles"])

with tab1:
 with st.expander("Show Workbook"):
  #st.dataframe(df_selection,use_container_width=True)
  shwdata = st.multiselect('Filter :', df.columns, default=["SALES","ORDERDATE","STATUS","YEAR_ID","PRODUCTLINE","CUSTOMERNAME","CITY","COUNTRY"])
  st.dataframe(df[shwdata],use_container_width=True
  )

with tab2.caption("Sales By percentiles"):
 c1,c2,c3,c4,c5=st.columns(5)
 with c1:
   st.info('Percentile 25 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 25):,.2f}")
 with c2:
   st.info('Percentile 50 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 50):,.2f}")
 with c3:
   st.info('Percentile 75 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 75):,.2f}")
 with c4:
   st.info('Percentile 100 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 100):,.2f}")
 with c5:
   st.info('Percentile 0 %', icon="⏱")
   st.metric(label='USD', value=f"{np.percentile(df['SALES'], 0):,.2f}")

def ad():
 theme_plotly = None # None or streamlit
 column=st.sidebar.selectbox('select a column',['COUNTRY','PRODUCTLINE','CITY'])
 type_of_column=st.sidebar.radio("What kind of analysis",['Categorical','Numerical'])

 c1,c2=st.columns([2,1])
 with c1:
   if type_of_column=='Categorical':
    dist=pd.DataFrame(df[column].value_counts())
    fig=px.bar(dist, title='Category by count',orientation="v")
    fig.update_layout(legend_title=None, xaxis_title="Observation", yaxis_title='Count')
    st.write(fig, theme=theme_plotly)
   else:
    st.subheader("Number Summary")
    st.dataframe(df['SALES'].describe(),use_container_width=True)

 with c2:
   st.subheader("Total Sales")
   st.metric(label='USD', value=f"{np.sum(df['SALES'], 0):,.2f}",help="sum",delta=np.average(df.SALES),
    delta_color="inverse")
    
    
ad()
