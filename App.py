import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import time
from data.meal_plans import get_meal_plan_data
from data.breathing_exercises import get_breathing_exercises_data
from utils.nutrition_calculator import calculate_daily_nutrition, get_nutrition_summary

# Configure page
st.set_page_config(
    page_title="30-Day Diet & Wellness Plan",
    page_icon="🥗",
    layout="wide"
)

# Initialize session state
if 'current_day' not in st.session_state:
    st.session_state.current_day = 1
if 'completed_days' not in st.session_state:
    st.session_state.completed_days = set()
if 'start_date' not in st.session_state:
    st.session_state.start_date = datetime.now()
if 'show_welcome' not in st.session_state:
    st.session_state.show_welcome = True

# Load data
@st.cache_data
def load_meal_data():
    return get_meal_plan_data()

@st.
