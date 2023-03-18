from flask import Flask, render_template, request

app = Flask(__name__)

CLASS = [
  "24/01",
  "24/02",
  "24/03",
  "24/04",
  "24/05",
  "24/06",
  "24/07",
  "24/08",
  "24/09",
  "24/10",
  "24/11",
  "24/12",
  "24/13",
  "24/14",
  "24/15",
  "24/16",
  "24/17",
  "24/18",
  "24/19",
  "24/20",
  "24/21",
  "24/22",
  "24/23",
  "24/24",
  "24/25",
  "24/26",
  "24/27",
  "24/28",
  "24/29",
  "24/30",

]

CCA = [
        "Basketball",
        "Football",
        "Frisbee",
        "Badminton",
        "Hockey",
        "Netball",
        "Shooting",
        "Table_Tennis",
        "Taekwondo",
        "Tennis",
        "Touch Rugby",
        "Volleyball",
        "Chinese_Orchestra",
        "Choir",
        "Dance_Society",
        "StageWorks",
        "Guitar_Ensemble",
        "Harmonica_Band",
        "Symphonic_Band",
        "Visual_Aids_Club",
        "Chinese_LDDS",
        "Debate",
        "Community_Champions_Council",
        "Outdoor_Activities_Club",
        "Photographic_Society",
        "Red_Cross_Youth",
        "STEM",
        "Strategist_Society",
        "Students’_Council",
        "Tamil_LDDS",
]

@app.route("/", methods=['GET', 'POST'])
def front():
    return render_template("front.html")

@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template("index.html", sport=CCA, clas=CLASS)

@app.route("/success", methods=['POST'])
def success():
  name = None
  cca = None
  Class = None
  improv = None
  name = request.form.get("name")
  cca = request.form.get("cca")
  Class = request.form.get("class")
  improv = request.form.get("improv")
  with open('suggest.txt', 'a') as file:
      file.write(name + ' ' + cca + ' ' + Class + ' '  + improv + ' \n')
  return render_template("success.html")

@app.route("/cca", methods=['GET', 'POST'])
def cca():
    return render_template("cca.html", sport=CCA, clas=CLASS)

@app.route("/register", methods=["POST"])
def register():
  name = None
  gender = None
  Class = None
  choice1 = None
  choice2 = None
  choice3 = None
  name = request.form['name']
  gender = request.form['gender']
  Class = request.form['class']
  choice1 = request.form['c1']
  choice2 = request.form['c2']
  choice3 = request.form['c3']
  if choice1 == choice2 == choice3:
    return render_template("failure1.html")
  elif Class not in CLASS:
    return render_template("failure3.html")
  else:
    with open('data.txt', 'a') as file:
      file.truncate(0)
      file.write(name + ' ' + gender + ' ' + Class + ' '  + "1." + ' ' + choice1 + ' ' + "ㅤ" + "2." + ' ' + choice2 + ' ' + "3." + ' ' + choice3 + ' \n')
    return render_template("registered.html")


@app.route("/mycca", methods=['GET', 'POST'])
def mycca():
    with open('data.txt', 'r') as f:
      data = f.read() 
      if len(data) == 0:
        choice = "(Unregistered)"
      else:  
        data = data.split(" ")
        choice = data[4]
        
    return render_template("mycca.html", sport=CCA, clas=CLASS, choice=choice)








app.run(host='0.0.0.0', port=81)
