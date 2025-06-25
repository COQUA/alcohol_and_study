# Efectos del alcohol en el estudio

## Descripción
Este proyecto analiza cómo el consumo de alcohol afecta el rendimiento académico de los estudiantes, utilizando un dataset de Kaggle (“Alcohol Effects On Study”) y un modelo de regresión lineal implementado con Scikit-Learn. Además, ofrece una API con FastAPI para predecir la nota final (G3) a partir de variables de entrada.

## Requisitos

- Python 3.8+
- pip
- Virtualenv o conda
- Node.js y npm (si aplica para frontend)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/COQUA/alcohol_and_study.git
   cd alcohol_and_study
   ```
2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. (Opcional) Instala dependencias de frontend:
   ```bash
   cd frontend
   npm install
   ```

## Estructura del proyecto

```
data/           # Dataset original en CSV
notebooks/      # Jupyter notebooks para EDA y entrenamiento
models/         # Modelos entrenados (.pkl)
app.py          # Servidor FastAPI
requirements.txt
frontend/       # Código del cliente web (opcional)
README.md
```

## Ejecución

### 1. Entrenamiento y análisis exploratorio
Ejecuta el notebook:
```bash
jupyter notebook notebooks/analysis.ipynb
```
Revisa celda a celda y ejecuta para reproducir el pre-procesamiento y entrenamiento. El modelo se guarda en `models/model.pkl`.

### 2. Levantar la API
Con el entorno virtual activado:
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```
La API estará disponible en `http://localhost:8000`.

### 3. Interfaz de usuario (Frontend)
```bash
cd frontend
npm run dev
```
Abre tu navegador en `http://localhost:3000` y completa el formulario.

## Uso de la API

Envía un POST a `/predict` con JSON:
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
Respuesta:
```json
{
  "predicted_grade": 14.2
}
```

## Interpretación de los parámetros

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
| traveltime  | Tiempo de viaje a la escuela (1:<15min, 2:15–30min, 3:30min–1h, 4:>1h)                             |
| studytime   | Tiempo de estudio semanal (1:<2h, 2:2–5h, 3:5–10h, 4:>10h)                                         |
| failures    | Número de asignaturas reprobadas anteriormente                                                     |
| schoolsup   | Apoyo educativo extra (“yes”/“no”)                                                                 |
| famsup      | Apoyo familiar (“yes”/“no”)                                                                        |
| paid        | Clases pagadas extra-curriculares (“yes”/“no”)                                                    |
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
- Incrementar `studytime` suele aumentar `G3`.  
- Aumentar `failures`, `Dalc` o `Walc` suele reducir `G3`.  

## Licencia

MIT
