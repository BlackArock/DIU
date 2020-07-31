#!/usr/bin/python
# -*- coding: utf-8 -*-

# encoding=utf8
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import datetime
import json


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://LitoralDev:calculus864@litoraldev.mooo.com:27047/diu"
#app.config['MONGO_PORT'] = '27047'
#app.config['MONGO_DBNAME'] = 'diu'
#app.config['MONGO_USERNAME'] = 'LitoralDev'
#app.config['MONGO_PASSWORD'] = 'calculus864'

mongo = PyMongo(app)


@app.route('/retenciones', methods=['POST'])
def create_retencion():
    fecha = request.json['fecha']
    fecha_iso = datetime.datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S.000Z")
    tipoRetencion =  request.json['tipoRetencion']
    cuit = request.json['cuit']
    nroConstancia = request.json['nroConstancia']
    importe = request.json['importe']
    if fecha and cuit and nroConstancia:
        id = mongo.db.retenciones.insert(
            {'fecha': fecha_iso, 'tipoRetencion': tipoRetencion, 'cuit': cuit, 'nroConstancia': nroConstancia, 'importe': importe})
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
    retencion = mongo.db.retenciones.find({'cuit': str(cuit) })
    response = json_util.dumps(retencion)
    return Response(response, mimetype="application/json")

@app.route('/retenciones/<id>', methods=['DELETE'])
def delete_retencion(id):
    mongo.db.retenciones.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'Retencion ' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response


@app.route('/retenciones/<_id>', methods=['PUT'])
def update_retenciones(_id):
    fecha = request.json['fecha']
    cuit = request.json['cuit']
    tipoRetencion = request.json['tipoRetencion']
    nroConstancia = request.json['nroConstancia']
    importe = request.json['importe']

    if fecha and cuit and nroConstancia and _id:        
        mongo.db.retenciones.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
            {'$set': {'fecha': fecha, 'cuit': cuit, 'tipoRetencion': tipoRetencion, 'nroConstancia': nroConstancia, 'importe': importe}})
        response = jsonify({'message': 'Retencion' + _id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
      return not_found()

# Percepciones !

@app.route('/percepciones', methods=['POST'])
def create_percepcion():
    fecha = request.json['fecha']
    fecha_iso = datetime.datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S.000Z")
    cuit = request.json['cuit']
    tipoPercepcion =  request.json['tipoPercepcion']
    tipoComprobante = request.json['tipoComprobante']
    nroComprobante = request.json['nroComprobante']
    letra = request.json['letra']
    importe = request.json['importe']
    if fecha and cuit and nroComprobante:
        id = mongo.db.percepciones.insert(
            {'fecha': fecha_iso, 'cuit': cuit, 'tipoPercepcion': tipoPercepcion, 'tipoComprobante': tipoComprobante,'nroComprobante': nroComprobante, 'letra': letra, 'importe': importe})
        response = jsonify({
            '_id': str(id),
            'fecha': fecha,            
            'cuit': cuit,
            'tipoPercepcion': tipoPercepcion,
            'tipoComprobante': tipoComprobante,
            'nroComprobante': nroComprobante,
            'letra' : letra,
            'importe': importe})
        response.status_code = 201
        return response
    else:
        return not_found()
    
@app.route('/percepciones', methods=['GET'])
def get_percepciones():
    percepciones = mongo.db.percepciones.find()
    response = json_util.dumps(percepciones)
    return Response(response, mimetype="application/json")


@app.route('/percepciones/<id>', methods=['GET'])
def get_percepcion(id):
    print(id)
    percepcion = mongo.db.percepciones.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(percepcion)
    return Response(response, mimetype="application/json")

@app.route('/percepciones/cuit/<cuit>', methods=['GET'])
def get_percepcion_cuit(cuit):
    print(cuit)
    percepcion = mongo.db.percepcion.find({'cuit': str(cuit) })
    response = json_util.dumps(percepcion)
    return Response(response, mimetype="application/json")

@app.route('/percepciones/<id>', methods=['DELETE'])
def delete_percepcion(id):
    mongo.db.percepciones.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'Percepcion' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response

@app.route('/percepciones/<_id>', methods=['PUT'])
def update_percepcion(_id):
    fecha = request.json['fecha']
    cuit = request.json['cuit']
    tipoPercepcion = request.json['tipoPercepcion']
    tipoComprobante = reques.json['tipoComprobante']
    nroComprobante = request.json['nroComprobante']
    letra = request.json['letra']
    importe = request.json['importe']

    if fecha and cuit and nroComprobante and _id:        
        mongo.db.percepciones.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, 
            {'$set': {'fecha': ISODate(fecha), 'cuit': cuit, 'tipoPercepcion': tipoPercepcion, 'nroComprobante': nroComprobante, 'letra': letra, 'importe': importe}})
        response = jsonify({'message': 'Percepcion ' + _id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
      return not_found()



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
    app.run(debug=True, host='0.0.0.0', port=27050)