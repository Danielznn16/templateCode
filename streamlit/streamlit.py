# Install `pip3 install streamlit`
# Run `streamlit run streamlit.py --server.port 8501`
# For more, check the docs for streamlit


import streamlit as st

def model_predict(input_str):
	pass
	return input_str[::-1]

input_str = st.text_area("Enter a string")
if st.button("Generate"):
	st.write("### Generated\n\n"+model_predict(input_str))