from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store Not Found'}, 404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message': "Store with the name '{}' already exists.".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
            return store.json(), 201
        except:
            return {'message': 'Error occured ehile creating a store.'}, 500

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'Store deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}