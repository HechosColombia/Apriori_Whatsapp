# Apriori Analysis of WhatsApp Chat Data / Análisis Apriori de Datos de Chat de WhatsApp

*This README is available in both English and Spanish.*

*Este README está disponible en inglés y español.*

## English

### Project Overview

This project applies the Apriori algorithm to analyze the content of a WhatsApp chat exported as a `.txt` file. The goal is to discover frequent word associations within the messages sent by a specific sender.

### Features

- **Stop Words Removal**: The script removes common Spanish stop words and the "-" sign before analyzing the text.
- **Customizable Sender Filtering**: Analyze messages sent by a specific individual from the chat.
- **Apriori Algorithm**: Discover frequent itemsets (word combinations) and generate association rules from the messages.
- **Parameter Tuning**: Easily adjust the minimum support, confidence, lift, and rule length for the Apriori algorithm.

### Prerequisites

Before running the script, ensure you have the following Python packages installed:

- `apyori`: for applying the Apriori algorithm.
- `pandas`: for data manipulation.
- `nltk`: for natural language processing, specifically stop words.
- `re`: for regular expressions.

You can install the necessary packages by running:

```bash
pip install apyori pandas nltk

How to Use
Prepare Your WhatsApp Chat Export:

Export a WhatsApp chat to a .txt file and place it in the root directory of this project.
Edit the Script:

Open the script file and modify the file_path variable to point to your chat file.
Set the sender_of_interest variable to the name of the sender whose messages you want to analyze.
Run the Script:

Execute the script to process the chat data and apply the Apriori algorithm. The script will output the most significant association rules found.

file_path = 'NameFile.txt'  # Path to the exported chat file
sender_of_interest = 'NameSender'  # Name of the sender to analyze

The script will filter messages sent by Vp and apply the Apriori algorithm to identify frequent word combinations in their messages.

Output
The script will output the association rules in the following format:

Rule: ['word1', 'word2'] -> Support: 0.0030 -> Confidence: 0.3000 -> Lift: 1.5000

Where:

Rule: The word combination found.
Support: The support value indicating how frequently the rule occurs in the dataset.
Confidence: The confidence value indicating the likelihood of finding the second word given the first.
Lift: The lift value indicating the strength of the rule compared to random chance.
If no rules are found with the current parameters, the script will notify you.

Customization
You can adjust the following parameters within the script to fine-tune the analysis:

min_support: Minimum support for the rules (default is 0.003).
min_confidence: Minimum confidence for the rules (default is 0.3).
min_lift: Minimum lift for the rules (default is 0.5).
min_length: Minimum number of items in a rule (default is 2).
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributions
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or improvements.

Acknowledgments
nltk for providing tools for natural language processing.
apyori for the implementation of the Apriori algorithm.
WhatsApp for providing the export chat feature used in this analysis.




Español
Resumen del Proyecto
Este proyecto aplica el algoritmo Apriori para analizar el contenido de un chat de WhatsApp exportado como un archivo .txt. El objetivo es descubrir asociaciones frecuentes de palabras dentro de los mensajes enviados por un remitente específico.

Características
Eliminación de Stop Words: El script elimina las stop words comunes en español y el signo "-" antes de analizar el texto.
Filtrado Personalizable del Remitente: Analiza los mensajes enviados por un individuo específico del chat.
Algoritmo Apriori: Descubre conjuntos de elementos frecuentes (combinaciones de palabras) y genera reglas de asociación a partir de los mensajes.
Ajuste de Parámetros: Ajusta fácilmente el soporte mínimo, la confianza, el lift y la longitud de las reglas para el algoritmo Apriori.
Requisitos
Antes de ejecutar el script, asegúrate de tener instalados los siguientes paquetes de Python:

apyori: para aplicar el algoritmo Apriori.
pandas: para la manipulación de datos.
nltk: para el procesamiento de lenguaje natural, específicamente stop words.
re: para expresiones regulares.
Puedes instalar los paquetes necesarios ejecutando:

pip install apyori pandas nltk

Cómo Usar
Prepara la Exportación de tu Chat de WhatsApp:

Exporta un chat de WhatsApp a un archivo .txt y colócalo en el directorio raíz de este proyecto.
Edita el Script:

Abre el archivo del script y modifica la variable file_path para que apunte a tu archivo de chat.
Establece la variable sender_of_interest con el nombre del remitente cuyos mensajes deseas analizar.
Ejecuta el Script:

Ejecuta el script para procesar los datos del chat y aplicar el algoritmo Apriori. El script mostrará las reglas de asociación más significativas encontradas.
Ejemplo de Uso

file_path = 'NombreArchivo.txt'  # Ruta del archivo de chat exportado
sender_of_interest = 'NombreRemmitente'  # Nombre del remitente a analizar

El script filtrará los mensajes enviados por Vp y aplicará el algoritmo Apriori para identificar combinaciones frecuentes de palabras en sus mensajes.

Salida
El script mostrará las reglas de asociación en el siguiente formato:

Regla: ['palabra1', 'palabra2'] -> Soporte: 0.0030 -> Confianza: 0.3000 -> Lift: 1.5000

Donde:

Regla: La combinación de palabras encontrada.
Soporte: El valor de soporte que indica la frecuencia con la que ocurre la regla en el conjunto de datos.
Confianza: El valor de confianza que indica la probabilidad de encontrar la segunda palabra dada la primera.
Lift: El valor de lift que indica la fuerza de la regla en comparación con el azar.
Si no se encuentran reglas con los parámetros actuales, el script te lo notificará.

Personalización
Puedes ajustar los siguientes parámetros dentro del script para afinar el análisis:

min_support: Soporte mínimo para las reglas (por defecto es 0.003).
min_confidence: Confianza mínima para las reglas (por defecto es 0.3).
min_lift: Lift mínimo para las reglas (por defecto es 0.5).
min_length: Número mínimo de elementos en una regla (por defecto es 2).
Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Contribuciones
¡Las contribuciones son bienvenidas! No dudes en enviar un pull request o abrir un issue si tienes sugerencias o mejoras.

Agradecimientos
nltk por proporcionar herramientas para el procesamiento de lenguaje natural.
apyori por la implementación del algoritmo Apriori.
WhatsApp por proporcionar la función de exportar chats utilizada en este análisis.


Este README ofrece una versión en inglés y español para que sea accesible a una audiencia más amplia. Puedes copiar y pegar este contenido en tu archivo `README.md` en GitHu.
