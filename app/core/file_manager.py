import os

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


def save_file(
    file,
    filename
):
    file_path = os.path.join(
        UPLOAD_DIR,
        filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:
        buffer.write(
            file.file.read()
        )

    return file_path