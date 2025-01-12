from flask import Flask, request, redirect, render_template
import random, string

app = Flask(__name__)
shortened_urls = {}

def url_gen(size=8):
    char = string.ascii_letters + string.digits
    return ''.join(random.choice(char) for _ in range(size))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['or_url']
        short_url = url_gen()

        while short_url in shortened_urls:
            short_url = url_gen()

        shortened_urls[short_url] = original_url
        return f"Shortened URL: {request.host_url}{short_url}"
    
    return render_template('url_shortener_index.html')

@app.route('/<short_url>')
def redirect_url(short_url):
    long_url = shortened_urls.get(short_url)
    if long_url:
        return redirect(long_url)
    return f"URL not found"

if __name__ == '__main__':
    app.run(debug=True)