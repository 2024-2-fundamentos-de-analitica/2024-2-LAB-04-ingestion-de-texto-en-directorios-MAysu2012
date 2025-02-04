# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import pandas as pd
import zipfile


ruta_zip = "files/input.zip"
ruta_input = "files/input"

if not os.path.exists(ruta_input):
    with zipfile.ZipFile(ruta_zip, 'r') as archivo_zip:
        archivo_zip.extractall("files/")

ruta_train_neg = "files/input/train/negative"
ruta_train_neu = "files/input/train/neutral"
ruta_train_pos = "files/input/train/positive"

archivos_neg = os.listdir(ruta_train_neg)
archivos_neu = os.listdir(ruta_train_neu)
archivos_pos = os.listdir(ruta_train_pos)

frases_train = []
sentimientos_train = []

for archivo in archivos_neg:
    with open(f"{ruta_train_neg}/{archivo}", "r", encoding="utf-8") as f:
        frases_train.append(f.read())
        sentimientos_train.append("negative")

for archivo in archivos_neu:
    with open(f"{ruta_train_neu}/{archivo}", "r", encoding="utf-8") as f:
        frases_train.append(f.read())
        sentimientos_train.append("neutral")

for archivo in archivos_pos:
    with open(f"{ruta_train_pos}/{archivo}", "r", encoding="utf-8") as f:
        frases_train.append(f.read())
        sentimientos_train.append("positive")

data_train = pd.DataFrame({"phrase": frases_train, "target": sentimientos_train})
data_train.to_csv("files/output/train_dataset.csv", index=False)


ruta_test_neg = "files/input/test/negative"
ruta_test_neu = "files/input/test/neutral"
ruta_test_pos = "files/input/test/positive"

archivos_neg = os.listdir(ruta_test_neg)
archivos_neu = os.listdir(ruta_test_neu)
archivos_pos = os.listdir(ruta_test_pos)

frases_test = []
sentimientos_test = []

for archivo in archivos_neg:
    with open(f"{ruta_test_neg}/{archivo}", "r", encoding="utf-8") as f:
        frases_test.append(f.read())
        sentimientos_test.append("negative")

for archivo in archivos_neu:
    with open(f"{ruta_test_neu}/{archivo}", "r", encoding="utf-8") as f:
        frases_test.append(f.read())
        sentimientos_test.append("neutral")

for archivo in archivos_pos:
    with open(f"{ruta_test_pos}/{archivo}", "r", encoding="utf-8") as f:
        frases_test.append(f.read())
        sentimientos_test.append("positive")

data_test = pd.DataFrame({"phrase": frases_test, "target": sentimientos_test})
data_test.to_csv("files/output/test_dataset.csv", index=False)


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

