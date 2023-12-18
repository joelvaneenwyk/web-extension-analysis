FROM alpine:3.19
LABEL MAINTAINER=furkan.sayim@yandex.com
LABEL name=WebExtensionAnalysis
LABEL src="https://github.com/joelvaneenwyk/web-extension-analysis.git"
LABEL creator=Tuhinshubhra
LABEL desc="Browser Extension Analysis Framework"

RUN apk add --update --no-cache git bash

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 py3-pip \
    && ln -sf python3 /usr/bin/python

RUN git clone https://github.com/joelvaneenwyk/web-extension-analysis.git /tmp/extanalysis

WORKDIR /tmp/extanalysis

RUN python -m venv .venv \
    && echo "#!/bin/bash" > ./python3.sh \
    && echo "source /tmp/extanalysis/.venv/bin/activate" >> ./python3.sh \
    && echo "python \"\$@\"" >> ./python3.sh \
    && chmod a+x ./python3.sh

RUN ./python3.sh -m pip install -r requirements.txt

EXPOSE 13337

ENTRYPOINT ["./python3.sh", "extanalysis.py"]
