from flask import Flask, jsonify
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

class Books(Resource):
    def get(self):
        headers = {
            'X-RapidAPI-Key': '76847fd9c9msheea5d2fc19e1bbdp182b79jsnfece3f89fc6e',
            'X-RapidAPI-Host': 'all-books-api.p.rapidapi.com'
        }
        api_url = 'https://all-books-api.p.rapidapi.com/getBooks'
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            print(response.json)
            books_data = response.json()
            return jsonify({'status': 'success', 'data': books_data}), 200
        else:
            return jsonify({'status': 'error', 'message': 'Failed to fetch book data'}), 500

api.add_resource(Books, '/books')

if __name__ == '__main__':
    app.run(debug=True)

