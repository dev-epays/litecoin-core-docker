FROM python:3.12.0b1-slim

ENV CORE_VERSION=0.21.2.1
ENV CORE_NAME="litecoin"

RUN useradd -m ${CORE_NAME} && apt-get update -y && apt-get install curl gnupg -y
ENV CORE_URL=https://download.litecoin.org/litecoin-${CORE_VERSION}/linux/litecoin-${CORE_VERSION}-x86_64-linux-gnu.tar.gz

RUN curl -SLO ${CORE_URL} \
  && tar --strip=2 -xzf *.tar.gz -C /usr/local/bin \
  && rm *.tar.gz

COPY env_core_starter.py /env_core_starter.py
USER ${CORE_NAME}

EXPOSE 9332 9333 19332 19333 19444
CMD python3 env_core_starter.py