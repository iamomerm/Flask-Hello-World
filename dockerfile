FROM python

RUN mkdir -p /home/app/templates

COPY requirements.txt /home/app/requirements.txt
COPY main.py /home/app/main.py
COPY index.html /home/app/templates/main.py

RUN python -m pip install -r /home/app/requirements.txt

RUN python /home/app/main.py