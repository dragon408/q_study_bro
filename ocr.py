import pytesseract
from PIL import Image
import re
import os

# Автоматично визначає шлях на Mac або на Railway (або не чіпає, якщо Tesseract знайдено в PATH)
if os.name == 'posix':
    possible_mac_path = "/opt/homebrew/bin/tesseract"
    if os.path.exists(possible_mac_path):
        pytesseract.pytesseract.tesseract_cmd = possible_mac_path
    # інакше — залишити за замовчуванням (для Linux/Docker)

def ocr_image(image_path, lang='eng'):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang=lang)
    return text

def questions_list(text):
    questions = re.split(r'®|©|@|\d+', text)
    questions = [q.strip() for q in questions if q.strip()]
    return questions

# ❗️Під час запуску на Railway з web-інтерфейсом — image_path має бути шлях до завантаженого файлу
# ❗️Приклад локального запуску:
# image_path = 'photo.jpg'
# text = ocr_image(image_path, lang='ukr')
# print(text)
# print(questions_list(text))
