from setuptools import setup, find_packages

with open('README.md', encoding='utf8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='kbengine_tips',
    version='1.2.0',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={
        ".": ["*.MD"],
    },
    url='https://github.com/jackylvm/kbengine_tips',
    license='GPL 3.0',
    author='jacky',
    author_email='jackylvm@foxmail.com',
    description='KBEngine编码提示',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown'
)
