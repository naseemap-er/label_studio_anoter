from distutils.core import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='label_studio_anoter',
    version='1.0',
    description='Python SharePoint API for folder or file operations (download, upload, delete)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Naseem AP',
    author_email='naseemalassampattil@gmail.com',
    url="https://github.com/naseemap-er/label_studio_anoter",
    download_url="https://github.com/naseemap-er/label_studio_anoter/archive/refs/tags/v1.0.tar.gz",
    packages=['label_studio_anoter'],
    license='MIT',
    keywords=['label_studio', 'label_studio_anoter', 'label_studio_yolo', 'yolo', 'pre_annotation', 'label_studio_pre_annotation'],
    install_requires=[
        'label-studio-sdk>=2.0.16',
        'ultralytics>=8.3.248',
        'Pillow>=12.1.0',
        'tqdm>=4.67.1',
        'requests>=2.32.5'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
    ],
)