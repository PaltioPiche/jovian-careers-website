from flask import Flask, render_template, jsonify

app = Flask(__name__)

MEMB = [{
  'id': 1,
  'title': 'Senior Membership',
  'location': 'NYC, NY',
  'cost': '$45.00'
}, {
  'id': 2,
  'title': 'Junior Membership',
  'location': 'Brooklyn, NY',
  'cost': '$35.00'
}, {
  'id': 3,
  'title': 'Family Membership',
  'location': 'Queens, NY',
  'cost': '$90.00'
}, {
  'id': 4,
  'title': 'Remote Membership',
  'location': 'Houston, TX',
}]


@app.route("/")
def hello_world():
  return render_template('home.html', memb=MEMB, company_name='Cule!')


@app.route("/api/memb")
def list_memb():
  return jsonify(MEMB)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
