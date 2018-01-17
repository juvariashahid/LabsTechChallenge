from flask import Flask, render_template

app = Flask(__name__)


@app.route('/js5160', methods=['GET'])
def main()
    return render_template('adilabs.html')


if __name__ == '__main__':
    app.run()

