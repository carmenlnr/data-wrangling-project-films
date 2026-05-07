# 🎬 Proyecto: ¿popular o bien valorada?
        Qué hace realmente que una película funcione

### Problema de negocio

En la industria del cine es importante entender qué factores influyen en el éxito de una película.

Este proyecto analiza si el éxito depende principalmente de la popularidad, la valoración o de otros factores como el género, el presupuesto y el momento de estreno.

El objetivo no es únicamente comparar métricas, sino entender cómo interactúan entre sí para definir el rendimiento de una película.


### Objetivo del proyecto

El objetivo de este proyecto es analizar qué factores influyen en el rendimiento de una película desde un enfoque multidimensional, estudiando relaciones entre variables como:
- Popularidad → nivel de consumo o visibilidad de una película
- Valoración → percepción de calidad por parte del público
- Género → tipo de contenido cinematográfico
- Presupuesto → nivel de inversión en la producción
- Año de estreno → impacto del contexto temporal

La idea principal es determinar si el éxito de una película puede explicarse mediante una única métrica o si depende de múltiples factores combinados.

### Dataset utilizados
El dataset proviene de dos fuentes pública de datos de películas:

1. TMDB Movie Dataset (Kaggle)

Dataset principal que contiene información de miles de películas con variables como:
    - título 
    - género 
    - presupuesto 
    - popularidad 
    - valoración media (TMDB)
    - número de votos 
    - fecha de estreno


2. OMDb API (datos externos de películas)

Se ha utilizado para enriquecer el dataset con información adicional: 
    - valoración OMDb 
    - número de votos  
    - director 
    - año de estreno


### Hipotesis
1. El género influye en popularidad y valoración

    Se analiza si ciertos géneros destacan más en popularidad o en calidad percibida.

2. El presupuesto influye más en popularidad que en valoración

    Se estudia si las películas más caras son más visibles, pero no necesariamente mejor valoradas.

3. Popularidad no siempre está relacionada con la valoración

    Se analiza si una película muy popular también está bien valorada.

4. OMDb y TMDB pueden ofrecer valoraciones diferentes

    Se comparan dos sistemas de valoración diferentes.

5. Las películas recientes tienden a ser más populares

    Se analiza si el paso del tiempo afecta a la popularidad y valoración.

---

### Proceso de análisis

- Análisis exploratorio de datos (EDA) para comprender la estructura del dataset
- Limpieza y transformación de datos en Python (Pandas)
- Tratamiento de valores nulos, duplicados y tipos de datos
- Procesamiento de variables categóricas como géneros
- Integración de datos externos mediante la API de OMDb
- Análisis de relaciones entre variables
- Estudio de patrones en popularidad, valoración, presupuesto y género

###  KPIs calculados
Durante el análisis se han definido indicadores clave para entender mejor el dataset:
    
    - Número total de películas analizadas
    - Popularidad media por género
    - Valoración media por género (TMDB e OMDb)
    - Presupuesto medio por género
    - Correlación entre popularidad y valoración
    - Diferencia entre IMDb y TMDB
    - Evolución de popularidad por año

### Métricas clave usadas
Para el análisis se han utilizado operaciones básicas de agrupación y cálculo en Pandas;

    - COUNT() → para contar el número de películas y frecuencias por género
    - MEAN() / AVG() → para calcular medias de valoración (TMDB e OMDb), popularidad y presupuesto
    - MIN / MAX → para identificar valores extremos en popularidad y ratings
    - GROUP BY → para agrupar datos por género y año
    - EXPLODE() → para trabajar correctamente con géneros múltiples por película
    - JOIN / MERGE → para unir el dataset principal con los datos obtenidos desde la API de OMDb (IMDb)
    -  Transformación de fechas → para extraer el año de estreno desde release_date
    - Cálculo de diferencias → para comparar OMDb vs TMDB (rating_diff)
    - Limpieza de datos → tratamiento de nulos, tipos de datos 


---

## Resultados / Insights 
- Los géneros de acción, aventura y ciencia ficción son los más populares, asociados a grandes producciones y mayor visibilidad.
- Géneros como documental, foreign o TV movie presentan baja popularidad, pero no necesariamente peor valoración.
- La valoración media entre géneros es bastante estable (aprox. entre 5.6 y 6.7), sin grandes diferencias entre tipos de película.
- La popularidad no está directamente relacionada con la valoración (correlación ≈ 0.27), lo que indica que son métricas independientes.
- OMDb presenta valoraciones ligeramente superiores a TMDB, aunque ambas plataformas siguen patrones similares.
- Las películas recientes tienden a ser más populares, influenciadas por factores como marketing, franquicias y distribución actual.

### Conclusiones

El análisis muestra que el éxito de una película no depende de una única variable, sino de la interacción entre varios factores como presupuesto, género, popularidad y sistema de valoración.

Se observa que:

- La popularidad y la valoración son métricas diferentes y no están fuertemente relacionadas.
- El género influye en la visibilidad, pero no determina la calidad percibida.
- El presupuesto afecta más a la exposición que a la valoración.
- El rendimiento de una película depende de múltiples factores combinados.
- Las distintas plataformas de valoración reflejan tendencias similares pero no idénticas.

En conclusión, no existe una única métrica que defina el “éxito” de una película, sino distintas perspectivas que pueden llevar a interpretaciones diferentes.

---

### Próximos pasos (qué extenderias si tuvieras más datos o más tiempo)
Si se quisiera ampliar el análisis, se podrían realizar las siguientes mejoras:

- Análisis de evolución temporal más detallado por décadas
- Estudio de tendencias de género a lo largo del tiempo
- Incorporación de más variables externas como premios o ingresos

---

### Cómo replicar el proyecto 
1. Clonar el repositorio
2. Descargar el dataset desde Kaggle (TMDB Movie Dataset)
3. Obtener una API key de OMDb API
4. Ejecutar el notebook (.ipynb)
5. Revisar el análisis y visualizaciones

### Presentación
https://docs.google.com/presentation/d/1McwCbpji0oNhfmi7BLYgZ_BdR9XNlK8cQ681B_qMk6I/edit?slide=id.p#slide=id.p
