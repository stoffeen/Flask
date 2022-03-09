from flask import Flask, render_template
from app.dynamodb_access import get_all_readings, get_item_by_attribute


app = Flask(__name__)


@app.get('/')
def index():
    readings = get_all_readings()
    return render_template('index.html', readings=readings)

@app.get("/graph")
def graph():

    # Sovrum
    items = get_item_by_attribute('sensor', "Sovrum")
    items.sort(key=lambda item: item['datetime'])
    labels = [row['datetime'] for row in items]
    values = [int (row['temp']) for row in items]
    
    # Kök
    items2 = get_item_by_attribute('sensor', "Kök")
    items2.sort(key=lambda item: item['datetime'])
    labels2 = [row['datetime'] for row in items2]
    values2 = [int (row['temp']) for row in items2]

    # Vardagsrum
    items3 = get_item_by_attribute('sensor', "Vardagsrum")
    items3.sort(key=lambda item: item['datetime'])
    labels3 = [row['datetime'] for row in items3]
    values3 = [int (row['temp']) for row in items3]

    # Toalett
    items4 = get_item_by_attribute('sensor', "Toalett")
    items4.sort(key=lambda item: item['datetime'])
    labels4 = [row['datetime'] for row in items4]
    values4 = [int (row['temp']) for row in items4]


    return render_template("graph.html", labels=labels, values=values, labels2=labels2, values2=values2, labels3=labels3, values3=values3, labels4=labels4, values4=values4)