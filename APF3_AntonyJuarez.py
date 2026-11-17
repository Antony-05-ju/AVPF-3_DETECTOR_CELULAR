# -*- coding: utf-8 -*-
"""
APF3_AntonyJuarez.py
Avance de Proyecto Final 3 (AVPF-3) - Herramientas de Desarrollo Profesional - Civil (UTP)
Alumno: Juárez Litano, Antony Daniel (U24201705)

Detector de celulares en tiempo real con un clasificador Haar Cascade (cascade.xml)
y OpenCV. Corresponde a la versión V4 del detector (Detector_Celular_B_Movil_V4.py);
solo se agregaron comentarios, la lógica es la misma.

Uso:
  1. Abrir DroidCam en el celular y anotar la dirección IP y el puerto que muestra.
  2. Reemplazar la URL de cv2.VideoCapture por la del celular.
  3. Dejar cascade.xml en la misma carpeta que este archivo y ejecutar el script.
  4. Presionar ESC para cerrar la ventana.
"""
import cv2

# Entrada de video. Para una webcam local se usaría: cv2.VideoCapture(0, cv2.CAP_DSHOW)
# Con DroidCam, el video se lee por red desde la dirección IP del celular.
# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap = cv2.VideoCapture("http://10.217.192.93:4747/video")

# Carga del modelo entrenado con Cascade Trainer GUI.
CelularBClassif = cv2.CascadeClassifier("cascade.xml")

while True:
  # Lectura de un fotograma; si no llega imagen, se termina el programa.
  ret, frame = cap.read()
  if not ret:
    break

  # El clasificador Haar trabaja sobre la imagen en escala de grises.
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Detección en varias escalas:
  #   scaleFactor  = 1.1 -> reduce la imagen un 10 % en cada escala (revisa muchos tamaños)
  #   minNeighbors = 91  -> exige muchas ventanas vecinas coincidentes (menos falsos positivos)
  #   minSize      = (70, 78) -> ignora detecciones más pequeñas que este tamaño en píxeles
  toy = CelularBClassif.detectMultiScale(
      gray, scaleFactor=1.1, minNeighbors=91, minSize=(70, 78)
  )

  # Por cada detección (x, y, ancho, alto) se dibuja el recuadro y la etiqueta.
  for x, y, w, h in toy:
    # Ajusta estos porcentajes según qué tan grande quieras el recuadro
    margen_x = int(w * 0.60)
    margen_y = int(w * 0.60)

    # Esquinas del recuadro ampliado (sin salirse del borde izquierdo/superior).
    x1 = max(x - margen_x, 0)
    y1 = max(y - margen_y, 0)
    x2 = x + w + margen_x
    y2 = y + h + margen_y

    # Dibujar el rectángulo ampliado
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # Etiqueta del objeto sobre el recuadro.
    cv2.putText(
        frame,
        "Celular",
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
    )

  # Muestra el fotograma con las detecciones.
  cv2.imshow("frame", frame)

  # ESC (código 27) cierra el programa.
  if cv2.waitKey(1) == 27:
    break

# Libera la cámara y cierra las ventanas.
cap.release()
cv2.destroyAllWindows()
