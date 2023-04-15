import streamlit
import pandas
streamlit.title('My parents new Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('omega 3 , Blueberry & Oatmeal')
streamlit.text('kale , Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-range eggs')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
# ,['Avocado'])
 # ,'Strawberries'])
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])
streamlit.dataframe(fruits_to_show)
#streamlit.dataframe(my_fruit_list)
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
streamlit.text(fruityvice_response.json())
# take the json version of the data and normalie it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# loads the data into dataframe which converts into table format
streamlit.dataframe(fruityvice_normalized)
import snowflake.connector
