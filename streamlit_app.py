import streamlit
import requests
import snowflake.connector # snowflake

from urllib.error import URLError

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

# 
def get_fruityvice_data(this_fruit_choice):
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice);
        # CONVERTS json data to Structured(Normalized) Format
        fruityvice_normalized = pd.json_normalize(fruityvice_response.json());
        return fruityvice_normalized

try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function); # Display the Normalized(structured) Data
except URLError as e:
    streamlit.error();


# -------------------------------------------------- USER INPUT FOR REQUEST -------------------------------------------------- #
# streamlit.write('The user entered ', fruit_choice)

# -------------------------------------------------- RESPONSE from REQUESTS -------------------------------------------------- #
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response)
# streamlit.text(fruityvice_response.json()) # just writes the data to the screen


streamlit.stop();

# ------------------------------------------- snowflake codes ------------------------------------------- #

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall();
        
# add button to load the fruit
if streamlit.button("Get Fruit Load List"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows  = get_fruit_load_list();
    streamlit.dataframe(my_data_rows);


