# 🎬 Proyecto: ¿popular o bien valorada?
        Qué hace realmente que una película funcione

### Objetivo del proyecto
El objetivo de este proyecto es analizar qué factores influyen en el rendimiento de una película, diferenciando entre dos conceptos:
    - Popularidad → qué tanto se consume o llama la atención una película
    - Valoración → qué tan bien es valorada por el público
La idea principal es entender si las películas más populares son también las mejor valoradas, o si son dos cosas distintas.

### Dataset utilizados
El dataset proviene de dos fuentes pública de datos de películas:

1. TMDB Movie Dataset (Kaggle)

Se ha utilizado como base principal del análisis. Contiene información de miles de películas con datos como:

    - título género 

    - presupuesto 

    - popularidad 

    - valoración media (TMDB)

    - número de votos 

    - fecha de estreno


2. OMDb API (datos externos de películas)

Se ha utilizado para enriquecer el dataset con información adicional: 

    - valoración IMDb 

    - número de votos en IMDb 

    - director 

    - año de estreno


### Hipotesis
1. El género influye en popularidad y valoración

    Se analiza si ciertos géneros destacan más en popularidad o en calidad percibida.

2. El presupuesto influye más en popularidad que en valoración

    Se estudia si las películas más caras son más visibles, pero no necesariamente mejor valoradas.

3. Popularidad no siempre está relacionada con la valoración

    Se analiza si una película muy popular también está bien valorada.

4. IMDb y TMDB pueden ofrecer valoraciones diferentes

    Se comparan dos sistemas de valoración diferentes.

5. Las películas recientes tienden a ser más populares

    Se analiza si el paso del tiempo afecta a la popularidad y valoración.

---

### Proceso de análisis
- Análisis exploratorio de datos (EDA) para entender la estructura del dataset
    - Revisión de variables numéricas y categóricas
    - Detección de valores nulos o inconsistencias
    - Análisis de distribución de variables como popularidad, presupuesto y valoraciones
    - Identificación de patrones iniciales entre variables
- Recolección de datos:

    - Se cargó un dataset de peliculas desde Kaggle.
    - Se obtuvieron datos adicionales mediante API.
- Limpieza y transformación de datos en Python (Pandas)

    - Eliminación de nulos y duplicados
    - Conversión de tipos de datos
    - Procesamiento de campos de texto (géneros, números, etc.)
- Integración de datos externos mediante API

    - Añadidos datos de IMDb (rating, votos)
    - Información de director y año
    - Unión con el dataset principal
- Análisis de datos

Durante el análisis se han estudiado los siguientes aspectos:
     - Géneros
        - Géneros más frecuentes
        - Relación con popularidad, valoración y presupuesto
    - Valoraciones
        - Comparación entre TMDB e IMDb
        - Relación entre valoración y popularidad
    - Presupuesto
        - Relación con género, popularidad y valoración
    - Popularidad
        - Películas más populares
        - Relación con valoración
    - API (IMDb)
        - Comparación IMDb vs TMDB
        - Número de votos, director y año de estreno




###  KPIs calculados
Durante el análisis se han definido indicadores clave para entender mejor el dataset:
    
    - Número total de películas analizadas
    - Popularidad media por género
    - Valoración media por género (TMDB e IMDb)
    - Presupuesto medio por género
    - Diferencia entre popularidad y valoración
    - Distribución de películas por año

### Métricas clave usadas
Para el análisis se han utilizado operaciones básicas de agrupación y cálculo:

COUNT() → para contar películas

AVG() → para calcular medias (rating, presupuesto, popularidad, votos)

MIN / MAX → para ver valores extremos

GROUP BY → para agrupar por género o año

JOIN → para unir datos del dataset con la API (OMDb)

Operaciones de limpieza en Pandas → para preparar y estructurar los datos


---

## Resultados / Insights (hallagoz más importanes, claros y accionables)
(Completar después del análisis, ejemplo de cómo quedará)

Los géneros de acción y aventura son los más populares

Documentales y dramas suelen tener mejores valoraciones

La popularidad no siempre implica mejor valoración

El presupuesto influye más en visibilidad que en calidad percibida

TMDB y IMDb no siempre coinciden

### Conclusiones
La popularidad y la valoración no siempre van de la mano.

Una película puede ser muy vista pero no estar bien valorada, o tener buenas valoraciones sin ser muy popular.

Esto ayuda a entender que el rendimiento de una película depende de diferentes factores y no de uno solo.

---

### Próximos pasos (qué extenderias si tuvieras más datos o más tiempo)
Si se quisiera ampliar el análisis, se podrían realizar las siguientes mejoras:

- Analizar evolución temporal de popularidad y valoración
- Analizar tendencias por década o evolución del cine en el tiempo
- Incorporar más fuentes de datos externas


---

### Cómo replicar el proyecto 
1. Clonar el repositorio
2. Descargar el dataset desde Kaggle (TMDB Movie Dataset)
3. Obtener una API key de OMDb API
4. Ejecutar el notebook (.ipynb)
5. Revisar el análisis y visualizaciones

### Presentación
Añadir