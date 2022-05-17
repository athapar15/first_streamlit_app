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
def get_fruityvoice_data(this_fruit_choice):
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)   
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
rerurn (fruityvice_normalized)

#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
     streamlit.error("Please select a fruit to get information.")
   else:    
    back_from_function = get_fruityvoice_data(fruit_choice)
    streamlit_dataframe(back_from_function)

#While we troubleshoot
streamlit.stop()
#streamlit.write('The user entered', fruit_choice)

#streamlit.text(fruityvice_response.json()) #Just writes the data to the screen

#take the json version of the response and normalize it
#output it ot the screen as a table



#queries account metadata
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

#queries data within snowflake database
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

#Allow end user to add fruit ot table
fruit_choice = streamlit.text_input('What fruit would you like to add','jackfruit')
streamlit.write('The user added: ', fruit_choice)

#this won't work but for class purposes only
my_cur.execute = ("insert into fruit_load_list values('from streamlit')")
