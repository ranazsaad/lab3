from flask import Blueprint,request,jsonify

movies_bp=Blueprint("movies",__name__)
movies=[]   

@movies_bp.route("/",methods=["GET"])
def get_movies():
    return jsonify(movies)

# @movies_bp.route("/<string:title>",methods=["GET"])
# def getbytitle(title):
#     movie = next((b for b in movies if b["title"] == title), None)
#     if movie is None:
#         return jsonify({"error": "movie not found"}), 404
#     return jsonify(movie)

@movies_bp.route("/<string:title>", methods=["GET"])
def get_by_title(title):
    # Find the movie by title
    movie = next((b for b in movies if b["title"].lower() == title.lower()), None)
    
    # Return 404 error if movie not found
    if movie is None:
        return jsonify({"error": "Movie not found"}), 404
    
    # Return the movie details as a JSON response
    return jsonify(movie)


@movies_bp.route("/",methods=["POST"])
def create_movie():
    movie={
        "id":len(movies)+1,
        "title":request.json.get("title"),
        "completed":request.json.get("completed",False)
    }
    movies.append(movie)
    return jsonify(movie),201


@movies_bp.route("/<int:id>",methods=["PUT"])
def update_movie(id):
    movie=next((t for t in movies if t["id"]==id),None)
    if movie is None:
        return jsonify({"error":"movie not found"}),404
    movie["title"]=request.json.get("title",movie["title"])
    movie["completed"]=request.json.get("completed",movie["completed"])
    return jsonify(movie)


@movies_bp.route("/<int:id>",methods=["DELETE"])
def delete_movie(id):
    global movies
    movies=[t for t in movies if t["id"]!=id]
    return '',204

@movies_bp.errorhandler(404)
def not_found(e):
    return jsonify({"error":"Resource not found"}),404