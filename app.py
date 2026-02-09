from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/make_call', methods=['POST'])
def make_call():
    # Abhi ke liye sirf "Testing" message bhej rahe hain
    return jsonify({"status": "success", "message": "Call initiated (Test Mode)"})

if __name__ == '__main__':
    app.run(debug=True)