# Efectos del alcohol en el rendimiento academico

## Descripción
Este proyecto analiza cómo el consumo de alcohol afecta el rendimiento académico de los estudiantes, utilizando un dataset de Kaggle (“Alcohol Effects On Study”) y un modelo de regresión lineal implementado con Scikit-Learn. Además, ofrece una API con FastAPI para predecir la nota final (G3) a partir de variables de entrada, y un cliente web React para interactuar con el modelo.

## Requisitos

- Python 3.8+  
- pip  
- Virtualenv o conda  
- Node.js (v14+) y npm o yarn  

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/COQUA/alcohol_and_study.git
   cd alcohol_and_study
   ```
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   ```
3. Instala dependencias backend:
   ```bash
   pip install -r requirements.txt
   ```
4. Instala dependencias del cliente web:
   ```bash
   cd client
   npm install    # o yarn install
   ```
5. Vuelve al directorio raíz si es necesario:
   ```bash
   cd ..
   ```

## Estructura del proyecto

```
data/           # Dataset original en CSV
notebooks/      # Jupyter notebooks para EDA y entrenamiento
models/         # Modelos entrenados (.pkl)
client/         # Aplicación React del frontend
app.py          # Servidor FastAPI
requirements.txt
README.md
```

## Ejecución

### 1. Entrenar y explorar datos
Ejecuta el notebook de análisis y entrenamiento:
```bash
jupyter notebook notebooks/analysis.ipynb
```
El modelo resultante se guardará en `models/model.pkl`.

### 2. Iniciar API (Backend)
Con el entorno virtual activado, ejecuta:
```bash
python -m uvicorn main:app --reload
```
La API estará disponible en `http://localhost:8000`.

### 3. Iniciar cliente web (Frontend React)
En otra terminal:
```bash
cd client
npm install  # Solo la primera vez
npm start
```
Abre tu navegador en `http://localhost:3000`.

## Uso de la API

Envía un POST a `http://localhost:8000/predict` con un JSON similar a:
```json
{
  "school": "GP",
  "sex": "F",
  "age": 17,
  "address": "U",
  "famsize": "GT3",
  "Pstatus": "T",
  "Medu": 3,
  "Fedu": 2,
  "Mjob": "at_home",
  "Fjob": "services",
  "reason": "course",
  "guardian": "mother",
  "traveltime": 1,
  "studytime": 2,
  "failures": 0,
  "schoolsup": "no",
  "famsup": "yes",
  "paid": "no",
  "activities": "yes",
  "nursery": "yes",
  "higher": "yes",
  "internet": "yes",
  "romantic": "no",
  "famrel": 4,
  "freetime": 3,
  "goout": 3,
  "Dalc": 1,
  "Walc": 2,
  "health": 3,
  "absences": 4,
  "G1": 12,
  "G2": 13
}
```

Respuesta de ejemplo:
```json
{
  "predicted_grade": 14.2
}
```

## Interpretación de parámetros

| Parámetro   | Descripción                                                                                       |
|-------------|---------------------------------------------------------------------------------------------------|
| school      | Escuela (“GP” - Gabriel Pereira, “MS” - Mousinho da Silveira)                                      |
| sex         | Sexo (“F” - femenino, “M” - masculino)                                                            |
| age         | Edad del estudiante (15–22)                                                                        |
| address     | Tipo de vivienda (“U” - urbano, “R” - rural)                                                      |
| famsize     | Tamaño familiar (“LE3” ≤3, “GT3” >3)                                                              |
| Pstatus     | Estado civil de los padres (“T” - juntos, “A” - separados)                                        |
| Medu, Fedu  | Nivel de educación de madre/padre (0=nada, 1=primaria, 2=secundaria, 3=grado, 4=máster)           |
| Mjob, Fjob  | Trabajo de madre/padre                                                                             |
| reason      | Razón para elegir la escuela (“home”, “reputation”, “course”, “other”)                            |
| guardian    | Tutor (“mother”, “father”, “other”)                                                               |
| traveltime  | Tiempo de viaje a la escuela (1:<15 min, 2:15–30 min, 3:30 min–1 h, 4:>1 h)                       |
| studytime   | Tiempo de estudio semanal (1:<2 h, 2:2–5 h, 3:5–10 h, 4:>10 h)                                     |
| failures    | Número de asignaturas reprobadas anteriormente                                                     |
| schoolsup   | Apoyo educativo extra (“yes”/“no”)                                                                 |
| famsup      | Apoyo familiar (“yes”/“no”)                                                                        |
| paid        | Clases pagadas extracurriculares (“yes”/“no”)                                                     |
| activities  | Actividades extracurriculares (“yes”/“no”)                                                         |
| nursery     | Educación preescolar (“yes”/“no”)                                                                  |
| higher      | Deseo de educación superior (“yes”/“no”)                                                           |
| internet    | Acceso a internet en casa (“yes”/“no”)                                                             |
| romantic    | Relación de pareja (“yes”/“no”)                                                                    |
| famrel      | Calidad de la relación familiar (1=muy mala–5=excelente)                                           |
| freetime    | Tiempo libre después de la escuela (1=muy bajo–5=muy alto)                                         |
| goout       | Frecuencia de salir con amigos (1=muy bajo–5=muy alto)                                             |
| Dalc        | Consumo de alcohol días de semana (1=bajo–5=alto)                                                  |
| Walc        | Consumo de alcohol fines de semana (1=bajo–5=alto)                                                |
| health      | Estado de salud (1=muy mala–5=muy buena)                                                           |
| absences    | Ausencias escolares (número de días)                                                               |
| G1, G2      | Notas de los dos primeros periodos (0–20)                                                          |

## Interpretación de resultados

El modelo predice **G3**, la nota final (0–20). Un valor mayor indica mejor rendimiento académico.

### Categorías de desempeño (G3)
- **0–5**: Muy bajo rendimiento  
- **6–10**: Rendimiento bajo  
- **11–15**: Rendimiento medio  
- **16–20**: Rendimiento alto  

### Influencia de variables clave
- **studytime** (Tiempo de estudio) 
  - 1 (<2 h/sem): Insuficiente  
  - 2 (2–5 h/sem): Moderado  
  - 3 (5–10 h/sem): Adecuado  
  - 4 (>10 h/sem): Intensivo  
- **Dalc / Walc** (Consumo de alcohol)  
  - 1: Muy bajo  
  - 2: Bajo  
  - 3: Moderado  
  - 4: Alto  
  - 5: Muy alto  
- **failures** (Reprobaciones previas)  
  - 0: Sin reprobaciones  
  - 1–2: Pocas reprobaciones  
  - ≥3: Varias reprobaciones  
- **absences** (Ausencias)  
  - 0–5: Excelente  
  - 6–10: Pocas  
  - 11–20: Moderadas  
  - >20: Frecuentes  

Con estos rangos, el usuario puede ajustar valores desde el cliente y anticipar cómo afectan la predicción de G3.


## Licencia

MIT
