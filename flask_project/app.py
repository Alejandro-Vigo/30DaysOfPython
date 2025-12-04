from flask import Flask, render_template, request, redirect, url_for, session
import os
import collections

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'supersecretkey'

def analyze_text(text):
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    word_freq = collections.Counter(words)  
    most_common_words = word_freq.most_common(5) 
    unique_words = len(set(words))
    lexical_density = unique_words / num_words if num_words > 0 else 0

    return {
        'num_words': num_words,
        'num_chars': num_chars,
        'most_common_words': most_common_words,
        'lexical_density': round(lexical_density, 2)
    }

@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')

@app.route('/result')
def result():
    analysis = session.get('analysis', {}) 
    return render_template('result.html', analysis=analysis)

@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    
    if request.method == 'POST':
        content = request.form['content']
        session['analysis'] = analyze_text(content) 
        return redirect(url_for('result'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host='0.0.0.0', port=port)