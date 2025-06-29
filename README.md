## 📄 README.md для проекта `PDFExtractorApp`

Это приложение на Python, которое позволяет:
- **Извлечь первую страницу из каждого PDF-файла** в выбранной папке
- **Создать новый PDF-документ**, содержащий все первые страницы
- **Добавить текстовую страницу с именем исходного файла**

Приложение использует библиотеки:
- `PyPDF2` — для работы с PDF-файлами
- `reportlab` — для создания текстовых страниц
- `tkinter` — для графического интерфейса

---

### 🛠️ Технологии

| Компонент | Версия / Использование |
|-----------|------------------------|
| Python    | 3.10+                  |
| PyPDF2    | 3.0.1                  |
| reportlab | 3.7.0                  |
| tkinter   | стандартная библиотека  |

---

### 📁 Структура проекта

```
pdf_extractor/
├── pdf_extractor.py       # Основной скрипт
├── requirements.txt     # Зависимости
└── README.md            # Этот файл
```

---

### 🚀 Запуск

#### 1. Установите зависимости:

```bash
pip install PyPDF2 reportlab
```

#### 2. Запустите приложение:

```bash
python pdf_extractor.py
```

---

### 🖱️ Использование

1. Нажмите **"Выбрать папку"**, чтобы выбрать папку с PDF-файлами.
2. Нажмите **"Исходный файл"**, чтобы указать место для сохранения нового PDF-документа.
3. Нажмите **"Собрать первые страницы"**, чтобы запустить процесс.

После завершения вы получите новый PDF-файл, содержащий:
- Первые страницы всех исходных PDF-документов
- Дополнительную текстовую страницу с названием исходного файла

---

### 🧾 Функционал

#### ✅ Основные функции:
- Выбор папки с PDF-файлами
- Выбор места для сохранения результирующего файла
- Извлечение первой страницы из каждого PDF
- Создание текстовой страницы с именем файла
- Сохранение всех данных в один PDF-документ

#### ✅ Дополнительно:
- Логирование ошибок и действий через `logging`
- Обработка исключений
- Проверка наличия PDF-файлов
- Отображение сообщений пользователю через `messagebox`

---

### 🧩 Пример использования

Предположим, у вас есть папка `input_pdfs`, содержащая следующие файлы:
- `file1.pdf`
- `file2.pdf`
- `file3.pdf`

После выполнения:
- В папке `output` будет создан файл `all_first_pages.pdf`
- В этом файле будут находиться:
  - Первая страница `file1.pdf`
  - Текстовая страница: `"Source File: file1.pdf"`
  - Первая страница `file2.pdf`
  - Текстовая страница: `"Source File: file2.pdf"`
  - ... и так далее

---

### 🧩 Кодовые особенности

- Используется `PdfWriter` для объединения документов
- Для создания текстовой страницы используется `reportlab.pdfgen.canvas`
- Логирование реализовано через `logging`
- Используются `tkinter` для GUI-интерфейса

---

### 🧾 Логи

Все действия записываются в лог-файл или выводятся в консоль (если запущено в режиме отладки).

Пример лога:

```
2025-06-15 14:30:45,123 - INFO - Found 3 PDF files in input_pdfs
2025-06-15 14:30:45,123 - INFO - Processing file1.pdf
2025-06-15 14:30:45,123 - INFO - Extracted the first page from file1.pdf
2025-06-15 14:30:45,123 - INFO - All first pages saved to output/all_first_pages.pdf
```

---

### 🧩 Ошибки и ограничения

| Ошибка | Решение |
|--------|---------|
| ❌ Не найдены PDF-файлы | Убедитесь, что папка содержит `.pdf`-файлы |
| ❌ Не указан выходной файл | Нажмите "Исходный файл", чтобы выбрать место для сохранения |
| ❌ Ошибка при создании текстовой страницы | Проверьте установку `reportlab` |
| ❌ Неверный формат PDF | Приложение работает только с PDF, поддерживаемыми `PyPDF2` |

---

### 📝 Автор

**Кудрявцев Данил**  
Системный администратор IT-отдела  
Email: mikushkinodanil4@gmail.com

---

### 📝 Лицензия

MIT License

Copyright (c) 2025 Кудрявцев Данил

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
