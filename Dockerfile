FROM python:3.6-alpine
ADD ./notifier /notifier
WORKDIR /
RUN pip install flask gunicorn
EXPOSE 5000
#CMD ["gunicorn", "-b", "0.0.0.0:5000", "\"notifier:create_app()\""]
#CMD [ "ls" ]
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:5000 \"notifier:create_app()\""]