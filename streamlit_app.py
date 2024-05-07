import streamlit as st 导入streamlitas st
import pandas as pd 导入 pandasas pd
 
st.write("""
# My first app # 我的第一个应用程序
Hello *world!* 你好世界！*
""") “””）
 
df = pd.read_csv("my_data.csv")
st.line_chart(df)
