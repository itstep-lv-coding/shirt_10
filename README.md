IT STEP Футболка
Приміряємо футболку
Завдання
У файлі під назвою shirt.py реалізуйте програму, яка очікує рівно два аргументи командного рядка:

- sys.argv[1] – ім'я (або шлях) до файлу JPEG або PNG, який буде відкритий як вхідний.
- sys.argv[2] – ім'я (або шлях) до файлу JPEG або PNG, який буде збережений як вихідний.

Програма повинна накласти зображення shirt.png (яке має прозорий фон) на вхідний файл після зміни розміру та обрізки вхідного зображення до потрібного розміру, зберігши результат як вихідний файл.
Інструкції
Відкрийте вхідний файл за допомогою функції Image.open з pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, змініть розмір і обріжте зображення за допомогою функції ImageOps.fit з pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, використовуючи значення за замовчуванням для method, bleed, та centering, накладіть зображення футболки за допомогою Image.paste з pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, та збережіть результат за допомогою Image.save з pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.
Програма повинна завершитись із sys.exit за умов:
- якщо користувач не вказав рівно два аргументи командного рядка,
- якщо імена вхідного і вихідного файлів не закінчуються на .jpg, .jpeg, або .png (незалежно від регістру),
- якщо розширення вхідного файлу відрізняється від розширення вихідного,
- якщо вказаний вхідний файл не існує.
Припущення
Припускається, що вхідне зображення буде фотографією людини, яка позує саме таким чином, щоб, після зміни розміру та обрізки, футболка виглядала так, ніби вона надіта ідеально.
Як тестувати
Ось як можна вручну перевірити ваш код:

- Запустіть програму з командою python shirt.py. Ваша програма повинна завершитись з повідомленням sys.exit:
  Too few command-line arguments

- Завантажте muppets.zip і розархівуйте колекцію фотографій ляльок за допомогою unzip muppets.zip. Запустіть програму з python shirt.py before1.jpg before2.jpg before3.jpg. Ваша програма повинна вивести:
  Too many command-line arguments

- Запустіть програму з python shirt.py before1.jpg invalid_format.bmp. Програма повинна завершитись з повідомленням:
  Invalid output

- Запустіть програму з python shirt.py before1.jpg after1.png. Програма повинна завершитись з повідомленням:
  Input and output have different extensions

- Запустіть програму з python shirt.py non_existent_image.jpg after1.jpg. Програма повинна завершитись з повідомленням:
  Input does not exist

- Запустіть програму з python shirt.py before1.jpg after1.jpg. Я
