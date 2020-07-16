FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python3 sudo nano vim python3-pip

RUN useradd -m accubits
RUN chown -R accubits:accubits /home/accubits/

COPY --chown=accubits . /home/accubits/ivr/

USER accubits
WORKDIR /home/accubits/ivr
ENV PATH "$PATH:/home/accubits/.local/bin"

RUN echo $PATH
RUN chmod +rwx ./engine_start.sh
RUN cd /home/accubits/ivr/ && \
    python3 -m pip install --upgrade pip && \
    pip3 install -r requirements.txt

EXPOSE 5056 5055
ENTRYPOINT ["./engine_start.sh"]


