import pytest
import pandas as pd
import numpy as np

def calcular_rentabilidad(df):
    """Calcula la rentabilidad de cada producto en el dataset de ventas."""
    df_resultado = df.copy()
    df_resultado['rentabilidad'] = ((1 - df_resultado['descuento']) * 100).round(2)
    return df_resultado

@pytest.fixture
def df_test():
    """Fixture que crea un DataFrame de prueba."""
    data = {
        'id': [1, 2, 3],
        'producto': ['Producto A', 'Producto B', 'Producto C'],
        'precio': [100.0, 200.0, 300.0],
        'cantidad': [2, 1, 3],
        'descuento': [0.1, 0.0, 0.25],
        'total': [180.0, 200.0, 675.0]
    }
    return pd.DataFrame(data)

# Escribe tus tests aquí
def test_columna_rentabilidad_existe(df_test):
    # Tu código aquí
    resultado = calcular_rentabilidad(df_test)
    assert 'rentabilidad' in resultado.columns

def test_valores_rentabilidad_correctos(df_test):
    # Tu código aquí
    resultado = calcular_rentabilidad(df_test)
    for index, row in resultado.iterrows():
        assert row['rentabilidad'] == (row['precio'] * row['descuento'])

def test_caso_descuento_cero():
    # Tu código aquí
    pass
