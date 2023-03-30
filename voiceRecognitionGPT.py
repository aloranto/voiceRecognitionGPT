# Secret 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
import os
import openai
import speech_recognition as sr
import tempfile

os.getenv('OPENAI_API_KEY')

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

    print("************   Se ha recogido: ", r.recognize_google(audio, language="es-ES"))

    transcript = sr.Recognizer().recognize_google(audio, language="es-ES")
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=transcript,
    max_tokens=500,
    n=1,
    stop=None,
    temperature=0.7,
)
print(response.choices[0].text)

