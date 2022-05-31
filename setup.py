import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

try:
    with open('requirements.txt', encoding="utf-8") as fr:
        reqs = fr.read().strip().split('\n')
except:
    reqs = ["elasticsearch", "pymysql", "uvicorn[standard]", "fastapi"]


setuptools.setup(
    name="easy-searchengine",
    version="0.1.1",
    author="Joohee Cho",
    author_email="joohee2008@cau.ac.kr",
    description="Easy Search Engine for personal websites etc..",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/streetmeow/Search-engine-for-web",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=reqs,
)