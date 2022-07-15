
# choose python image
FROM python:3.9-slim-buster

# working directory
WORKDIR /pe-portfolio-site

# install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy directory
COPY . .

# Run container locally on port 5000
CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000


