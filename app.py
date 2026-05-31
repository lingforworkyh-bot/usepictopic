import os
from pathlib import Path
from flask import Flask, request, render_template, jsonify
from feature_extractor import FeatureExtractor
from database import PartDatabase

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = Path('uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['CACHE_PATH'] = Path('feature_cache') / 'database.pkl'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('feature_cache', exist_ok=True)

extractor = None
db = PartDatabase()
ready = False


def init():
    global extractor, db, ready
    print("Loading model...")
    extractor = FeatureExtractor()

    cache_path = app.config['CACHE_PATH']
    if cache_path.exists():
        print("Loading cache...")
        db.load(str(cache_path))
        ready = True
        print(f"Ready: {len(db.records)} parts loaded")
    else:
        print("No cache found. Run locally first to build database.")


@app.route('/')
def index():
    count = len(db.records) if ready else 0
    return render_template('index.html', ready=ready, count=count)


@app.route('/search', methods=['POST'])
def search():
    if not ready:
        return jsonify({'error': 'Database not ready'}), 400

    if 'photo' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['photo']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    ext = Path(file.filename).suffix or '.jpg'
    save_path = app.config['UPLOAD_FOLDER'] / f'query{ext}'
    file.save(str(save_path))

    try:
        query_feat = extractor.extract(str(save_path))
        results = db.search(query_feat, top_k=3)
        return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


init()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
