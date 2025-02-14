from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

temps_data = []  # Stores (temperature, timestamp)

@app.route('/store')
def store_data():
    data_given = request.args.get('data', default=0, type=int)
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    temps_data.append((data_given, timestamp))
    return f"Temperature {data_given} stored at {timestamp}"

@app.route('/show_data')
def show_data():
    if not temps_data:
        return "No data available."
    
    return "\n".join([f"Temperature: {temp}, Timestamp: {timestamp}<br>" for temp, timestamp in temps_data])


@app.route('/show_stats')
def show_stats():
    if not temps_data:
        return "No data available."
    
    temps = [temp for temp, _ in temps_data]
    min_temp = min(temps)
    max_temp = max(temps)
    avg_temp = sum(temps) / len(temps)
    
    return f"Min Temperature: {min_temp}<br>Max Temperature: {max_temp}<br>Average Temperature: {avg_temp}"


if __name__ == '__main__':
    app.run(debug=True, port=8080)

