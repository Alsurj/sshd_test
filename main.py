#from fastapi import FastAPI
#from pydantic import Basemodel
import numpy
import os, glob

#app = FastAPI()

# list all .npz files
npzfiles = [f for f in glob.glob('../FCGF_docker/data/threedmatch/*.npz')]
## other approach
#for file in glob.glob("*.npz"):
#    npzfiles.append(file)

#class train_data(BaseModel):
#    name: str
#    sequences: str
#    batch_num: int

#@app.get(/dataset)
#def get_dataset():
#    results= []
