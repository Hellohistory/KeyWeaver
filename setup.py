import os
from cx_Freeze import setup, Executable

VERSION = os.environ.get('CI_VERSION', '0.0.0')

base = "Win32GUI"
icon_path = "logo.ico"

main_script = "main.py"
executable_name = "KeyWeaver"

include_files = [
    'logo.png',
    'logo.ico',
]

packages = ["PyQt5", "fastapi", "uvicorn", "zxcvbn", "pyperclip", "asyncio"]

build_exe_options = {
    "packages": packages,
    "include_files": include_files,

    "excludes": [
        "PyQt5.QtQml",
        "PyQt5.QtQuick",
        "PyQt5.QtSql",
        "PyQt5.QtWebEngineCore",
        "PyQt5.QtWebEngine",
        "PyQt5.QtWebEngineWidgets",
    ],
}

setup(
    name="KeyWeaver",
    version=VERSION,
    description="A powerful password generator and strength checker.",
    options={
        "build_exe": build_exe_options,
    },
    executables=[
        Executable(
            main_script,
            base=base,
            target_name=executable_name,
            icon=icon_path
        )
    ]
)