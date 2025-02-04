FROM python:3.12

# install python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY ./ /app

ENTRYPOINT ["streamlit", "run", "main_auth.py", "--server.port=8080", "--server.address=0.0.0.0"]