FROM python:3.11.6
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src/uni_party uni_party
CMD ["python", "-m", "uni_party.init_bot.run"]
