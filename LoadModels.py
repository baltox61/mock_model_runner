import os
import glob
import pickle as p

class LoadModels(object):
    def __init__(self):
        self.model_objects = {}
        self.pkl_model=None
        self.pkl_model_obj_len=None
        self.picklefiles = glob.glob(os.environ['MODEL_PATH'] +  '/*/*.pkl' )
        self.pkl_model_name=None
        self.ext = None
    def pickle_models(self):
        print('Loading Pickle Files')
        try:
            for modelfile in self.picklefiles:
                self.pkl_model = p.load(open(modelfile, 'rb'))
                (self.pkl_model_name, self.ext)=os.path.splitext(os.path.basename(modelfile))
                self.model_objects.update({self.pkl_model_name: self.pkl_model})
            self.pkl_model_obj_len = str(len(self.model_objects))
        except:
            print("Error loading pickle files")
        print('Pickle Files Loaded: ' + self.pkl_model_obj_len)
        return self.model_objects
