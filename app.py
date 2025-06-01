from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ''
    input_json = ''

    if request.method == 'POST':
        input_json = request.form['json_input']
        try:
            config = json.loads(input_json)

            new_domains = [
                "geosite:category-ads-all",
                "geosite:google",
                "google.com"
            ]

            if 'routing' in config and 'rules' in config['routing']:
                for rule in config['routing']['rules']:
                    if 'user' in rule:
                        rule['domain'] = new_domains

            output = json.dumps(config, indent=2, ensure_ascii=False)
        except Exception as e:
            output = f"❌ خطا در پردازش JSON: {e}"

    return f"""
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <title>تبدیل JSON هوشمند</title>
    <style>
        body {{
            background: linear-gradient(to right, #1f4037, #99f2c8);
            font-family: 'Vazirmatn', sans-serif;
            direction: rtl;
            padding: 30px;
            color: #fff;
            text-align: center;
        }}
        textarea {{
            width: 90%;
            height: 300px;
            border-radius: 15px;
            padding: 10px;
            font-size: 14px;
            font-family: monospace;
            background: #2c3e50;
            color: #00ffae;
            border: none;
            margin-top: 10px;
        }}
        button {{
            margin-top: 10px;
            background-color: #16a085;
            color: white;
            padding: 10px 20px;
            border: none;
            font-family: 'Vazirmatn', sans-serif;
            font-size: 16px;
            border-radius: 10px;
            cursor: pointer;
        }}
        button:hover {{
            background-color: #138d75;
        }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Vazirmatn&display=swap" rel="stylesheet">
</head>
<body>
    <h1>🎯 تبدیل JSON به Routing باحال</h1>
    <form method="post">
        <textarea name="json_input" placeholder="اینجا JSON خود را بچسبانید...">{input_json}</textarea><br>
        <button type="submit">🔄 تبدیل</button>
    </form>

    {f'''
    <textarea id="output" readonly>{output}</textarea><br>
    <button onclick="copyOutput()">📋 کپی خروجی</button>
    <script>
        function copyOutput() {{
            const text = document.getElementById("output");
            text.select();
            text.setSelectionRange(0, 99999);
            document.execCommand("copy");
            alert("✅ خروجی با موفقیت کپی شد!");
        }}
    </script>
    ''' if output else ''}
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
