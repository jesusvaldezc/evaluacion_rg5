# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, jsonify
import csv
import glob

app = Flask(__name__, static_url_path="")

@app.route('/', methods=['GET'])
def ejemplo_json():

    csv_files = glob.glob('data/*.csv')
    lista = []
    if len(csv_files) == 0:
        response = {"No hay archivos csv por convertir a json" : 400}
        return response
    else:
        while len(csv_files) > 0:
            csv_path = csv_files.pop()
            with open(csv_path,'r') as myFile:
                reader = csv.DictReader(myFile)
                for rows in reader:
                    lista.append(rows)

        return jsonify(lista)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port='5050')
