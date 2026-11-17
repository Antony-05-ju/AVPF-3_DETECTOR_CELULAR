import cv2

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Conexión a tu cámara (DroidCam / IP Webcam)
cap = cv2.VideoCapture("http://10.214.148.209:4747/video")

# Cargar el clasificador en cascada
CelularBClassif = cv2.CascadeClassifier("cascade.xml")

if not cap.isOpened():
  print("Error: No se pudo conectar a la cámara del celular.")
  exit()

while True:
  ret, frame = cap.read()

  if not ret:
    print("Error: No se pudo recibir el fotograma. Reconectando...")
    break

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Detección optimizada con mayor exigencia (minNeighbors alto)
  # para eliminar los falsos positivos en la mesa
  toy = CelularBClassif.detectMultiScale(
      gray, scaleFactor=1.1, minNeighbors=22, minSize=(90, 100)
  )

  for x, y, w, h in toy:
    margen_x = int(w * 0.15)
    margen_y = int(h * 0.15)

    x1 = max(x - margen_x, 0)
    y1 = max(y - margen_y, 0)

    x2 = x + w + margen_x
    y2 = y + h + margen_y

    # Dibujar el rectángulo solo sobre el celular real
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

  # Presiona la tecla ESC para salir
  if cv2.waitKey(1) == 27:
    break

cap.release()
cv2.destroyAllWindows()
