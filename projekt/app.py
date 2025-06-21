import stremlit as st
import requests
import pandas as  pd

st.title("Project Management App")

st.header("Add a Developer")

dev_name = st.text_input("Developer Name")
dev_experience = st.number_input("Experience (Years)", min_value=0, max_value=50, value=0)

if sy.button("Create Developer"):
    dev_data = {"name": dev_name, "experience": dev_experience}
    response = requests.post(" https://localhost:8000/developers", json=dev_data)
    st.json(response.json())

    st.header("add a project")
    proj_title = st.text_input("Project Title")
    proj_desc = st.text_area("Project Description")
    proj_lang = st.text_input("Languages Used (Coma-separated)")
    lead_dev_name = st.text_input("Lead Developer Name")
    lead_dev_exp = st.number_input("lead Developer Experience (Years)", min_value=0, max_value=50, value=0)

    response = requests.post("https://localhost:8000/projects/", json=proj_data)
    st.json(response.json())
st.header("Project Dashboard")
if st.button("get project"):
