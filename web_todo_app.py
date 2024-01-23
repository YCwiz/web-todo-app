"""this main contains all the main logic related to the app.

streamlit - module that allows to create web app
objects - module that contains all classes
supp_funcs - contains support functions and logic
"""
import streamlit as st
from objects import *
from supp_funcs import *

"""Head of web page."""
st.title("My Todo App")
st.subheader("Easy to use Task Manager")
st.write("This is to increase my productivity")

"""Fuction that stores new tasks to database."""
def add_to_db_tb() :
    new_task = st.session_state["new_task"]
    new_task = Task(new_task)
    db = CRUD()
    db.add_to_db(new_task)

"""Retrieves list of tasks from database"""
tasks = view_tasks()

"""Renders all tasks in list as checkboxes."""
for task in tasks :

    complete = st.checkbox(task, key=task)

    if complete :
        """When user clicks check box task gets removed and page refreshed."""
        remove_from_db_cb(task)
        st.rerun()

"""Input box widget add new tasks."""
st.text_input(label="Enter a todo :", 
            on_change=add_to_db_tb,
            key="new_task")
