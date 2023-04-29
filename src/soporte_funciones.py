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