from flask import Flask, request, jsonify
from clear_db import clear_table
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Database Reset API',
        'endpoints': {
            'POST /clear': 'Clear the database table',
            'GET /': 'Show this info'
        }
    })

@app.route('/clear', methods=['POST'])
def clear_database():
    try:
        success, message = clear_table()
        
        if success:
            return jsonify({
                'status': 'success',
                'message': message
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': message
            }), 500
            
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Unexpected error: {str(e)}'
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'database_url': 'configured' if os.getenv('DATABASE_URL') else 'missing',
        'table_name': os.getenv('TABLE_NAME', 'people')
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
