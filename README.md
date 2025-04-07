# aiseberg-assignment

Create a virtual Environment and activate (This project is created with 3.11.5)
```
python3 -m venv venv
source venv/bin/activate

```

Install requirements.txt and run the Django Project
```
pip install -r requirements.txt
cd project
python3 manage.py runserver
```

To signup/signin - open ```http://localhost:8000/accounts/signin``` . You can signup with user/pass or signin directly with google.

Once you are logged in, on the dashboard, you will see upload button, you can upload files from there. Also, to see the uploaded files,



dashboard: ```http://localhost:8000/dashboard```

upload: ```http://localhost:8000/uploads/```

list files: ```http://localhost:8000/uploads/my-files/```

Signout: ```http://localhost:8000/accounts/logout/```
