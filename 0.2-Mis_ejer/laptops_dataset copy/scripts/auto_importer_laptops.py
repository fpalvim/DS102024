import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


# 1.1 Inspección Inicial

class AutoImporter:
    """
    Clase para inspeccionar y analizar un dataframe utilizando pandas 

    Attributes:
        df (pandas.DataFrame): El dataframe a inspeccionar.
    """

    def __init__(self, df):
        """
        Inicializa la instancia con el dataframe proporcionado.

        Args:
            df (pandas.DataFrame): El marco de datos a inspeccionar.
        """
        self.df = df

    def inspeccion_inicial(self):
        """
        Inspecciona el dataframe y imprime los resultados.
        """
    # Tamaño y estructura de los datos
        print("=== TAMAÑO Y ESTRUCTURA DE LOS DATOS ===")
        print(f"Número total de registros: {self.df.shape[0]}")
        print(f"Número de columnas: {self.df.shape[1]}")
        print(f"Uso de memoria: {self.df.memory_usage().sum() / 1024:.2f} KB")
        print("\n")

    # Tipos de datos y nombres de columnas
        print("=== TIPOS DE DATOS Y NOMBRES DE COLUMNAS ===")
        print(self.df.dtypes)
        print("\n")
        print("Información detallada del DataFrame:")
        print(self.df.info())
        print("\n")

    # Identificación de problemas iniciales
        print("=== IDENTIFICACIÓN DE PROBLEMAS INICIALES ===")
        print(f"Número de filas duplicadas: {self.df.duplicated().sum()}")
        print("\nValores nulos por columna:")
        print(self.df.isnull().sum())
        print("\nValores nulos relativos por columna:")
        print(round(self.df.isnull().sum() / len(self.df) * 100),2)

    # Mostrar las primeras filas para verificar la estructura
        print("\nPrimeras filas del dataset:")
        print(self.df.head())


class DataFrameDescriber:
    """
    Clase para analizar y describir un dataframe, separando datos numéricos y no numéricos.

    Attributes:
        df (pandas.DataFrame): El dataframe a inspeccionar.
    """

    def __init__(self, df):
        """
        Inicializa la instancia con el dataframe proporcionado.

        Args:
            df (pandas.DataFrame): El marco de datos a inspeccionar.
        """
        self.df = df
        self.numeric_cols = self.df.select_dtypes(include=['number'])
        self.non_numeric_cols = self.df.select_dtypes(exclude=['number'])

    def describe_numerico(self):
        """
        Genera un análisis descriptivo de las columnas numéricas.

        Returns:
            pandas.DataFrame: Descripción de las columnas numéricas.
        """
        return self.numeric_cols.describe()

    def describe_categorico(self):
        """
        Genera un análisis descriptivo de las columnas no numéricas.

        Returns:
            pandas.DataFrame: Descripción de las columnas no numéricas.
        """
        return self.non_numeric_cols.describe(include='all')
    


