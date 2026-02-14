from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    fio = "Анна Малиновски"
    age = 30
    profession = "Психолог"

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Профиль</title>
        <style>
            body {
                font-family: Arial;python app.py

                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .card {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                text-align: center;
            }
            h1 { margin-bottom: 10px; }
            p { font-size: 18px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{{ fio }}</h1>
            <p>Возраст: {{ age }}</p>
            <p>Профессия: {{ profession }}</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, fio=fio, age=age, profession=profession)

if __name__ == "__main__":
    app.run(debug=True)
