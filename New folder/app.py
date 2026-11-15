from flask import Flask, request, jsonify

app = Flask(__name__)

# අනිත් PC වලින් එවන ස්ටේටස් මෙතන තාවකාලිකව සේව් වෙනවා
connected_pcs = {}

@app.route('/api/update', methods=['POST'])
def update_status():
    data = request.json
    pc_name = data.get('pc_name')
    status = data.get('status')
    
    if pc_name:
        connected_pcs[pc_name] = {
            "status": status,
            "ip": request.remote_addr
        }
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error"}), 400

@app.route('/api/pcs', methods=['GET'])
def get_pcs():
    # Master PC එකෙන් මේකට රික්වෙස්ට් කරලා අනිත් PC වල විස්තර බලාගන්න පුළුවන්
    return jsonify(connected_pcs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
