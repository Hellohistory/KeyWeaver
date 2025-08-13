import sys
import os
from cx_Freeze import setup, Executable

VERSION = os.environ.get('CI_VERSION', '0.0.0')

if sys.platform == "darwin":
    icon_path = "logo.icns"
    base = None
elif sys.platform == "win32":
    icon_path = "logo.ico"
    base = "Win32GUI"
else:
    icon_path = None
    base = None

main_script = "main.py"
executable_name = "KeyWeaver"

include_files = [
    'logo.png',
    'logo.ico',
    'logo.icns',
    'LICENSE'
]

packages = ["PyQt5", "fastapi", "uvicorn", "zxcvbn", "pyperclip", "asyncio"]


build_exe_options = {
    "packages": packages,
    "include_files": include_files,
}

bdist_mac_options = {
    "bundle_name": executable_name,
}

setup(
    name="KeyWeaver",
    version=VERSION,
    description="A powerful password generator and strength checker.",
    options={
        "build_exe": build_exe_options,
        "bdist_mac": bdist_mac_options,
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