import streamlit
import snowflake.connector
import pandas
streamlit.title('Zena\'s Amazing Athleisure Catalog12')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

