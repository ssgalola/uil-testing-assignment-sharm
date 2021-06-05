from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

triangle_sides = []
# a, b, c = [float(i) for i in triangle_sides[0]]


def get_sides():
    triangle_sides.clear()
    
    get_sides_url = "http://13.212.56.51:8080/get-sides"
    data = requests.get(get_sides_url)
    data_json = data.json()
    triangle_sides.append(data_json['sides'])
    return 
    

def compute_perimeter(sides):
    # get_sides()
    a, b, c = [float(i) for i in sides]
    perimeter = a + b + c
    return float(perimeter)
    

def compute_area(sides):
    # get_sides()
    a, b, c = [float(i) for i in sides]
    
    p = a + b + c
    s = p / 2
    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
    
    
@app.route('/perimeter', methods=['get'])
def get_perimeter():
    get_sides()
    
    if (len(triangle_sides) == 1):
        response = {
            'perimeter': compute_perimeter(triangle_sides[0])
        }
    
        triangle_sides.clear()
        return json.dumps(response), 200
    
    else:
        return 'Please input proper sides of triangle', 400
    
    
@app.route('/area', methods=['get'])
def get_area():
    get_sides()
    
    if (len(triangle_sides) == 1):
        response = {
            'area': compute_area(triangle_sides[0])
        }
        
        triangle_sides.clear()
        return json.dumps(response), 200
    
    else:
        return 'Please input proper sides of triangle', 400


@app.route('/area-and-perimeter', methods=['get'])
def get_area_and_perimeter():
    get_sides()
    
    if (len(triangle_sides) == 1):
        response = {
            'area': compute_area(triangle_sides[0]),
            'perimeter': compute_perimeter(triangle_sides[0])
        }
    
        triangle_sides.clear()
        return json.dumps(response), 200
    
    else:
        return 'Please input proper sides of triangle', 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8081')