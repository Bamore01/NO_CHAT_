import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import altair as alt
import time
import zipfile

from base import retrieval

# Page title
st.set_page_config(page_title='Retrieval Augmentation Generation', page_icon='🤖')
st.title('🤖 Retrieval Augmentation Generation')

with st.form('Generation Form'):
    answer = st.text_input(label='Introduce tu pregunta:', placeholder='Por favor, introduce una pregunta')
    submitted = st.form_submit_button('Preguntar')

    if submitted:
        if answer:
            with st.spinner(f"Generando respuestas..."):
                answer = str(answer)
                answer = f'"{answer}"'
                st.write(answer)
                output = retrieval(answer)
            st.write('Generated Question(s):')
            st.text_area("Response", value=output)
    else:
        st.error('Please, provide a context to generate questions from')
