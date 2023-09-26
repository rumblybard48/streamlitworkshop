
import streamlit as st
st.title('Hello to my streamlit app :sunglasses:')
user_input = st.text_input("Enter your ame:")
st.write("Hello,", user_input)
age1 = st.slider("Select your Age:", 0, 100, 25) # (Min, Max, Start)
st.write("You are", age1, "years old.")
if st.button("Click me 🐣"):
    st.write("Peeka-Boo 👻") #  '+ user_input'
# Take user input
num1 = st.text_input("Enter the first number:")
num2 = st.text_input("Enter the second number:")
operation = st.radio("Select an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# if (num1!="" and num2!=""):

# Perform the calculation
if st.button("Calculate"):
    if operation == "Add":
        result = float(num1) + float(num2)
    elif operation == "Subtract":
        result = float(num1) - float(num2)
    elif operation == "Multiply":
        result = float(num1) * float(num2)
    elif operation == "Divide":
        result = float(num1) / float(num2)
    st.write("Result:", result)

import plotly.express as px

# Sample data
data = {
    'Time': [1, 2, 3, 4, 5], # 'Month': ['Jan', 'Feb', ...]
    'Value': [10, 16, 5, 11, 8] # 'Sales': [12000, 15000, ...]
}

# Create a Plotly figure
fig = px.line(data, x='Time', y='Value', title='Sample Line Chart') # x='Month', y='Sales', title='Monthly Sales Trend'

# Display the chart in Streamlit
st.plotly_chart(fig)


# Markdown
st.markdown("# This is a Heading")
st.markdown("## This is a Subheading")
st.markdown("This is a paragraph of text with **bold** and *italic* formatting.")
# HTML
st.write("<h1>This is an HTML Heading</h1>", unsafe_allow_html=True)
st.write("<p>This is a paragraph of text with <strong>bold</strong> and <em>italic</em> formatting.</p>", unsafe_allow_html=True)


# Create two columns
col1, col2 = st.columns(2)

# Add content to each column
with col1:
    st.header("Column 1")
    st.write("This is the left column.")

with col2:
    st.header("Column 2")
    st.write("This is the right column.")

# Create a widget group
with st.expander("Click to expand"):
    st.write("This content is hidden by default.")
    name1 = st.text_input("Enter your name:")
    age = st.slider("Select your age:", 0, 100, 25)
    submit_button = st.button("Submit")

# Perform actions based on user input
if submit_button:
    st.write(f"Hello, {name}! You are {age} years old.")
