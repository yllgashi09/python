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
    response = requests.get("https://localhost:8000/projects/")
    project_data = response.json()['projects']
    if project_data:
        project_df = pd.dataframe(project_data)

        st.subheader("Project Overview")
        st.dataframe(projects_df)

        st.subheader("Project Overview")
        for project in project_data:
            st.markdown(f"**title:** {project['title']}")
            st.markdown(f"**Description:** {project['Description']}")
            st.markdown(f"**language:** {', '.join['language']}")
            st.markdown(f"**lead developer:** {project['lead developer']['name']}with {project['lead_developer']['experience']}years of experience")
            st.markdown(f"---")
        else:
            st.warning('no project found.')


