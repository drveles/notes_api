FROM python:3.12

WORKDIR /notes_api

COPY . ./api
RUN ls

RUN pip install --no-cache-dir --upgrade -r /notes_api/api/requirements.txt


CMD [ "fastapi", "run", "/notes_api/api/main.py"]