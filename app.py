from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Rs.10000"
  },
  {
    "id": 2,
    "title": "Data Scientist",
    "location": "Delhi, India",
    "salary": "Rs.15000"
  },
  {
    "id": 3,
    "title": "Frontend Engineer",
    "location": "Remote",
    "salary": "$20000"
  },
  {
    "id": 4,
    "title": "Backend Engineer",
    "location": "Remote",
    "salary": "$25000"
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Jovian")

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)