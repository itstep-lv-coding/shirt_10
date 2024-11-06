import sys
from PIL import Image, ImageOps


def main():
    # Перевірка аргументів командного рядка
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py <input_image> <output_image>")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # input_path = "before1.jpg"
    # output_path = "after1.jpg"

    # Перевірка розширення файлів
    if not (input_path.lower().endswith(('.jpg', '.jpeg', '.png')) and output_path.lower().endswith(
            ('.jpg', '.jpeg', '.png'))):
        sys.exit("Input and output must be .jpg, .jpeg, or .png")

    # Перевірка, чи розширення вхідного та вихідного файлів співпадають
    if input_path.split('.')[-1].lower() != output_path.split('.')[-1].lower():
        sys.exit("Input and output have different extensions")

    # Спроба відкрити вхідний файл
    try:
        input_image = Image.open(input_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Відкриття зображення футболки
    shirt_image = Image.open("shirt.png")

    # Зміна розміру та обрізка вхідного зображення під розмір футболки
    input_image = ImageOps.fit(input_image, shirt_image.size, method=0, bleed=0.0, centering=(0.5, 0.5))

    # Накладання зображення футболки на вхідне зображення
    input_image.paste(shirt_image, (0, 0), shirt_image)

    # Збереження результату
    input_image.save(output_path)
    print(f"Saved output to {output_path}")


if __name__ == "__main__":
    main()