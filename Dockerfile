FROM python:3.6
WORKDIR .
RUN if [ -f /requirements.txt ]; then /bin/pip install -r /requirements.txt; fi
EXPOSE 5000
CMD ["python", "application.py"]