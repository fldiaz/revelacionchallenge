# Objetivo 1: Crear un modelo de clasificación de autos y motos.

Utilice YOLO para detectar objetos en imágenes.
Los directorios  son:
yolo-coco/: donde se encuentran los archivos del modelo YOLOv3 entrenados previamente. Los weights deben bajarse de
https://pjreddie.com/media/files/yolov3.weights
imagenes / : Esta carpeta contiene cuatro imágenes estáticas con las que se puede realizar la detección de objetos con fines de prueba y evaluación.
Para correr el modelo se debe utilizar el script imagenes.py y otorgar un path a la imagen de prueba

```
cd audio_recog
python imagenes.py
```

# Objetivo 2: Crear un modelo de detección de voz y transcripción de
canciones en ingles y en español

En esta aplicación, se intenta convertir archivos de audio a texto.
Se usa la libreria SpeechRecognition con la API de Google Cloud Speech
Se utiliza la web de conversión Zamzar para modificar la extensión de los archivos, la principal limitación es el peso de los archivos: 'maximum_file_size': 1048576
El directorio es audios, donde se encuentras algunos ejemplos.
Para correr el modelo se debe utilizar el script speech.py y otorgar un path al audio de prueba

```
cd audio_recog
python speech.py
```