class CompleteDescribeTable:
    def __init__(self, df):
        self.df = df
        self.resumen = []

    def describe_complete(self):
        for columna in self.df.columns:
            data = self.df[columna]
            tipo_dato = data.dtype

            if tipo_dato in ['float64', 'int64']:
                var_tipo = 'numerica'
                card_absoluta = data.nunique()
                card_relativa = (data.nunique() / len(self.df)) * 100
                missing_pct = round(data.isnull().mean() * 100, 2)
                rango = (data.min(), data.max())
                moda = data.mode()[0] if not data.mode().empty else np.nan
                mean_val = data.mean()
                median_val = data.median()
                skew_val = data.skew()
                kurtosis_val = data.kurtosis()
                std_deviation_val = data.std()
                asimetria = 'positiva' if moda < median_val < mean_val else ('simetrica' if mean_val == median_val == moda else 'negativa')
                # Shapiro test
                stat_, p_ = stats.shapiro(data) if len(data) > 3 else (np.nan, np.nan)
                normal_test = 'No normal' if p_ < 0.05 else 'Normal'
                dist = 'No Gaussiana' if p_ < 0.05 else 'Gaussiana'
                # calculo de outliers
                Q1 = data.quantile(0.25)
                Q3 = data.quantile(0.75)
                IQR = Q3 - Q1
                limite_inferior = Q1 - 1.5 * IQR
                limite_superior = Q3 + 1.5 * IQR
                outliers = (data < limite_inferior) | (data > limite_superior)
                outliers_pct = round((outliers.sum() / len(data)) * 100, 2)
                self.resumen.append([columna, tipo_dato, var_tipo, card_absoluta, card_relativa, dist, missing_pct, outliers_pct, rango, moda, median_val, mean_val, std_deviation_val, Q1, Q3, skew_val, kurtosis_val, stat_, p_, normal_test, asimetria])
            else:
                var_tipo = 'categorica'
                card_absoluta = data.nunique()
                card_relativa = (data.nunique() / len(self.df)) * 100
                # Para categoricas no se aplica normalidad
                missing_pct = round(data.isnull().mean() * 100, 2)
                self.resumen.append([columna, tipo_dato, var_tipo, card_absoluta, card_relativa, None, missing_pct, None, None, None, None, None, None, None, None, None, None])

    def get_describe_complete(self):
        resumen_df = pd.DataFrame(self.resumen, columns=['variable', 'tipo de dato', 'tipo de variable', 'cardinalidad abs' ,'cardinalidad %', 'distribucion', '% missing', '% Outliers', 'rango', 'moda', 'mediana', 'media', 'desv estandar', 'Q1','Q3', 'asimetria', 'curtosis', 'Valor estad.' , 'Valor de P', 'prueba normalidad', 'tipo asimetria']).set_index('variable')
        return resumen_df


class AutoPlot:
    def __init__(self):
        self.numeric_plots = ['hist', 'boxplot', 'kde']
        self.categorical_plots = ['countplot', 'barplot']
        self.bivariate_plots = {
            ('numeric', 'numeric'): 'scatterplot',
            ('numeric', 'categorical'): 'boxplot',
            ('categorical', 'categorical'): 'countplot'
        }

    def univariate_plot(self, data, variable, type):
        if type in ['continuo', 'discreto']:
            sns.histplot(data=data, x=variable, kde=True)
        elif type == 'nominal' or type == 'ordinal':
            sns.countplot(data=data, x=variable)
        plt.title(f'Distribución de {variable}')
        plt.show()

    def bivariate_plot(self, data, variables, types):
        plot_type = self.bivariate_plots.get((types[0], types[1]), None)
        if plot_type == 'scatterplot':
            sns.scatterplot(data=data, x=variables[0], y=variables[1])
        elif plot_type == 'boxplot':
            sns.boxplot(data=data, x=variables[1], y=variables[0]) 
        elif plot_type == 'countplot':
            sns.countplot(data=data, x=variables[0], hue=variables[1])
        plt.title(f'Relación entre {variables[0]} y {variables[1]}')
        plt.show()

    def multivariate_plot(self, data, variables, types):
        # Para gráficos multivariados, se pueden considerar:
        # - Pair plots (sns.pairplot) para explorar relaciones entre todas las variables numéricas
        # - Heatmaps para visualizar correlaciones
        # - Gráficos 3D (si se tienen 3 variables numéricas)
        # - Gráficos de agrupamiento (si se tiene una variable categórica)
        # ...

        # Aquí puedes implementar diferentes tipos de gráficos multivariados
        # según tus necesidades específicas

        # Ejemplo: Pair plot para variables numéricas
        numeric_vars = [var for var, t in zip(variables, types) if t in ['continuo', 'discreto']]
        if len(numeric_vars) > 1:
            sns.pairplot(data[numeric_vars])
        plt.show()