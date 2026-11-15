from flask import Flask, request, jsonify

app = Flask(__name__)

connected_pcs = {}

@app.route('/api/update', methods=['POST'])
def update_status():
    data = request.json
    pc_name = data.get('pc_name')
    
    if pc_name:
        connected_pcs[pc_name] = data  # ලැබෙන සියලුම විස්තර ඩික්ෂනරි එක ලෙස සේව් කරයි
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error"}), 400

@app.route('/api/pcs', methods=['GET'])
def get_pcs():
    return jsonify(connected_pcs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
