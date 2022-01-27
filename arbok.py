from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import pandas as pd
import os, sys
from LoadModels import LoadModels
from Runner import run_model
from dotenv import load_dotenv
import multiprocessing as mp

application = Flask(__name__)
with application.app_context():
    #Load env vars
    env_path = os.path.join(os.getcwd(), '.env')
    load_dotenv(dotenv_path=env_path)
    #Loading models
    loadModel=LoadModels()
    model_objects=loadModel.pickle_models()
    #Create conda env
    #Activate conda env
    
@application.route('/calculate', methods=['POST'])
def calculate():
    #Processing request data
    payload = request.get_json()
    model_name = payload['model_name']
    inputs = payload['inputs']
    model = model_objects[model_name]
    #Spawing subprocess
    q = mp.Queue()
    p = mp.Process(target=run_model, args=(q, inputs, model, model_name))
    p.start()
    p.join()
    result=q.get()

    return jsonify(result)

if __name__ == '__main__':
    application.run()
