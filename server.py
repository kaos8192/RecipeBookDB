#A basic flask server connected to a DB
from flask import Flask, render_template, request, redirect, g
import sqlite3 as sql

databaseat = "database/recipes.db"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search-recipe")
def search_recipe():
    return TEST

@app.route("/found-recipe/<recipe>")
def found_recipe(recipe):
    return TEST

@app.route("/search-ingredient")
def search_ingredient():
    return TEST

@app.route("/found-ingredient/<ingredient>")
def found_ingredient(ingredient):
    return TEST

@app.route("/search-equipment")
def search_equipment():
    return TEST

@app.route("/found-equipment/<equipment>")
def found_equipment(equipment):
    return TEST

@app.route("/new-recipe")
def new_recipe():
    return render_template("addrecipe.html")

@app.route("/addrec",methods = ["POST","GET"])
def addrec():
    if request.method=="POST":
        try:
            name=request.form["name"]
            desc=request.form["desc"]
            ingre=request.form["ingre"]
            equip=request.form["equip"]
            steps=request.form["steps"]

            with sql.connect(databaseat) as con:
                cur=con.cursor()
                cur.execute("INSERT INTO Recipes (name, info, steps)\
                        VALUES (?,?,?)",(name,desc,steps))
                eqarr = equip.split(',')
                inarr = ingre.split(',')
                for epm in eqarr:
                    cur.execute("INSERT INTO Equipment (rname,\
                            equipment) VALUES (?,?)",(name,epm))
                for ing in inarr:
                    cur.execute("INSERT INTO Ingredients (rname,\
                            ingredient) VALUES (?,?)",(name,ing))
                con.commit()
                msg="Recipe noted!"
        except:
            con.rollback()
            msg = "ERROR INSERTION!!!"

        finally:
            return render_template("confirmation.html",msg=msg)
            con.close()
            #return ingre

@app.route("/recipes/")
def recipes():
    rec = sql.connect(databaseat)

    rec.row_factory = sql.Row #Return as dictionary and not a tuple

    cur = rec.cursor()
    cur.execute("SELECT * FROM Recipes;")

    rows = cur.fetchall()

    return render_template("recipes.html", rows=rows)

@app.route("/ingredient/", defaults={"ingredient":"Rice"})
@app.route("/ingredient/<recipe>")

def ingredient(recipe):
    ing = sql.connect(databaseat)

    ing.row_factory = sql.Row #Return as dictionary and not a tuple

    cur = ing.cursor()

    par = (recipe,) #This line is actually complete for this case
    cur.execute("SELECT ingredient FROM Ingredients WHERE rname=?;",par)

    rows = cur.fetchall()

    return render_template("ingredients.html", rows=rows)

@app.route("/ingredients/")

def ingredients():
    ing = sql.connect(databaseat)

    ing.row_factory = sql.Row #Return as dictionary and not a tuple

    cur = ing.cursor()
    cur.execute("SELECT * FROM Ingredients;")

    rows = cur.fetchall()

    return render_template("ingredients.html", rows=rows)

@app.route("/equipment/", defaults={"equipment":"Blender"})
@app.route("/equipment/<recipe>")

def equipment(recipe):
    equip = sql.connect(databaseat)

    equip.row_factory = sql.Row #Return as dictionary and not a tuple

    cur = equip.cursor()

    par = (recipe,) #This line is actually complete for this case
    cur.execute("SELECT equipment FROM Equipment WHERE rname=?;",par)

    rows = cur.fetchall()

    return render_template("equipment.html", rows=rows)

@app.route("/equipments/")

def equipments():
    equip = sql.connect(databaseat)

    equip.row_factory = sql.Row #Return as dictionary and not a tuple

    cur = equip.cursor()
    cur.execute("SELECT * FROM Equipment;")

    rows = cur.fetchall()

    return render_template("equipment.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
