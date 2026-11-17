# DETECTOR DE CELULARES MEDIANTE HAAR CASCADE Y OPENCV

## 1. Descripción del proyecto

El presente proyecto consiste en el desarrollo de un sistema de detección de teléfonos celulares en tiempo real, mediante técnicas de visión computacional, utilizando Python, OpenCV y el algoritmo de clasificación Haar Cascade.

El sistema utiliza un clasificador personalizado, entrenado a partir de un conjunto de imágenes positivas y negativas, para identificar posibles teléfonos celulares a través de una cámara web o un dispositivo móvil conectado mediante DroidCam.

Cuando el programa identifica una posible coincidencia, muestra un rectángulo verde y la etiqueta "Celular" sobre la región detectada.

Este proyecto fue desarrollado como parte del Avance de Proyecto Final 3 (AVPF-3) del curso Herramientas de Desarrollo Profesional - Civil, de la Universidad Tecnológica del Perú.

## 2. Objetivos del proyecto

### Objetivo general

Desarrollar un sistema de detección de celulares en tiempo real mediante el entrenamiento e implementación de un clasificador Haar Cascade utilizando Python y OpenCV.

### Objetivos específicos

- Construir un conjunto de imágenes positivas y negativas para el entrenamiento.
- Preparar y procesar las muestras mediante herramientas de OpenCV.
- Entrenar un clasificador personalizado utilizando Cascade Trainer GUI.
- Implementar el modelo entrenado mediante Python.
- Realizar pruebas de detección utilizando DroidCam.
- Analizar los resultados y las limitaciones del sistema.

## 3. Tecnologías y herramientas utilizadas

| Herramienta | Aplicación |
|---|---|
| Python | Desarrollo del programa de detección. |
| OpenCV | Procesamiento de imágenes y visión computacional. |
| Haar Cascade | Clasificación y detección del celular. |
| Cascade Trainer GUI | Configuración y entrenamiento del clasificador. |
| DroidCam | Captura de video mediante el celular. |
| Visual Studio Code | Edición y ejecución del código. |
| CMD | Ejecución de comandos y scripts. |
| Git y GitHub | Control de versiones y publicación del proyecto. |

## 4. Estructura del proyecto

```text
Detector-Celular-HaarCascade/
│
├── p/
│   └── Imágenes positivas del celular
│
├── n/
│   └── Imágenes negativas del entorno
│
├── classifier/
│   └── Archivos generados durante el entrenamiento
│
├── cascade.xml
│
├── pos_samples.vec
│
├── Detector_Celular_B_Movil_V1.py
├── Detector_Celular_B_Movil_V2.py
├── Detector_Celular_B_Movil_V3.py
├── Detector_Celular_B_Movil_V4.py
├── Detector_Celular_B_Movil_V5.py
│
└── README.md
```

Nota: La estructura representa los principales elementos del proyecto. Los archivos auxiliares deben conservar sus nombres y ubicaciones originales.

## 5. Construcción del dataset

Para desarrollar el clasificador se construyó un conjunto de datos propio, organizado en dos categorías:

| Categoría | Cantidad | Característica |
|---|---:|---|
| Positivas (p) | 168 | Imágenes que contienen el celular. |
| Negativas (n) | 407 | Imágenes que no contienen el objeto de interés. |
| Total | 575 | Imágenes utilizadas. |

Las imágenes fueron capturadas, recortadas y organizadas mediante scripts desarrollados en Python.

La carpeta `p` contiene las imágenes positivas utilizadas para identificar las características visuales del celular, mientras que la carpeta `n` contiene imágenes negativas que permiten al clasificador diferenciar el objeto de otros elementos del entorno.

## 6. Procedimiento de desarrollo y entrenamiento

El desarrollo del proyecto siguió las etapas establecidas en la metodología de entrenamiento mediante clasificadores en cascada.

### Paso 1. Consulta de la documentación

Se revisó la documentación de OpenCV sobre el funcionamiento y entrenamiento de clasificadores en cascada.

Documentación oficial:

https://docs.opencv.org/4.x/dc/d88/tutorial_traincascade.html

### Paso 2. Instalación de Cascade Trainer GUI

Se descargó e instaló Cascade Trainer GUI, herramienta utilizada para configurar y ejecutar el entrenamiento del clasificador Haar Cascade.

### Paso 3. Creación de la carpeta del objeto

Se creó la estructura de trabajo correspondiente al objeto que se desea detectar: el teléfono celular.

### Paso 4. Captura y organización de imágenes

Se utilizaron scripts de Python para capturar, recortar y guardar las fotografías en sus respectivas carpetas:

- `p`: imágenes positivas.
- `n`: imágenes negativas.

Para utilizar la biblioteca auxiliar imutils, se instaló mediante:

```bash
pip install imutils
```

### Paso 5. Entrenamiento del clasificador

Se configuró el entrenamiento mediante Cascade Trainer GUI, utilizando las muestras positivas y negativas previamente preparadas.

Características del entrenamiento:

| Parámetro | Valor |
|---|---|
| Clasificador | HAAR |
| Imágenes positivas | 168 |
| Imágenes negativas | 407 |
| Tamaño de muestra | 24 × 24 píxeles |
| Etapas configuradas | 12 |
| Etapas alcanzadas | 11 |

El entrenamiento finalizó en 11 etapas al alcanzarse la condición de falsas alarmas establecida durante el proceso.

Como resultado se obtuvo el archivo `cascade.xml`, que contiene el clasificador entrenado.

### Paso 6. Implementación del detector en Python

Una vez obtenido el modelo, se desarrolló el programa de detección utilizando OpenCV.

El script principal es:

