from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()


@app.route('/')
def home():
    return render_template("index.html", blogs=response)


@app.route('/post/<blog_id>')
def blog_id(blog_id):
    title = response[int(blog_id)]['title']
    subtitle = response[int(blog_id)]['subtitle']
    body = response[int(blog_id)]['body']
    return render_template('post.html', title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
