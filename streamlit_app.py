import streamlit
import requests

import snowflake.connector # snowflake

# TITLE
streamlit.title('My Mom\'s New Healthy Diner');

# HEADER
streamlit.header('Breakfast Favorites');

# TEXT
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal');
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie');
streamlit.text('🐔 Hard-Boiled Free-Range Egg');
streamlit.text('🥑🍞 Avocado Toast');

# Another HEADER
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');


# IMPORTING PANDAS
import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

# SET INDEX AS FRUIT NAME
my_fruit_list = my_fruit_list.set_index('Fruit');

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Avocado'])
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Avocado'])

# Show the Fruits based on the User Selection.
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the TABLE on page
# streamlit.dataframe(my_fruit_list);
streamlit.dataframe(fruits_to_show);


# New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!");

# -------------------------------------------------- USER INPUT FOR REQUEST -------------------------------------------------- #
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# -------------------------------------------------- RESPONSE from REQUESTS -------------------------------------------------- #
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice);
# streamlit.text(fruityvice_response)
# streamlit.text(fruityvice_response.json()) # just writes the data to the screen

# CONVERTS json data to Structured(Normalized) Format
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# Display the Normalized(structured) Data
streamlit.dataframe(fruityvice_normalized)

# ------------------------------------------- snowflake codes ------------------------------------------- #
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
# my_data_row = my_cur.fetchone() # just fetches one row

my_data_rows = my_cur.fetchall() # fetches all the rows

# Allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('Thanks for adding ',add_my_fruit)

streamlit.header("The fruit load list contains:") #streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_rows) # streamlit.text(my_data_row)