```bash
python Detector_Celular_B_Movil_V5.py
```

El programa realiza las siguientes operaciones:

1. Importa las bibliotecas necesarias.
2. Establece la conexión con la cámara mediante DroidCam.
3. Carga el clasificador utilizando `cv2.CascadeClassifier()`.
4. Convierte los fotogramas a escala de grises.
5. Ejecuta la función `detectMultiScale()` para identificar posibles coincidencias.
6. Dibuja rectángulos verdes sobre las regiones detectadas.
7. Muestra la etiqueta "Celular" en la ventana de video.

## 7. Instalación y ejecución del proyecto

### Requisitos previos

- Windows 10 o Windows 11.
- Python instalado.
- Visual Studio Code o una terminal CMD.
- DroidCam instalado en el celular y en la computadora, si se utiliza este método de captura.
- Archivo `cascade.xml` correspondiente al modelo entrenado.

### Opción 1. Descargar el repositorio en ZIP

1. Ingresa a la página principal del repositorio.
2. Selecciona el botón "Code".
3. Haz clic en "Download ZIP".
4. Descomprime el archivo en tu computadora.
5. Abre la carpeta del proyecto en Visual Studio Code.

### Opción 2. Clonar el repositorio mediante Git

Ejecuta el siguiente comando:

```bash
git clone https://github.com/TU-USUARIO/Detector-Celular-HaarCascade.git
```

Ingresa a la carpeta:

```bash
cd Detector-Celular-HaarCascade
```

### Instalación de bibliotecas

Abre CMD o la terminal de Visual Studio Code y ejecuta:

```bash
pip install opencv-python imutils
```

### Verificación de OpenCV y Haar Cascade

Antes de ejecutar el detector, comprueba que OpenCV tenga disponible la función CascadeClassifier.

Abre Python y ejecuta:

```python
import cv2

print(cv2.__version__)

print(hasattr(cv2, 'CascadeClassifier'))
```

El resultado esperado de la última instrucción es:

```text
True
```

Si el resultado es `False`, puede existir una instalación incompleta o una incompatibilidad de OpenCV.

En ese caso, se recomienda realizar el siguiente procedimiento.

Desinstalar OpenCV:

```bash
pip uninstall opencv-python
```

Instalar la versión indicada en la guía del docente:

```bash
pip install opencv-python==4.10.0.84
```

Volver a ejecutar la prueba:

```python
import cv2

print(hasattr(cv2, 'CascadeClassifier'))
```

El resultado esperado es:

```text
True
```

### Configuración de DroidCam

Para utilizar el celular como cámara:

1. Instala y abre DroidCam en el dispositivo móvil.
2. Ejecuta DroidCam en la computadora.
3. Conecta ambos dispositivos a la misma red Wi-Fi.
4. Identifica la dirección IP y el puerto mostrados por la aplicación.
5. Abre `Detector_Celular_B_Movil_V5.py`.
6. Configura la dirección de conexión correspondiente a tu dispositivo.

La dirección IP y el puerto deben corresponder a la conexión activa de DroidCam. No utilices una dirección de otro equipo.

### Ejecución del detector

Desde la terminal, ejecuta:

```bash
python Detector_Celular_B_Movil_V5.py
```

Se abrirá una ventana de video en tiempo real donde se visualizarán las detecciones del celular mediante rectángulos verdes y etiquetas.

Para finalizar el programa, presiona la tecla ESC.

## 8. Resultados obtenidos

El sistema fue probado utilizando DroidCam como fuente de video.

Durante las pruebas se consiguió detectar el teléfono celular y delimitarlo mediante rectángulos verdes, mostrando la etiqueta correspondiente.

También se identificaron detecciones adicionales o falsos positivos en determinadas condiciones de prueba.

Estos resultados evidencian que el modelo cumple parcialmente con el objetivo de detección, pero todavía presenta limitaciones relacionadas con la variedad del dataset, las condiciones de iluminación, la orientación del objeto y los parámetros del clasificador.

Los resultados corresponden a pruebas experimentales y no representan una medición estadística general de precisión.

## 9. Limitaciones y posibles mejoras

Entre las principales limitaciones identificadas se encuentran:

- Variabilidad limitada de algunas imágenes positivas.
- Diferencias entre las condiciones de entrenamiento y las pruebas reales.
- Sensibilidad a cambios de iluminación y orientación.
- Aparición de falsos positivos.
- Necesidad de ampliar y diversificar el dataset.
- Posibilidad de optimizar los parámetros del clasificador.

Como mejoras futuras se propone incrementar la cantidad y variedad de imágenes, realizar nuevas pruebas experimentales y ajustar los parámetros del entrenamiento para reducir las detecciones incorrectas.

## 10. Autor

**Antony Daniel Juárez Litano**

Universidad Tecnológica del Perú (UTP)

Curso: Herramientas de Desarrollo Profesional - Civil

Sección: 49744

Proyecto: Avance de Proyecto Final 3 (AVPF-3)

Año: 2026

## 11. Referencias y documentación

- OpenCV. Documentación sobre entrenamiento de clasificadores en cascada: https://docs.opencv.org/4.x/dc/d88/tutorial_traincascade.html
- Python. Sitio oficial de descarga: https://www.python.org/downloads/
- OpenCV. Biblioteca de visión computacional: https://opencv.org/
- Cascade Trainer GUI. Herramienta de entrenamiento utilizada durante el desarrollo, según la guía proporcionada en clase.

---

## Información adicional

Este repositorio contiene los archivos principales del proyecto académico y permite consultar el procedimiento de preparación del dataset, entrenamiento del clasificador e implementación del detector de celulares mediante Python y OpenCV.
