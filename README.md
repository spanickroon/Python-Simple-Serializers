# Python-Simple-Serializers

Python object serializer that works in 4 formats:
- json
- pickle
- yaml
- toml

---

## Installation

1. Git clone current repository
   ```bash
    git clone https://github.com/spanickroon/Python-Simple-Serializers.git
    ```
2. Go to project
    ```bash
    cd Python-Simple-Serializers
    ```
3. Create and activate a virtual environment
   ```bash
    python3 -m venv .venv && . .venv/bin/activate
    ```
4. Run command
    ```bash
    pip install -r requirements.txt
    ```
5. Run command
    ```bash
    chmod +x startapp.py
    ```
6. Check functionality
    ```bash
    ./startapp.py --help
    ```
---

## Testing

1. Run tests
    ```bash
    coverage run -m unittest
    ```

2. Check coverage
    ```bash
    coverage report
    ```

## Build and publish to pypi

1. Build package
    ```bash
    python3 -m build
    ```
   
2. Publish package
    ```bash
    python3 -m twine upload --repository pypi dist/*
    ```
   
---
