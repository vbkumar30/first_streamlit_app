import streamlit
import pandas
streamlit.title('My parents new Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('omega 3 , Blueberry & Oatmeal')
streamlit.text('kale , Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-range eggs')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
