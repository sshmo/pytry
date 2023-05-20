"""pytry is a place to try python."""

from distutils.core import setup

setup(
    name="pytry",
    version="0.1",
    description="pytry is a place to try python.",
    url="https://github.com/sshmo/pytry",
    author="Shabbir Mousavi",
    author_email="nabaeazim1@gmail.com",
    license="GPLv3+",
    packages=["pytry"],
    zip_safe=False,
    install_requires=[
        "pandas>=2.0.1",
    ],
)
