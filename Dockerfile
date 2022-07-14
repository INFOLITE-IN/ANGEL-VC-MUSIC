COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /app
COPY . /app/ANGEL
WORKDIR /app/ANGEL

CMD ["python3", "main.py"]
