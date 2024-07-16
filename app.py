from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for Digimons
digimons = [
]

@app.route('/')
def home():
    sorted_digimons = sorted(digimons, key=lambda x: x['name'])
    return render_template('home.html', digimons=sorted_digimons)

@app.route('/add', methods=['GET', 'POST'])
def add_digimon():
    if request.method == 'POST':
        name = request.form.get('name')
        level = request.form.get('level')
        type = request.form.get('type')
        description = request.form.get('description')
        image_url = request.form.get('image_url')
        digimons.append({"name": name, "level": level, "type": type, "description": description, "image_url": image_url})
        return redirect(url_for('home'))
    return render_template('add_digimon.html')

if __name__ == '__main__':
    app.run(debug=True)
