import os
import subprocess
from datetime import (
    datetime,
    timezone,
)

import gradio as gr

ROOP_PYTHON_PATH = "/home/python/roop/.venv/bin/python"
ROOP_SCRIPT_PATH = "/home/python/roop/run.py"


def greet(video_path: str, image_path: str) -> str:
    output_path = generate_output_path(video_path)
    process_args = (
        ROOP_PYTHON_PATH, ROOP_SCRIPT_PATH, "-s", image_path, "-t", video_path, "-o", output_path,
        "--execution-provider", "cuda", "--frame-processor", "face_swapper", "face_enhancer"
    )

    subprocess.run(process_args)

    return output_path


def generate_output_path(input_path: str) -> str:
    filename, extension = os.path.splitext(input_path)
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

    return f"{filename} {now_str}{extension}"


demo = gr.Interface(greet, ["video", gr.Image(type="filepath")], "video")

demo.launch()
