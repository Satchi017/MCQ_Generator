from setuptools import find_packages, setup

setup(
    name='MCQ_Generator',
    version='0.0.1',
    author='Satchidand',
    author_email='satchi017@gmail.com',
    install_requirement=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()

)