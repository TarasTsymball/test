from flask import Flask, render_template, request, send_file
import pdfkit
import tempfile
import os

app = Flask(__name__)

def html_to_pdf(html_content, output_pdf_path):
    try:
        # Опции для конвертации
        options = {
            'page-size': 'A4',
            'margin-top': '0mm',
            'margin-right': '0mm',
            'margin-bottom': '0mm',
            'margin-left': '0mm',
        }

        # Путь к исполняемому файлу wkhtmltopdf
        wkhtmltopdf_path = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'

        # Конфигурация pdfkit
        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

        # Конвертация HTML в PDF
        pdfkit.from_string(html_content, output_pdf_path, configuration=config, options=options)

        print(f'Конвертация успешно завершена. PDF сохранен по пути: {output_pdf_path}')

    except Exception as e:
        print(f'Произошла ошибка при конвертации: {str(e)}')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        html_content = request.form.get('html_content')
        if html_content:
            # Создаем временный файл для PDF
            temp_pdf_fd, temp_pdf_path = tempfile.mkstemp(suffix='.pdf')
            os.close(temp_pdf_fd)

            # Конвертируем HTML в PDF
            html_to_pdf(html_content, temp_pdf_path)

            # Отправляем PDF-файл клиенту
            return send_file(temp_pdf_path, as_attachment=True, download_name='output.pdf')

    # Отображаем форму для ввода HTML-кода
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
