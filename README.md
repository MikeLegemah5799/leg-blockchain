
**Activate the virtual environment**

```
source blockchain-env/bin/activate
```

**Install all packages**
```
pip3 install -r requirements.txt
```

**Create virtual environment**
```
python3 -m venv blockchain-env
```

**Run Virtual environment**
```
source blockchain-env/bin/activate
```

**Run the tests**
Make sure you have the virtual environment running first.
```
python3 -m pytest backend/tests
```

**Run the application and API**
Make sure you have the virtual environment running first.
```
python3 -m backend.app
```