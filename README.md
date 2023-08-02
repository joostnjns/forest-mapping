# To do
- Extracting 'ground truth' from forest type using source: https://maps.elie.ucl.ac.be/lifewatch/ecotopes.html?lang=en
- Further preprocessing of sentinel1 or 2
- Test segment everything
- Data fusion sentinel 1 and 2
- Supervised classification of segments, potentially taking into account time-related information (imagery as timeseries)

# forest-mapping

[![Release](https://img.shields.io/github/v/release/joostnjns/forest-mapping)](https://img.shields.io/github/v/release/joostnjns/forest-mapping)
[![Build status](https://img.shields.io/github/actions/workflow/status/joostnjns/forest-mapping/main.yml?branch=main)](https://github.com/joostnjns/forest-mapping/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/joostnjns/forest-mapping/branch/main/graph/badge.svg)](https://codecov.io/gh/joostnjns/forest-mapping)
[![Commit activity](https://img.shields.io/github/commit-activity/m/joostnjns/forest-mapping)](https://img.shields.io/github/commit-activity/m/joostnjns/forest-mapping)
[![License](https://img.shields.io/github/license/joostnjns/forest-mapping)](https://img.shields.io/github/license/joostnjns/forest-mapping)

Repository to map forest types based on open-source satellite data.

- **Github repository**: <https://github.com/joostnjns/forest-mapping/>
- **Documentation** <https://joostnjns.github.io/forest-mapping/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

``` bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:joostnjns/forest-mapping.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with 

```bash
make install
```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see
[here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see
[here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Releasing a new version



---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
