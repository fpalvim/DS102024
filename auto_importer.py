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

    def describe_numeric(self):
        """
        Genera un análisis descriptivo de las columnas numéricas.

        Returns:
            pandas.DataFrame: Descripción de las columnas numéricas.
        """
        return self.numeric_cols.describe()

    def describe_non_numeric(self):
        """
        Genera un análisis descriptivo de las columnas no numéricas.

        Returns:
            pandas.DataFrame: Descripción de las columnas no numéricas.
        """
        return self.non_numeric_cols.describe(include='all')