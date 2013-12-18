from setuptools import setup, find_packages
import os

version = '0.1.1'

setup(
    name='wn-client',
    version=version,
    description='Talk to wn framework over HTTP',
    author='Pratik Vyas',
    author_email='pdvyas@erpnext.com',
	download_url='https://github.com/webnotes/wn-client/archive/'+version+'.tar.gz',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read().split(),
)
