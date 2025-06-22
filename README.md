
# Proyecto: Predicción de Salario de Desarrolladores

Este proyecto utiliza datos de la encuesta de Stack Overflow para predecir el salario anual de desarrolladores de software en función de su país, nivel educativo y años de experiencia.

## 🧠 ¿Qué hace este proyecto?

Entrena un modelo de machine learning para estimar el salario de un desarrollador según tres variables clave:

- País de residencia
- Nivel educativo
- Años de experiencia

Luego, se implementa una interfaz sencilla usando **Streamlit** para que cualquier usuario pueda ingresar sus datos y obtener una predicción inmediata.

## 🌐 Ver la aplicación online

[![Render](https://img.shields.io/badge/Vercel-Ver%20App-black?logo=render)](https://salary-predict.onrender.com/)

---

## 📂 Estructura del Proyecto

```
TRABAJO-EVALUATIVO/
│
├── Trainer/
│   ├── model.ipynb                
│   ├── model_comentado.ipynb     
│   ├── saved_steps.pkl           
│
├── app.py                        
├── predict_page.py              
├── survey_results_public.csv    
                     
```

## 🚀 ¿Cómo ejecutarlo?

1. Clona el repositorio:

```bash
git clone https://github.com/Ticii18/Practical-Evaluative-Machine-Learning
cd Practical-Evaluative-Machine-Learning
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

1. Ejecutá la aplicación:

```bash
streamlit run app.py
```

## 🧪 Tecnologías utilizadas

- Python 3
- Streamlit
- NumPy
- scikit-learn
- Pandas
- Pickle

## 📊 Datos

Los datos provienen de la encuesta anual de desarrolladores de Stack Overflow.


## ✨ Autores

- Ticiano Vera
- Riquelme Alan [![GitHub](https://img.shields.io/badge/GitHub-Perfil-black?logo=github)](https://github.com/AlanRik20)

---


