from flask import Flask, jsonify, request  
from products import products

app = Flask(__name__)

from products import products

@app.route("/ping") #Ruta http 
def ping():
    return jsonify({"message": "pong"})

@app.route("/products", methods=["GET"])
def getProducts():
    return jsonify({"products": products , "messsage": "Product's List"})

@app.route("/products/<string:product_name>")
def getProduct(product_name):
    productsfound = [product for product in products if product["name"] == product_name]
    if (len(productsfound)> 0 ):
        return jsonify({"product": productsfound[0]})
    return jsonify({"message": "Product not found"})

@app.route("/products", methods=["POST"])
def addproduct():
    new_product = {
        "name": request.json["name"], 
        "price": request.json["price"],
        "quantify": request.json["quantify"]
    }
    products.append(new_product)
    return jsonify({"message": "Product added Succesfully", "products": products })

@app.route("/products/<string:product_name>", methods=["PUT"])
def editproducts(product_name):
    productfound = [product for product in products if product["name"] == product_name]
    if (len(productfound) > 0):
        productfound[0]["name"] = request.json["name"]
        productfound[0]["price"] = request.json["price"]
        productfound[0]["quantify"]= request.json["quantify"]
        return jsonify({
            "message": "Product update",
            "product": productfound[0]
        })
    return jsonify({"message": "Product not found"})

@app.route("/products/<string:product_name>", methods=["DELETE"])
def deleteproduct(product_name):
    productsfound = [product for product in products if product["name"] == product_name]
    if len(productsfound) > 0:
        products.remove(productsfound[0])
        return jsonify({
            "Message": "Product remove",
            "Products": products
        }) 
    return jsonify({"message": "Product not found"})


if __name__ == "__main__":
    app.run(debug=True, port=4000) 