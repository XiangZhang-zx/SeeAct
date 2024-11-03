from setuptools import setup, find_packages

setup(
    name="seeact",
    version="0.2.8.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.20.0",
        "pandas>=2.2.2",
        "protobuf>=4.25.3",
        "pydantic>=2.7.0",
        "Pympler>=1.0.1",
        "click>=8.1.7",
        "ollama",
        "fastapi",
        "uvicorn",
        "torch",
        "transformers",
        "accelerate",
        "anthropic",
        "python-dotenv",
        "litellm",
        "requests",
        "backoff",
        # 添加其他依赖
    ],
    author="XXXXX",
    author_email="XXXX@example.com",
    description="SeeAct: A tool for action execution",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/XiangZhang-zx/SeeAct",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)