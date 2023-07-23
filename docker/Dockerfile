FROM python:3.11.4-slim-buster

# install all packages for chromedriver
RUN apt-get update && \
    apt-get install -y xvfb gnupg wget curl unzip --no-install-recommends && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable && \
    wget -q --continue -P /chromedriver "http://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip" && \
    unzip /chromedriver/chromedriver* -d /chromedriver

# make the chromedriver executable and move it to default selenium path.
RUN chmod +x /chromedriver/chromedriver
RUN mv /chromedriver/chromedriver /usr/bin/chromedriver

COPY ./ /app/

WORKDIR /app 

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--workers", "10"]