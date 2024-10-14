from flask import Flask,request,jsonify
from routes.movies import movies_bp
app=Flask(__name__)
app.register_blueprint(movies_bp,url_prefix="/movies")

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error":"Resource not found"}),404

if __name__=="__main__":
    app.run(debug=True,port=3000)