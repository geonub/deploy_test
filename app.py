version: 0.2

phases:
  install:
    runtime-versions:
      python: 3.11
    commands:
      - pip install --upgrade pip
  build:
    commands:
      - pip install -r requirements.txt
artifacts:
  files:
    - app.py
    - requirements.txt
  base-directory: .