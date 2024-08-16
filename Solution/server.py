from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
        <head>
            <title>Personnalisation de T-shirts</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    margin: 0;
                    padding: 20px;
                    text-align: center;
                }}
                h1 {{
                    color: #333;
                }}
                form {{
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    display: inline-block;
                }}
                input[type="text"] {{
                    width: 80%;
                    padding: 10px;
                    margin: 10px 0;
                    border-radius: 4px;
                    border: 1px solid #ccc;
                }}
                input[type="submit"] {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }}
                input[type="submit"]:hover {{
                    background-color: #45a049;
                }}
                .container {{
                    max-width: 600px;
                    margin: auto;
                    padding: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Bienvenue sur notre site de personnalisation de t-shirts</h1>
                <form action="/preview" method="get">
                    <label for="user_text">Entrez le texte à afficher sur le t-shirt:</label><br>
                    <input type="text" id="user_text" name="user_text" required><br>
                    <input type="submit" value="Prévisualiser">
                </form>
            </div>
        </body>
        </html>
    '''

@app.route('/preview', methods=['GET'])
def preview():
    user_text = request.args.get("user_text") or None

    template = '''
        <html>
        <head>
            <title>Prévisualisation de votre T-shirt</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    margin: 0;
                    padding: 20px;
                    text-align: center;
                }}
                h1 {{
                    color: #333;
                }}
                .preview-container {{
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    display: inline-block;
                    position: relative;
                    text-align: center;
                }}
                .preview-container img {{
                    max-width: 100%;
                    border-radius: 8px;
                    display: block;
                }}
                .text-overlay {{
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    font-size: 24px;
                    color: white;
                    font-weight: bold;
                    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
                    white-space: nowrap;
                }}
                .button {{
                    margin-top: 20px;
                    display: inline-block;
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    text-decoration: none;
                    border-radius: 4px;
                }}
                .button:hover {{
                    background-color: #45a049;
                }}
            </style>
        </head>
        <body>
            <div class="preview-container">
                <h1>Prévisualisation de votre t-shirt</h1>
                <div class="text-overlay">{{user_text}}</div>
                <img src="/static/tshirt_template.jpg" alt="T-shirt"/>
                <br>
                <a href="/" class="button">Revenir</a>
            </div>
        </body>
        </html>
    '''

    return render_template_string(template).render(user_text=user_text) # Add render(user_text=user_text) to avoid SSTI vulnerability

if __name__ == '__main__':
    app.run(debug=True)