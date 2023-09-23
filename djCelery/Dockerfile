FROM python:3.11.4-alpine

WORKDIR /usr/src/app

# prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# ensure Python output is sent directly sent to the terminal without buffering
ENV PYTHONBUFFERED=1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

# COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# Make entrypoint.sh executable
# RUN chmod +x /usr/src/app/entrypoint.sh

# Use the correct path to entrypoint.sh in ENTRYPOINT
# ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
