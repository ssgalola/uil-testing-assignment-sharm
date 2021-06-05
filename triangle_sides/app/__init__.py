from flask import Flask, request, jsonify
import json

app = Flask(__name__)

triangle_sides = []


def checker(sides):
    is_a_triangle = False
    
    if (len(sides) == 3):
        a, b, c = [float(i) for i in sides]
        
        if (a + b + c > 0):
            if (a + b > c) and (a + c > b) and (b + c > a):
                is_a_triangle = True
            
    return is_a_triangle
    
    
@app.route('/check-sides', methods=['post'])
def check_sides():
    request_sides = request.json['sides']
    
    if checker(request_sides):
        triangle_sides.append(request_sides)
        return 'Sides form a triangle', 200
    
    else:
        return 'Not a triangle', 400
    

@app.route('/get-sides', methods=['get'])
def get_sides():
    
    if (len(triangle_sides) == 1):
        response = {
            'sides': triangle_sides[0]
        }
        
        triangle_sides.clear()
        return json.dumps(response), 200
    
    else:
        return 'Please input sides of triangle', 400
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')