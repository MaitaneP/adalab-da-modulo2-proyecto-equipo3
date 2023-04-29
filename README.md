# promo-d-da-modulo2-proyecto-equipo3-Maitane-Elisa-Paula-Paloma
Este repositorio incluye el proyecto del equipo 3 del Módulo 2 de la promo D del bootcamp de Data Analytics de Adalab. El nombre del equipo es RKG (Restart Kernel Girls) y las integrantes son Elisa Jiménez, Paula Velasco, Paloma Mesón y Maitane Portilla.

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

***ORGANIZACIÓN DE LA INFORMACIÓN:***
La documentación se ha organizado en las siguientes carpetas:
- [**datos:**]() Recoge los .csv, .txt, .xml con las respuestas a la encuesta, así como un .pdf con el detalle de las preguntas realizadas y todas las posibles respuestas de cada una.
- [**trabajo:**]() Carpeta de trabajo.
- **notebooks:** Se incluyen los Jupyter Notebooks definitivos que se indican a continuuación:
    * [***.ipynb***](): contiene las tareas de .
- **resultados:** Se incluyen los siguientes archivos con los resultados de las tareas desarrolladas en los Jupyter Notebooks:
    * [***df_completo_sin_tratar.csv***](): archivo .csv con el dataframe completo con todas las preguntas pero sin realizar sobre él ninguna tarea de limpieza.
    * [***df_completo_ordenado.csv***](): archivo .csv con el dataframe completo tan solo con las columnas homogeneizadas y ordenadas.
    * [***.ipynb***](): contiene
- **src:** Incluye los siguientes archivos:
    * [***soporte_funciones.py***](): contiene el .py usado para almacenar funciones.
    * [***soporte_variables.py***](): contiene el .py usado para almacenar variables.
