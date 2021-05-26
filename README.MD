### Setup venv:

```shell
python3 -m venv venv
source venv/bin/activate
```

### Install requirements:

```shell
pip install -r ./requirements.txt
```

### Run app:

```shell
uvicorn app.main:app
```

### URL:

```shell
http://localhost:8000/api/contracts/generate-contract?name=validName&company=Company
```