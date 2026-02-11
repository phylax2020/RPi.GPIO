#!/bin/bash
# 1. Quellpakete generieren
rm -rf deb_dist/ dist/ *.egg-info/ 
python3 setup.py --command-packages=stdeb.command sdist_dsc --compat 13

# 2. In den generierten Ordner wechseln
cd deb_dist/rpi-gpio-0.8.8/

# 3. Die Python-Abhängigkeiten in der Steuerdatei korrigieren (sed)
sed -i 's/\${misc:Depends}, \${python3:Depends}, //' debian/control

# 4. Das Paket final bauen
export PYBUILD_INTERPRETERS=python3
dpkg-buildpackage -rfakeroot -uc -us -b
cd ..

