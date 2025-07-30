# setup.py for py2app
from setuptools import setup

APP = ['nehu_wifi_gui.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'app_icon.icns',  # Optional: add an icon file
    'plist': {
        'CFBundleName': 'NEHU WiFi Login',
        'CFBundleDisplayName': 'NEHU WiFi Login',
        'CFBundleIdentifier': 'com.nehu.wifi.login',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleInfoDictionaryVersion': '6.0',
        'CFBundleExecutable': 'NEHU WiFi Login',
        'NSHumanReadableCopyright': 'Copyright © 2025 NEHU WiFi Login',
        'NSHighResolutionCapable': True,
        'LSMinimumSystemVersion': '10.14',
        'NSRequiresAquaSystemAppearance': False,  # Support dark mode
        'NSAppleScriptEnabled': True,
        'CFBundleDocumentTypes': [],
        'NSPrincipalClass': 'NSApplication',
        'NSApplicationCategoryType': 'public.app-category.utilities',
    },
    'packages': ['selenium', 'cryptography', 'tkinter'],
    'includes': ['tkinter', 'tkinter.ttk', 'tkinter.messagebox', 'tkinter.simpledialog'],
    'excludes': ['matplotlib', 'numpy', 'scipy'],  # Exclude unused packages to reduce size
    'resources': [],
    'optimize': 2,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=[
        'selenium>=4.0.0',
        'cryptography>=3.0.0',
    ],
)