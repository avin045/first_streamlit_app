import streamlit
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
streamlit.dataframe(my_fruit_list);

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
