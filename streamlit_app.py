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
# seperate the the base URL from the fruit name.
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# Remove the line for the raw json data.
# Take the json verson of the response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Output it on the screen as a table
streamlit.dataframe(fruityvice_normalized)
# The user is asked to enter a fruit choicer .
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# Display on the screen the fruit choice


streamlit.write('The user entered ', fruit_choice)
# Display on the screen the fruit choice
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)












































