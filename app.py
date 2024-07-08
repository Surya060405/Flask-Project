from flask import Flask , render_template , jsonify
app = Flask(__name__)
JOBS = [{'id' : 1, 'title' : 'Data Analyst' , 'location' : 'Bengaluru'},{'id' : 2, 'title' : 'Data Scientist' , 'location' : 'Delhi'},{'id' : 3, 'title' : 'Frontend Developer' , 'location' : 'Hyderabad'}]
@app.route('/')
def hello_world():
    return render_template("design.html",jobs = JOBS ) 
@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host='127.0.0.1' , port=5000 , debug=True)