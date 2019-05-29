# [Panda3D Engine Documentation](https://panda3d.readthedocs.io)

This repository contains a work-in-progress conversion from the old Mediawiki format to a new Sphinx-based site. This should make it much easier for people to contribute to the documentation, and will also allow us to have the manual and API reference in one place.

Since this new format is still quite rough around the edges, Panda3D's main website will still be linking to the old manual.

## Todo List
- [x] Base conversion utilizing [the panda-sphinx repository](https://github.com/Moguri/panda-sphinx)
- [ ] Manual fixes for formatting issues
- [ ] Welcome page (index.rst)
- [ ] Move API Reference from Doxygen to Sphinx
- [ ] Spellcheck/proofread

## Building The Documentation
```
pip3 install -r requirements.txt
python3 -m sphinx ./source ./build
```
