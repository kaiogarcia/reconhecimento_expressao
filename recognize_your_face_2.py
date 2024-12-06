import cv2
from deepface import DeepFace

# Inicializa o classificador de rosto do OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Caminho da imagem
image_path = "raiva.jpg"

# Carrega a imagem
image = cv2.imread(image_path)

if image is None:
    print("Erro: Não foi possível carregar a imagem.")
else:
    # Converte a imagem para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detecta rostos na imagem
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Desenha um retângulo ao redor do rosto detectado
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Recorta o rosto detectado
        face = image[y:y+h, x:x+w]

        try:
            # Analisa emoções usando DeepFace
            analysis = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
            
            # Verifica o formato do retorno
            if isinstance(analysis, list):
                emotion = analysis[0]['dominant_emotion']
            else:
                emotion = analysis['dominant_emotion']
            
            # Exibe a emoção detectada acima do rosto
            cv2.putText(image, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        except Exception as e:
            print("Erro na análise de emoções:", e)

    # Exibe a imagem com as detecções
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
