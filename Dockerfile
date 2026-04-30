FROM apache/spark:3.5.1

USER root

RUN pip install python-dotenv

ENV PATH="/opt/spark/bin:/opt/spark/sbin:${PATH}"