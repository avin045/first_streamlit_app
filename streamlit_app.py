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
my_fruits_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruits_list);
