#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'


@app.route('/bakeries')
def bakeries():
    bake = Bakery.query.all()
    responce  = [baking.to_dict() for baking in bake]

    return make_response(jsonify(responce), 200)


@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bake = Bakery.query.filter(Bakery.id==id).all()
    responce  = [baking.to_dict() for baking in bake]
    return make_response(jsonify(responce), 200)

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    bake = BakedGood.query.order_by(BakedGood.price.desc()).all()

    responce  = [baking.to_dict() for baking in bake]
    return make_response(jsonify(responce), 200)



@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    most_expensive = db.session.query(BakedGood).order_by(BakedGood.price.desc()).first()
    
    response = most_expensive.to_dict() if most_expensive else {}
    
    return make_response(jsonify(response), 200)



if __name__ == '__main__':
    app.run(port=5555, debug=True)
