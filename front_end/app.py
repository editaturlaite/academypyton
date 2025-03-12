from flask import Flask,render_template

app = Flask(__name__) # pasakome, kad cia bus pagrindinis musu programos failas
 
@app.route("/") # endpointas - tai taskas i kuri kreipiasi naudotojai (/ - tiesiog nieko)
def home():
    return "<h1>Cia yra namu puslapis</h1>"
 
@app.route("/slaptas") # endpointas - tai taskas i kuri kreipiasi naudotojai (/ - tiesiog nieko)
def slaptas():
    return "Labai slaptas puslapis"
 
if __name__ == '__main__':
    app.run(debug=True) # paleidziam flask kad veiktu ir eitu prisijungti


