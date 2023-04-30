# EDA. Análisis exploratorio de los datos
def df_explore(dataframe, nombre):
    print(f"EXPLORACIÓN DEL DATAFRAME {nombre.upper()}")
    print("--------------")
    print(f"El dataframe {nombre} tiene {dataframe.shape[0]} filas y {dataframe.shape[1]} columnas")
    print("--------------")
    print("Las primeras 5 columnas son:")
    display(dataframe.head())
    print("Las últimas 5 columnas son:")
    display(dataframe.tail())
    print("--------------")
    print("Una muestra de dos filas seleccionadas al azar:")
    display(dataframe.sample(2))
    print("--------------")
    print(f"El dataframe {nombre} tiene las siguientes columnas:")
    for col in dataframe.columns:
        print(col) 
    print("--------------")
    print(f"Los principales estadísticos de las variables numéricas son:")
    display(dataframe.describe())
    print("--------------")
    print(f"Los principales estadísticos de las variables categóricas son:")
    display(dataframe.describe(include=object))
    print("--------------")
    print("El porcentaje de nulos por columna:")
    for i, col in enumerate(dataframe.isnull().sum()):
        print(f"{dataframe.isnull().sum().index[i]}: {col/dataframe.shape[0]*100}")
    print("--------------")
    print("El numero de valores distintos de cada columna es:")
    for col in dataframe.columns:
        if len(dataframe[col].value_counts()) > 6:
            print(col, len(dataframe[col].value_counts()))
        else:
            print(col, len(dataframe[col].value_counts()))
            print(f"Los valores son: {dataframe[col].unique()}")



# Limpieza y tratamiento de datos
def limpiar_q9(row):
    try:
        if 'Jupyter (JupyterLab, Jupyter Notebooks, etc)' in row:
            r = row.replace("Jupyter (JupyterLab, Jupyter Notebooks, etc)", 'Jupyter-JupyterLab-JupyterNotebooks')
            return r
        else:
            return row
    except:
        return row
    
def limpiar_q24(row):
    try:
        if 'Build and/or run the data infrastructure that my business uses for storing, analyzing, and operationalizing data' in row:
            r = row.replace('Build and/or run the data infrastructure that my business uses for storing, analyzing, and operationalizing data', 'Build and/or run the data infrastructure that my business uses for storing analyzing and operationalizing data')
            return r
        else:
            return row
    except:
        return row
    
def limpiar_q41a(row):
    try:
        if "Basic statistical software (Microsoft Excel, Google Sheets, etc.)" in row:
            r = row.replace("Basic statistical software (Microsoft Excel, Google Sheets, etc.)", "Basic statistical software (Microsoft Excel-Google Sheets)")
            return r
        else:
            return row
    except:
        return row
    
def limpiar_q41b(row):
    try:
        if "Local development environments (RStudio, JupyterLab, etc.)" in row:
            r = row.replace("Local development environments (RStudio, JupyterLab, etc.)", "Local development environments (RStudio-JupyterLab)")
            return r
        else:
            return row
    except:
        return row
    
def limpiar_q41c(row):
    try:
        if "Business intelligence software (Salesforce, Tableau, Spotfire, etc.)" in row:
            r = row.replace("Business intelligence software (Salesforce, Tableau, Spotfire, etc.)", "Business intelligence software (Salesforce-Tableau-Spotfire)")
            return r
        else:
            return row
    except:
        return row
    
def limpiar_q41d(row):
    try:
        if "Advanced statistical software (SPSS, SAS, etc.)" in row:
            r = row.replace("Advanced statistical software (SPSS, SAS, etc.)", "Advanced statistical software (SPSS-SAS)")
            return r
        else:
            return row
    except:
        return row

def limpiar_q41e(row):
    try:
        if "Cloud-based data software & APIs (AWS, GCP, Azure, etc.)" in row:
            r = row.replace("Cloud-based data software & APIs (AWS, GCP, Azure, etc.)", "Cloud-based data software & APIs (AWS-GCP-Azure)")
            return r
        else:
            return row
    except:
        return row
    