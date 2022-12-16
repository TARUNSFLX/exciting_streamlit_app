import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣''Omega 3 and Blueberry Oatmeal')
streamlit.text('🥬''Kale, Spinach and Rocket Smoothie')
streamlit.text('🥚''Hard-Boiled Free-Range Egg')
streamlit.text('🥑''Avocado Toast')

streamlit.header('🍌''🥭''Build Your Own Fruit Smoothie''🥑''🫐')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let us put a pick list so that the customer can select the fruit they want
fruits_selected = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice API response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

