FROM nvidia/cuda:12.3.0-runtime-ubuntu22.04

ARG USER_ID=10001
ARG USER_NAME=python
ARG USER_HOME=/home/$USER_NAME

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    GRADIO_SERVER_NAME=0.0.0.0 \
    GRADIO_SERVER_PORT=7860

RUN <<EOF
  apt-get update
  DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y python3-dev python3-venv python3-tk git build-essential ffmpeg
  adduser --uid $USER_ID --home $USER_HOME --gecos "" --disabled-password $USER_NAME
EOF

USER $USER_NAME

WORKDIR $USER_HOME

RUN <<EOF
  git clone https://github.com/s0md3v/roop
  python3 -m venv roop/.venv
  ./roop/.venv/bin/pip --no-cache-dir install -r roop/requirements.txt
EOF

ADD --chown=$USER_NAME:$USER_NAME https://huggingface.co/ezioruan/inswapper_128.onnx/resolve/main/inswapper_128.onnx ./roop/models/inswapper_128.onnx

WORKDIR $USER_HOME/app

COPY requirements.txt ./

RUN <<EOF
  python3 -m venv .venv
  ./.venv/bin/pip --no-cache-dir install -r requirements.txt
EOF

COPY . .

EXPOSE 7860

ENTRYPOINT ["./.venv/bin/python3", "main.py"]
