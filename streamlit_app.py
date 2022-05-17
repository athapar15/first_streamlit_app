import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

#import streamlit
streamlit.title('My Parents Healthy New Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pick list here so that they can pick their own fruit
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#Display Table on Page
streamlit.dataframe(fruits_to_show)

#create reapeatable code block called a function
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)   
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return (fruityvice_normalized)

#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
     streamlit.error("Please select a fruit to get information.")
   else:    
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit_dataframe(back_from_function)
except URLError as e:
   streamlit.error()

#While we troubleshoot
