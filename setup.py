from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
  name = 'termshape',         
  packages = ['termshape'],   
  version = '0.0.2',      
  license='MIT',
  description = 'Tremshape is a minimalistic Python packgage, that only prints basic shapes on terminal.',   
  long_description=long_description,
  long_description_content_type="text/markdown",  author = 'Zvi Bazak',
  author_email = 'zvibazak@gmail.com',
  url = 'https://github.com/zvibazak/termshape',
  download_url = 'https://github.com/zvibazak/termshape/archive/v_0.0.2.tar.gz',
  keywords = ['terminal', 'shape'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
