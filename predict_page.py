import streamlit as st
import pickle
import numpy as np


def load_module():
    with open('./Trainer/saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_module()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Prediccion del salario de un desarrollador de software")

    st.write("""### Ingresa la informacion del salario que deseas predecir""")

    countries =[    
    "United States",
    "India",
    "United Kingdom",
    "Germany",
    "Canada",
    "Brazil",
    "France",
    "Spain",
    "Australia",
    "Netherlands",
    "Poland",
    "Italy",
    "Russian Federation",
    "Sweden",
    ]
    
    education_levels=[
    "Less than a Bachelors", # Tecnicatura
    "Bachelor’s degree", #Licenciatura
    "Master’s degree",
    "Post grad",
    ]

    country = st.selectbox("Países", countries)
    education = st.selectbox("Nivel de educación", education_levels)

    expericence = st.slider("Años de experiencia", 0, 50, 3)

    ok = st.button("Calcular el salario")
    if ok:
        X = np.array([[country, education, expericence ]])
        X[0, 0] = le_country.transform([X[0, 0]])[0]
        X[0, 1] = le_education.transform([X[0, 1]])[0] #convertir las variables texto a números

        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
    if not ok:
        st.info("Por favor, completa los datos y presiona 'Calculate Salary'.")
