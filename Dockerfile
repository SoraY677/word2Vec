FROM python:3.7.9

ARG project_dir=/projects/

ADD /requirements.txt $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt