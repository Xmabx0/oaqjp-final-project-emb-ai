"""
Servidor Flask para la deteccion de emociones.
Este script maneja las solicitudes web y conecta con el detector de emociones.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Recibe el texto de la interfaz, lo analiza y devuelve el resultado formateado.
    """
    # Obtener el texto del argumento de la URL
    text_to_analyze = request.args.get('textToAnalyze')

    # Llamar a la funcion de deteccion
    response = emotion_detector(text_to_analyze)

    # Extraer los valores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Validacion de error para entradas vacias
    if dominant_emotion is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"

    # Respuesta con el formato solicitado por el cliente
    return (
        f"Para la declaración dada, la respuesta del sistema es 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} y 'sadness': {sadness}. "
        f"La emoción dominante es {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renderiza la pagina principal del proyecto.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    