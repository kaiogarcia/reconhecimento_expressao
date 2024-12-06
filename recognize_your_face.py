import cv2
from deepface import DeepFace

# Inicializa o classificador de rosto do OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Captura de vídeo ao vivo da câmera
video_capture = cv2.VideoCapture(0)

while True:
    # Captura quadro por quadro
    ret, frame = video_capture.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostos no quadro
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Desenha um retângulo ao redor do rosto detectado
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Recorta o rosto detectado
        face = frame[y:y+h, x:x+w]

        try:
            # Analisa emoções usando DeepFace
            analysis = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
            
            # Verifica o formato do retorno
            if isinstance(analysis, list):
                emotion = analysis[0]['dominant_emotion']
            else:
                emotion = analysis['dominant_emotion']
            
            # Exibe a emoção detectada acima do rosto
            cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        except Exception as e:
            print("Erro na análise de emoções:", e)

    # Exibe o quadro com as detecções
    cv2.imshow('Video', frame)

    # Sai com a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
video_capture.release()
cv2.destroyAllWindows()
