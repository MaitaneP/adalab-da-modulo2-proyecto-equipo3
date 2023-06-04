# adalab-da-modulo2-proyecto-equipo3
Este repositorio incluye el proyecto del equipo 3 del Módulo 2 de la promo D del bootcamp de Data Analytics de Adalab.

***OBJETIVO:***
Adalab nos ha contratado para analizar la información de la encuesta 2021 Kaggle DS & ML Survey. El objetivo es analizar las respuestas de la encuesta para determinar si el bootcamp de Data Analytics que ofrece se ajusta a las necesidades del mercado para un Data Analyst. Para ello analizaremos qué herramientas/competencias son las que se incluyen en el plan de estudios del bootcamp y cuales son las que según la encuesta son más necesarias para un Data Analyst.

A continuación un pequeño resumen de las competencias que se desarrrollan en el bootcamp de Adalab
    - SQL : MySQL Workbench
    - Python : VSCode
        - Pandas
        - Numpy
    - EDA, métodos de limpieza de datos
    - ETL incluyendo el uso de APIs para la extracción de datos y la carga de los datos en MySQL Workbench desde Python.
    - Visualizacion:
        - Tableau
        - Matplotlib
        - Seaborn
    - Introcucción al Machine Learning

Preguntas de investigación:
    - Herramiantas más usadas por los Data Analyst: BBDD, tratamiento de datos, visualización, etc.
    - Funciones de un Data Analyst
    - Análisis del perfil del Data Analyst: genero, edad, formación, sector, país etc. ¿Cómo afectan estas variables a los resultados?
    - Análisis según los años de experiencia
    - Análisis según sector

***PLANIFICACIÓN:***
A continuación un pequeño resumen de cómo se ha organizado el trabajo en 3 sprints:

SPRINT 1:
- Establecer working agreements
- Crear repositorio en GitHub
- Analizar la encuesta, organizar y comprender la información recogida
- Diseñar preguntas de investigación iniciales
- Crear un Jupyter Notebook para cargar los datos, realizar una primera limpieza para obtener cada dataframe con la estructura deseada
- Realizar las primeras graficas, exploración inicial dee los datos

SPRINT 2:
- Unificación y limpieza inicial de los datos en un solo dataframe
- Exploración en mayor profundidad de los datos
    - Creación de visualizaciones
- Acotamiento de las preguntas de investigación en función de los datos
    -Herramientas más utilizadas por Data Analyst en el mundo
- Crear las primeras funciones de limpieza profunda de columnas

SPRINT 3:
- Limpieza de columnas + automatización de procesos
    - Automatizamos el proceso de cambio de nombres de las columnas definiendo la función 'nombres_columnas'.
    - Continuamos automatizando y limpiando datos. Reemplazamos los valores por si y no en función de las herramientas que utiliza cada usuario.
    - Analizamos cómo separar los valores de la columnas q7, para poder hacer el conteo por usuario de cada herramienta.
        - Separamos las columnas, para poder contabilizarlas individualmente.

- Nos damos cuenta de que nuestro acercamiento de cara a la obtención de gráficas era demasiado laborioso
    - Realizamos supervisión técnica
    - Trazamos nuevo plan de limpieza y posterior análisis

- Se lleva a cabo el nuevo plan realizando el análisis estadístico y mediante gráficas solicitado, extrayendo las conclusiones pertinentes

***ORGANIZACIÓN DE LA INFORMACIÓN:***
La documentación se ha organizado en las siguientes carpetas:
- [**datos:**](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/tree/main/datos) Recoge los .csv, .txt, .xml con las respuestas a la encuesta, así como un .pdf con el detalle de las preguntas realizadas y todas las posibles respuestas de cada una.
- [**notebooks:**](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/tree/main/notebooks) Se incluyen los Jupyter Notebooks definitivos que se indican a continuuación:
    * [***1_union_datos.ipynb***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/notebooks/1_union_datos.ipynb): contiene las primeras tareas de carga de datos, una primera limpieza para obtener cada dataframe con la estructura deseada, su exploración numérica y la unión de todos los datos en un único dataframe.
    * [***2_seleccion_datos_.ipynb***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/notebooks/2_seleccion_datos.ipynb): contiene el renombrado y reordenado de las columnas, las primeras tareas de selección de los datos para el dataframe de trabajo y una exploración gráfica de dicho dataframe, así como un apartado de conclusiones.
    * [***3_tratamiento_datos.ipynb***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/notebooks/3_tratamiento_datos.ipynb): contiene el grueso de las tareas de limpieza del dataframen con la información seleccionada como relevante (preguntas seleccionadas para el perfil de Data Analyst).
    * [***4_estadistica_y_visualizacion_datos.ipynb***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/notebooks/4_estadistica_y_visualizacion_datos.ipynb): contiene el grueso de las tareas de análisis estadístico (tablas de frecuencias y de contingencia) y mediante gráficos y visualización con la información seleccionada como relevante (preguntas seleccionadas para el perfil de Data Analyst).
