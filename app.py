#!/usr/bin/python
# -*- coding: utf-8 -*-

# encoding=utf8
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://LitoralDev:calculus864@litoraldev.mooo.com:27047/diu"
#app.config['MONGO_PORT'] = '27047'
#app.config['MONGO_DBNAME'] = 'diu'
#app.config['MONGO_USERNAME'] = 'LitoralDev'
#app.config['MONGO_PASSWORD'] = 'calculus864'

mongo = PyMongo(app)


@app.route('/retenciones', methods=['POST'])
def create_retenciones():
    fecha = request.json['fecha']
    tipoRetencion =  request.json['tipoRetencion']
    cuit = request.json['CUIT']
    nroConstancia = request.json['nroConstancia']
    importe = request.json['importe']
    if fecha and cuit and nroConstancia:
        id = mongo.db.retenciones.insert(
            {'fecha': fecha, 'tipoRetencion': tipoRetencion, 'cuit': cuit, 'nroConstancia': nroConstancia, 'importe': importe})
        response = jsonify({
            '_id': str(id),
            'fecha': fecha,
            'tipoRetencion': tipoRetencion,
            'cuit': cuit,
            'nroConstancia': nroConstancia,
            'importe': importe})
        response.status_code = 201
        return response
    else:
        return not_found()
    
@app.route('/retenciones', methods=['GET'])
def get_retenciones():
    retenciones = mongo.db.retenciones.find()
    response = json_util.dumps(retenciones)
    return Response(response, mimetype="application/json")


@app.route('/retenciones/<id>', methods=['GET'])
def get_retencion(id):
    print(id)
    retencion = mongo.db.uretenciones.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(retencion)
    return Response(response, mimetype="application/json")

@app.route('/retenciones/cuit/<cuit>', methods=['GET'])
def get_retencion_cuit(cuit):
    print(cuit)
    retencion = mongo.db.retenciones.find({'CUIT': str(cuit) })
    response = json_util.dumps(retencion)
    return Response(response, mimetype="application/json")

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})



@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000)