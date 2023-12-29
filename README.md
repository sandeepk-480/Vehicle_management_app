<h2>Vehicle Management</h2>

- Vehicle Management System with CRUD Operations, with seperate form for add and update <br>
-  It contains Operations like add vehicle number, model, type, and description. <br>
-   All the data is shown on the homepage in a tabular format with 2 buttons update and delete according to the roles. <br>
-   It has 3 roles- <br>
Super Admin- Can perform all CRUD operations <br>
Admin- Can perform update and view <br>
User- Can view <br>

<h3>How to Use it?</h3>
<h4>follow this and, run the following commands</h4>

1) open VS Code, or any of  your code editor. <br>
2) open a new terminal. <br>
3) git clone https://github.com/sandeepk-480/Vehicle_management_app.git <br>
4) pip install -r req.txt <br>
5) cd vehicle_management_app <br>
6) python manage.py loaddata > data.json <br>
7)  python manage.py runserver <br>

Roles: <br><br>

1) Super Admin- (also superuser)<br>
username- superadmin<br>
password- admin<br>
3) Admin-<br>
username- admin<br>
password- vehicle123<br>
3) User-<br>
username- user<br>
password- vehicle123<br>