- [**resultados:**](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/tree/main/resultados) Se incluyen los siguientes archivos con los resultados de las tareas desarrolladas en los Jupyter Notebooks:
     * [***graficas***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/tree/main/resultados/graficas): carpeta con los .png de las gráficas generadas en el notebook 4_estadistica_y_visualizacion_datos.ipynb.
     * [***presentacion***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/tree/main/resultados/presentacion): carpeta con los .png de las gráficas para la presentacion
    * [***tablas_contingencia***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/tree/main/resultados/tablas_contingencia): carpeta con los .csv de las tablas de contingencia
    * [***tablas_frecuencias***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/tree/main/resultados/tablas_frecuencias): carpeta con los .csv de las tablas de frecuencias
    * ***df_completo_sin_tratar.csv***: archivo .csv con el dataframe completo con todas las preguntas pero sin realizar sobre él ninguna tarea de limpieza.
    * ***df_completo_ordenado.csv***: archivo .csv con el dataframe completo tan solo con las columnas homogeneizadas y ordenadas.
    * [***df_da_relevante.csv***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante.csv): archivo .csv con el dataframe de Data Analyst con las preguntas relevantes sin tratar/limpiar.
    * [***df_da_relevante_limpio.csv***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_limpio.csv): archivo .csv con el dataframe de Data Analyst con las preguntas relevantes limpio, sin explotar las preguntas que lo requieren.
    * [***df_da_relevante_limpio.pkl***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_limpio.pkl): archivo .pkl con el dataframe de Data Analyst con las preguntas relevantes limpio, sin explotar las preguntas que lo requieren.
    * [***df_da_relevante_q7_limpio.csv***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_q7_limpio.csv): archivo .csv con el dataframe de Data Analyst con la pregunta q7 y las columnas relevantes para usar como hues. Datos limpios, tras explotar la pregunta q7.
    * [***df_da_relevante_q8_limpio.csv***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_q8_limpio.csv): archivo .csv con el dataframe de Data Analyst con la pregunta q8 y las columnas relevantes para usar como hues. Datos limpios para analizar la pregunta q8.
    * [***df_da_relevante_q9_limpio.csv***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_q9_limpio.csv): archivo .csv con el dataframe de Data Analyst con la pregunta q9 y las columnas relevantes para usar como hues. Datos limpios, tras explotar la pregunta q9.
    * [***df_da_relevante_q10_limpio***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_q10_limpio.csv): archivo .csv con el dataframe de Data Analyst con la pregunta q10 y las columnas relevantes para usar como hues. Datos limpios, tras explotar la pregunta q10.
    * [***df_da_relevante_q14_limpio.csv***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_q14_limpio.csv): archivo .csv con el dataframe de Data Analyst con la pregunta q14 y las columnas relevantes para usar como hues. Datos limpios, tras explotar la pregunta q14.
    * [***df_da_relevante_q20_limpio.csv***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_q20_limpio.csv): archivo .csv con el dataframe de Data Analyst con la pregunta q20 y las columnas relevantes para usar como hues. Datos limpios, tras explotar la pregunta q20.
    * [***df_da_relevante_q24_limpio.csv***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_q24_limpio.csv): archivo .csv con el dataframe de Data Analyst con la pregunta q24 y las columnas relevantes para usar como hues. Datos limpios, tras explotar la pregunta q24.
    * [***df_da_relevante_q32_limpio.csv***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_q32_limpio.csv): archivo .csv con el dataframe de Data Analyst con la pregunta q32 y las columnas relevantes para usar como hues. Datos limpios, tras explotar la pregunta q32.
    * [***df_da_relevante_q34_limpio.csv***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_q34_limpio.csv): archivo .csv con el dataframe de Data Analyst con la pregunta q34 y las columnas relevantes para usar como hues. Datos limpios, tras explotar la pregunta q34.
    * [***df_da_relevante_q35_limpio.csv***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_q35_limpio.csv): archivo .csv con el dataframe de Data Analyst con la pregunta q35 y las columnas relevantes para usar como hues. Datos limpios para analizar la pregunta q35.
    * [***df_da_relevante_q39_limpio.csv***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_q39_limpio.csv): archivo .csv con el dataframe de Data Analyst con la pregunta q39 y las columnas relevantes para usar como hues. Datos limpios, tras explotar la pregunta q39.
    * [***df_da_relevante_q41_limpio.csv***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/resultados/df_da_relevante_q41_limpio.csv): archivo .csv con el dataframe de Data Analyst con la pregunta q41 y las columnas relevantes para usar como hues. Datos limpios, tras explotar la pregunta q41.

- **src:** Incluye los siguientes archivos:
    * [***soporte_funciones.py***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/src/soporte_funciones.py): contiene el .py usado para almacenar funciones.
    * [***soporte_variables.py***](https://github.com/MaitaneP/adalab-da-modulo2-proyecto-equipo3/blob/main/src/soporte_variables.py): contiene el .py usado para almacenar variables.