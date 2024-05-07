import streamlit as st # 导入streamlitas st
import pandas as pd # 导入 pandasas pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("my_data.csv")
st.line_chart(df)
