from program import main
from flask import Flask, render_template, request
from io import StringIO
import sys

# Init
app = Flask(__name__)

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout

@app.route('/')
def app_form():
    return render_template('form.html', template_folder='templates')

@app.route('/', methods=['POST'])
def app_form_text():
    text = request.form['u']
    with Capturing() as output:
        main(text)
    
    fin_test = output
    return render_template('result.html', template_folder='templates', fin_test=fin_test)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)