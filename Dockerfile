FROM python:3.8-slim-buster

# install system package
RUN apt-get update \
    && apt-get install -yq \
        vim \
        wget \
        gnupg2 \
        unzip \
        ca-certificates \
        apt-transport-https \
        curl \
        xvfb \
        x11-utils \
        libglib2.0-0 \
        libnss3 \
        libgconf-2-4 \
        libfontconfig1 \
        libxrender1 \
        libxtst6 \
        libxi6 \
        procps \
    && rm -rf /var/lib/apt/lists/*

# install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -yq google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# install Chrome Driver
RUN CHROMEDRIVER_VERSION=`curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE` \
    && wget -q "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/ \
    && rm chromedriver_linux64.zip

# install Python packages
RUN pip install BeautifulSoup4
RUN pip install selenium
RUN pip install requests
RUN pip install schedule

# create working dir
RUN mkdir /app
# cpoy gacha.py to /app 
COPY gacha.py /app
# set working dir
WORKDIR /app

# setting $DISPLAY 環境變量
ENV DISPLAY=:99

# setting Xvfb
RUN Xvfb :99 -screen 0 1024x768x24 &

ENTRYPOINT ["python", "/app/gacha.py"]