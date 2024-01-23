"""Module that contains supporting logic and functions.

objects - module that contain task and CRUD objects
streamlit - module to allow creation of web app
"""
from objects import *
import streamlit as st

def view_tasks() :
    """Renders list of tasks that is stored in database and returns it.
    
    CRUD - object/class to help with the database management
    db - instance of CRUD
    list_of_tasks - stores the tasks in a list
    tasks - stores tasks as tuples from database
    """
    db = CRUD()
    list_of_tasks = []
    tasks = db.read_from_db()
    for name, complete in tasks :
        """Unpacks tuple and store it as list."""
        task = Task(name, complete)
        list_of_tasks.append(task.name)

    return list_of_tasks

def remove_from_db_cb(task) :
    """Function allows a task to be removed from database.
    
    old_task - instance of Task object
    db - instance object that handles database management
    remove_from_db - method that removes a task from the database
    """
    old_task = Task(task)
    db = CRUD()
    db.remove_from_db(old_task)
