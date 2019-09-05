import subprocess as sp

end = """

Done. What to do next?

- cd {{ cookiecutter.slug }}
- git init
- make init
- Add encypted $PYPI_USERNAME and $PYPI_PASSWORD to .travis.yml
- git commit -m "initial commit"

"""

if __name__ == "__main__":
    print(end)
