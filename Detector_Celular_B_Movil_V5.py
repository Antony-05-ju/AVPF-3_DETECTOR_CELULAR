import cv2

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap = cv2.VideoCapture("http://10.214.148.209:4747/video")

CelularBClassif = cv2.CascadeClassifier("cascade.xml")

if not cap.isOpened():
  print("Error: No se pudo conectar a la cámara del celular.")
  exit()

while True:
  ret, frame = cap.read()
  if not ret:
    print("Error: No se pudo recibir el fotograma.")
    break

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Mantenemos tus parámetros de precisión, pero puedes ajustar minSize
  # si notas que detecta objetos más chicos.
  toy = CelularBClassif.detectMultiScale(
      gray, scaleFactor=5, minNeighbors=91, minSize=(90, 100)  # Tamaño mínimo aumentado para filtrar objetos pequeños/gato
  )

  for x, y, w, h in toy:
    # FILTRO ADICIONAL: Validar la proporción (un celular suele ser más alto que ancho o rectangular)
    # Esto ayuda a descartar formas cuadradas extrañas o texturas de la pared/gato.
    proporcion = h / float(w)
    if proporcion < 0.8:  # Si es demasiado ancho en comparación a su alto, lo ignora
      continue

    # Márgenes para ampliar el cuadro al tamaño real del celular
    margen_x = int(w * 0.60)
    margen_y = int(w * 0.60)

    x1 = max(x - margen_x, 0)
    y1 = max(y - margen_y, 0)
    x2 = x + w + margen_x
    y2 = y + h + margen_y

    # Dibujar el rectángulo ampliado
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
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

  cv2.imshow("frame", frame)

  if cv2.waitKey(1) == 27:
    break

cap.release()
cv2.destroyAllWindows()
