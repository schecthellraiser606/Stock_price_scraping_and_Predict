FROM continuumio/anaconda3:2019.03

RUN pip install --upgrade pip && \
    conda update conda

WORKDIR /code
EXPOSE 8888

ADD Scraping-Learning.yml /code/

CMD ["--notebook-dir=/code"]
