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
streamlit.dataframe(my_fruit_list)
# Let us put a pick list so that the customer can select the fruit they want
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))
# Display the table on the page
streamlit.dataframe(my_fruit_list)
# Just numbers won't make any sense . He wants to pick the fruits by name
import pandas
my_fruit_list = my_fruit_list.set_index('Fruit')

