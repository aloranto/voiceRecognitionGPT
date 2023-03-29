import speech_recognition as sr
import requests

# Crear un objeto de reconocimiento de voz
r = sr.Recognizer()

# Usar el micrófono como fuente de entrada de audio
with sr.Microphone() as source:
    
    # Ajustar el nivel de ruido de fondo
    r.adjust_for_ambient_noise(source)
    
    # Indicar al usuario que comience a hablar
    print("Habla ahora:")
    
    # Escuchar la entrada de audio del usuario
    audio = r.listen(source)
    
    # Enviar la entrada de audio a la API de ChatGPT
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci-codex/completions", 
        headers={"Authorization": "Bearer API_KEY"}, 
        json={
            "prompt": f"{r.recognize_google(audio)}", 
            "max_tokens": 1000,
            "temperature": 0.7
        }
    )
    
    # Imprimir la respuesta de la API
    print(response.json()["choices"][0]["text"])