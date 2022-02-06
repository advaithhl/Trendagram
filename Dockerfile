FROM public.ecr.aws/lambda/python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip3 install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt --target ${LAMBDA_TASK_ROOT}

# copy app
COPY app.py ${LAMBDA_TASK_ROOT}

CMD [ "app.handler" ]
