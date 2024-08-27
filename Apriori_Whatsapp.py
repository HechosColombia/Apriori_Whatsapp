!pip install apyori

import re
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from apyori import apriori
from pprint import pprint

# Cargar las stop words en español
# Load Spanish stop words
stop_words = set(stopwords.words('spanish'))
# Añadir el signo "-" a la lista de stop words
# Add the "-" sign to the stop words list
stop_words.add('-')

# Función para cargar y preprocesar los datos del chat
# Function to load and preprocess chat data
def preprocess_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    messages = []
    current_message = ""
    current_sender = None

    for line in lines:
        # Verificar si la línea coincide con el formato de timestamp
        # Check if the line matches the timestamp format
        if re.match(r'^\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{2}.* - .*:', line):
            if current_message and current_sender:
                if "<Multimedia omitido>" not in current_message:
                    messages.append((current_sender, current_message.strip()))

            # Extraer el remitente y el mensaje
            # Extract the sender and the message
            date_time, rest = line.split(" - ", 1)
            sender, message = rest.split(":", 1)
            current_sender = sender.strip()
            current_message = message.strip()
        else:
            # Continuación del mensaje anterior
            # Continuation of the previous message
            current_message += " " + line.strip()

    # Añadir el último mensaje si no contiene "<Multimedia omitido>"
    # Add the last message if it doesn't contain "<Multimedia omitido>"
    if current_message and current_sender:
        if "<Multimedia omitido>" not in current_message:
            messages.append((current_sender, current_message.strip()))

    return messages

# Parámetros de configuración
# Configuration parameters
file_path = 'namefile.txt'  # Ruta del archivo de chat exportado / Path of the exported chat file
sender_of_interest = 'NameSender'  # Nombre del remitente / Name of the sender

# Preprocesar el chat
# Preprocess the chat
chat_data = preprocess_chat(file_path)

# Convertir a DataFrame para un manejo más sencillo
# Convert to DataFrame for easier handling
df = pd.DataFrame(chat_data, columns=['Sender', 'Message'])

# Filtrar mensajes del remitente especificado
# Filter messages from the specified sender
filtered_messages = df[df['Sender'] == sender_of_interest]['Message'].tolist()

# Lista para almacenar las transacciones (mensajes tokenizados sin stop words)
# List to store transactions (tokenized messages without stop words)
transacciones = []

# Recorrer los mensajes filtrados
# Loop through the filtered messages
for mensaje in filtered_messages:
    # Tokenizar cada mensaje y eliminar stop words y el signo "-"
    # Tokenize each message and remove stop words and the "-" sign
    tokens = [palabra.lower() for palabra in mensaje.split() if palabra.lower() not in stop_words]
    transacciones.append(tokens)

# Filtrar las transacciones que no estén vacías
# Filter transactions that are not empty
transacciones = [t for t in transacciones if len(t) > 0]

# Aplicar el algoritmo Apriori con parámetros ajustados
# Apply the Apriori algorithm with adjusted parameters
resultados = list(apriori(
    transacciones,
    min_support=0.003,       # Ajuste del soporte mínimo / Minimum support adjustment
    min_confidence=0.3,     # Ajuste de la confianza mínima / Minimum confidence adjustment
    min_lift=0.5,           # Ajuste del lift mínimo / Minimum lift adjustment
    min_length=2            # Ajuste de la longitud mínima / Minimum length adjustment
))

# Mostrar las primeras 10 reglas de asociación
# Display the first 10 association rules
if resultados:
    print(f"Se encontraron {len(resultados)} reglas de asociación:")
    # Found association rules
    for regla in resultados[:19]:
        items = [x for x in regla[0]]
        print(f"Regla: {items} -> Soporte: {regla[1]:.4f} -> Confianza: {regla[2][0][2]:.4f} -> Lift: {regla[2][0][3]:.4f}")
else:
    pprint("No se encontraron reglas de asociación con los parámetros actuales.")
    # No association rules found with the current parameters