# 📱 Detector de Celulares mediante Haar Cascade y OpenCV

Sistema de detección de celulares en tiempo real desarrollado en **Python**, utilizando **OpenCV** y el algoritmo de clasificación **Haar Cascade**. El proyecto utiliza un modelo entrenado con imágenes propias y permite realizar detecciones mediante una cámara web o un dispositivo móvil conectado a través de DroidCam.

## 📌 Descripción del proyecto

Este proyecto consiste en desarrollar un detector personalizado capaz de identificar teléfonos celulares mediante técnicas de visión computacional.

Para su desarrollo se construyó un conjunto de datos propio, se entrenó un clasificador Haar Cascade y posteriormente se implementó el modelo en Python utilizando OpenCV para realizar detecciones en tiempo real.

El sistema identifica posibles celulares y muestra rectángulos verdes con la etiqueta **"Celular"** sobre las regiones detectadas.

## 📊 Dataset utilizado

Para el entrenamiento del clasificador se utilizaron las siguientes imágenes:

| Tipo de imágenes | Cantidad | Descripción |
|---|---:|---|
| Positivas (p) | 168 | Imágenes que contienen celulares. |
| Negativas (n) | 407 | Imágenes de fondos y escenas sin el objeto. |
| **Total** | **575** | Conjunto de imágenes utilizado. |

## ⚙️ Herramientas y tecnologías

- **Python:** lenguaje de programación.
- **OpenCV:** procesamiento de imágenes y detección de objetos.
- **Haar Cascade:** algoritmo de clasificación utilizado para reconocer celulares.
- **Cascade Trainer GUI:** herramienta utilizada para configurar y ejecutar el entrenamiento.
- **DroidCam:** conexión de la cámara del celular con la computadora.
- **Visual Studio Code:** entorno de desarrollo.

## 📁 Estructura del proyecto

```text
Detector-Celular-HaarCascade/
│
├── p/                              # Imágenes positivas
├── n/                              # Imágenes negativas
│
├── classifier/                     # Archivos del entrenamiento
│   ├── cascade.xml
│   ├── params.xml
│   ├── log.txt
│   └── stage*.xml
│
├── cascade.xml                      # Clasificador utilizado
│
├── pos_samples.vec                  # Muestras positivas generadas
│
├── Detector_Celular_B_Movil_V1.py
├── Detector_Celular_B_Movil_V2.py
├── Detector_Celular_B_Movil_V3.py
├── Detector_Celular_B_Movil_V4.py
├── Detector_Celular_B_Movil_V5.py  # Programa principal
│
├── Detector_Celular_B_p.py
├── Detector_Celular_B_n.py
│
└── README.md
```

## 📥 Cómo descargar y utilizar este proyecto

### Opción 1 — Descargar archivo ZIP

1. Ingresa a la página principal del repositorio.
2. Haz clic en el botón verde **Code (Código)**.
3. Selecciona **Download ZIP (Descargar ZIP)**.
4. Descomprime el archivo en tu computadora.
5. Abre la carpeta del proyecto en Visual Studio Code.

### Opción 2 — Clonar mediante Git

Abre CMD o una terminal y ejecuta:

```bash
git clone https://github.com/TU-USUARIO/Detector-Celular-HaarCascade.git
```

Ingresa a la carpeta:

```bash
cd Detector-Celular-HaarCascade
```

## 🛠️ Instalación y configuración

### 1. Instalar Python

Descarga Python desde:

https://www.python.org/downloads/

Durante la instalación, activa la opción **Add Python to PATH**.

Verifica que Python esté instalado:

```bash
python --version
```

### 2. Instalar las bibliotecas necesarias

Abre CMD o la terminal de Visual Studio Code y ejecuta:

```bash
pip install opencv-python numpy imutils
```

Estas bibliotecas permiten realizar el procesamiento de imágenes y ejecutar los scripts auxiliares del proyecto.

### 3. Configurar DroidCam

Para utilizar la cámara del celular:

1. Instala DroidCam en tu dispositivo móvil.
2. Abre DroidCam en tu computadora.
3. Conecta ambos dispositivos a la misma red Wi-Fi.
4. Identifica la dirección IP y el puerto que muestra DroidCam.
5. Abre el archivo `Detector_Celular_B_Movil_V5.py` en Visual Studio Code.
6. Busca la siguiente línea:

```python
cap = cv2.VideoCapture("http://TU_IP_DROIDCAM:4747/video")
```

7. Reemplaza `TU_IP_DROIDCAM` por la dirección IP que aparece en tu aplicación DroidCam.

**Importante:** utiliza la dirección IP y el puerto correspondientes a tu propia conexión. La dirección de cada dispositivo puede ser diferente.

### 4. Ejecutar el detector

Verifica que el archivo `cascade.xml` se encuentre en la misma carpeta que el programa principal.

Desde la terminal, ejecuta:

```bash
python Detector_Celular_B_Movil_V5.py
```

El programa abrirá una ventana de video en tiempo real y mostrará rectángulos verdes con la etiqueta **Celular** cuando identifique posibles coincidencias.

Para finalizar la ejecución, presiona la tecla **ESC**.

## 🧠 Entrenamiento del clasificador

El modelo fue desarrollado utilizando el algoritmo Haar Cascade mediante Cascade Trainer GUI.

Características principales del entrenamiento:

| Parámetro | Valor |
|---|---|
| Tipo de clasificador | HAAR |
| Muestras positivas | 168 |
| Muestras negativas | 407 |
| Tamaño de muestra | 24 × 24 píxeles |
| Etapas configuradas | 12 |
| Etapas del modelo final | 11 |

Como resultado se obtuvo el archivo `cascade.xml`, utilizado posteriormente para realizar la detección mediante OpenCV.

## 🎯 Resultados obtenidos

El detector fue implementado y probado utilizando DroidCam como fuente de video.

Durante las pruebas se consiguió identificar el celular mediante rectángulos verdes y etiquetas de texto.

Sin embargo, también se observaron algunas detecciones adicionales o falsos positivos, por lo que el modelo presenta oportunidades de mejora relacionadas con la calidad y variedad del dataset y los parámetros del clasificador.

## ⚠️ Consideraciones importantes

- Es necesario tener Python instalado y las bibliotecas correspondientes.
- Para utilizar DroidCam, ambos dispositivos deben estar conectados a la misma red.
- La dirección IP y el puerto deben configurarse de acuerdo con la conexión actual.
- No elimines ni cambies de ubicación el archivo `cascade.xml` sin actualizar la ruta en el código.
- El modelo fue entrenado específicamente para detectar celulares.
- Los resultados pueden variar según la iluminación, orientación, distancia y condiciones del entorno.
- Si la cámara no se conecta, verifica que DroidCam esté activo y que ningún otro programa esté utilizando la cámara.

## 👨‍💻 Autor

**Antony Daniel Juárez Litano**

Universidad Tecnológica del Perú (UTP)

Curso: Herramientas de Desarrollo Profesional - Civil

Proyecto: Avance de Proyecto Final 3 (AVPF-3)

Año: 2026

---

**Desarrollado con Python, OpenCV y Haar Cascade.**
