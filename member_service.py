from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Product Class/Model
class Member(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  name = db.Column(db.String(100), unique=True)
  memclass = db.Column(db.String(200))
  access = db.Column(db.Float)
  tools = db.Column(db.String)

  def __init__(self, name, memclass, access, qty):
    self.name = name
    self.memclass = memclass
    self.access = access
    self.tools = tools

# Product Schema
class MemberSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'memclass', 'access', 'tools')

# Init schema
member_schema = MemberSchema(strict=True)
members_schema = MemberSchema(many=True, strict=True)

# Create a Product
@app.route('/member', methods=['POST'])
def add_product():
  name = request.json['name']
  memclass = request.json['memclass']
  access = request.json['access']
  qty = request.json['tools']

  new_member = Member(name, memclass, access, tools)

  db.session.add(new_member)
  db.session.commit()

  return product_schema.jsonify(new_member)

# Get All Members
@app.route('/member', methods=['GET'])
def get_products():
  all_members = Product.query.all()
  result = members_schema.dump(all_members)
  return jsonify(result.data)

# Get Single Member
@app.route('/member/<id>', methods=['GET'])
def get_member(id):
  member = Member.query.get(id)
  return member_schema.jsonify(member)

# Update a Member
@app.route('/member/<id>', methods=['PUT'])
def update_member(id):
  member = Member.query.get(id)

  name = request.json['name']
  memclass = request.json['memclass']
  access = request.json['access']
  tools = request.json['tools']

  member.name = name
  member.memclass = memclass
  member.access = access
 member.tools = tools

  db.session.commit()

  return member_schema.jsonify(member)

# Delete Member
@app.route('/member/<id>', methods=['DELETE'])
def delete_member(id):
  member = Product.query.get(id)
  db.session.delete(member)
  db.session.commit()

  return member_schema.jsonify(member)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)