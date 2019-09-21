# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from sklearn.externals import joblib
from flask_cors import CORS, cross_origin
from pandas import pandas
import json

app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "*"}})

CORS(app)


@app.route('/predict',  methods=['POST'])
#@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

def predict():
    
     encoderFileName = 'encoder.sav'
     filename = 'finalized_model.sav'
     loaded_model = joblib.load(filename)
     loaded_encoder = joblib.load(encoderFileName)    
     battleData = request.get_json()
     
     battleDataFramePandas = pandas.DataFrame(data=battleData, columns=["id", "Type1","Type2","HP","Attack","Defense","SpAtk","SpDef","Speed","Legendary","id_2", "Type1_2","Type2_2","HP_2","Attack_2","Defense_2","SpAtk_2","SpDef_2","Speed_2","Legendary_2"])
     battleDataFramePandasDropID = battleDataFramePandas.drop(["id","id_2"], axis=1)
    
     result = loaded_model.predict(loaded_encoder.transform(battleDataFramePandasDropID))
     
     print(result)
     
     print (result[0] == 0)
     
     if (result[0] == 0):
         winner = battleDataFramePandas.id.tolist()[0]
     else:
         winner = battleDataFramePandas.id_2.tolist()[0]
     
     return jsonify({'Winner': winner});
     
     #return jsonify([{'Winner': result}])

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
     # jsonified = json.dumps(battleData)
     #battleDataEval = eval(jsonified)
   #  battleDataFormat = json.dumps(battleDataEval)
    # battleDataJson = pandas.read_json(jsonified)
    # battleDataPd = pandas.read_json(battleData)