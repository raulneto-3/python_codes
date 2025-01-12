import os
import shutil
import logging
from transformers import pipeline
from PIL import Image
import pytesseract
import configparser

# Configuração de logging
logging.basicConfig(filename='file_organiser.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Carregar modelos de IA
text_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
image_classifier = pipeline("image-classification", model="google/vit-base-patch16-224")

def classify_text(text):
    labels = ["document", "code", "project", "other"]
    result = text_classifier(text, candidate_labels=labels)
    return result['labels'][0]

def classify_image(image_path):
    image = Image.open(image_path)
    result = image_classifier(image)
    return result[0]['label']

def read_file_content(file_path):
    _, extension = os.path.splitext(file_path)
    if extension in ['.txt', '.md', '.py', '.java', '.html', '.csv']:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif extension in ['.jpg', '.jpeg', '.png', '.gif']:
        return pytesseract.image_to_string(Image.open(file_path))
    else:
        return ""

def organise_files(path):
    for root, _, files in os.walk(path):
        for current_file in files:
            source = os.path.join(root, current_file)
            content = read_file_content(source)
            if content:
                if current_file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    category = classify_image(source)
                else:
                    category = classify_text(content)
                destination_dir = os.path.join(path, category)
                os.makedirs(destination_dir, exist_ok=True)
                destination = os.path.join(destination_dir, current_file)
                try:
                    shutil.move(source, destination)
                    logging.info(f"Moved {source} to {destination}")
                except Exception as e:
                    logging.error(f"Error moving {source} to {destination}: {str(e)}")



if __name__ == '__main__':
    path = "C:\\Users\\King\\Downloads"
    try:
        organise_files(path)
    except Exception as e:
        logging.error(f"Error: {str(e)}")