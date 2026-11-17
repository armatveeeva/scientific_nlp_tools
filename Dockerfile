FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN pip install --no-cache-dir .

CMD ["python", "-c", "import scientific_nlp_tools; print('scientific-nlp-tools ready')"]