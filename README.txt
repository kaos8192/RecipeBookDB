Recipe database and server written by Geir Anderson
Used class examples from Dr.Dymacek and online examples.
Online examples:
https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
https://pythonbasics.org/flask-sqlite/

===========================================================
Run the server using:

./run_server.sh

Kill server with ctrl+c.

===========================================================
Working URLs:

localhost/
-Home page

localhost/new-recipe
-Form for adding a recipe, submitting redirects to /addrec
-Adds a new recipe to the database, fills all three tables with information
!!!Ingredients and equipment must be comma separated for backend parsing to work!!!

localhost/addrec
-Confirms on successful database update
!!!Should only be opened through /new-recipe or will error!!!

localhost/recipes/
-Lists all stored recipe names, descriptions and steps.

localhost/ingredients/
-Lists all stored ingredients, with their measurements for all recipe.

localhost/ingredient/<recipe>
-Lists all ingredients and measurements for a given recipe.

localhost/equipments/
-Lists all equipment for all recipes.

localhost/equipment/<recipe>
-Lists all equipment for a given recipe.
-----------------------------------------------
===============================================
TODO:
-Add a search feature
-Cleanup listers
-Optimize database in general
-Add CSS
-Improve usability and accessibility

