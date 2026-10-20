# Assignment 2: Sample package and Git workflow

## Aim
Create a sample package, host it in a Git repository, check out a file,
modify it, and push the changes again.

## Package
`foss-geometry-toolkit` is a Python package that performs 2D geometric
calculations (rectangle and circle dimensions). It requires Python 3.9
or later and has no third-party runtime dependencies.

Run the example from this directory:

```sh
python3 example.py
```

Optional installation in a virtual environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install .
```

To run unit tests:

```sh
python3 -m unittest discover -s tests
```

## Repository
- Hosting service: GitHub (Git is the version-control system).
- Repository: https://github.com/<your-username>/<your-repo-name>
- Branch: `assignment-2-geometry-package`
- Package directory: `Semester 5/Free Open Source Software/Assignment-2`

The initial commit provides rectangle area and perimeter calculations (version 0.1.0).
The second commit adds circle area and circumference computations (version 0.2.0)
after checking out the source file from HEAD.

## Git procedure performed

A separate branch or worktree was created from `origin/main` to preserve unrelated local
changes. The following commands show the two-stage workflow (paths are relative
to the repository root):

```sh
git fetch origin main
git worktree add -b assignment-2-geometry-package /tmp/foss-assignment-2-worktree origin/main
cd /tmp/foss-assignment-2-worktree

# Set assignment directory path shortcut
P="Semester 5/Free Open Source Software/Assignment-2"

# 1. Create initial package files (v0.1.0 with rectangle computations)
git add -- "$P"
git commit -m "Add sample Python geometry calculation package"
git push -u origin assignment-2-geometry-package

# 2. Check out the tracked file from HEAD before editing it
git checkout HEAD -- "$P/geometry_toolkit/calculator.py"

# 3. Add circle_area and circle_perimeter, update exports in __init__.py,
# update example.py, and change package version from 0.1.0 to 0.2.0.
git diff -- "$P"
git diff --check
git add -- "$P"
git commit -m "Add circle geometry computations after file checkout"
git push origin assignment-2-geometry-package
```

`git checkout HEAD -- <file>` restores that file from the current commit;
it does not lock it. Run it before making edits you want to keep.

## Expected output

```text
Rectangle (Length: 5, Width: 3): Area = 15.0, Perimeter = 16.0
Circle (Radius: 7): Area = 153.94, Circumference = 43.98
```

## Inspect the history

```sh
git log --oneline -2 assignment-2-geometry-package
git diff assignment-2-geometry-package~1 assignment-2-geometry-package -- "Semester 5/Free Open Source Software/Assignment-2"
```

The initial package commit is `[initial-commit-hash]` (e.g., `313a073`). The next commit
contains the checked-out file's modification, version bump to `0.2.0`, and the updated usage example.
