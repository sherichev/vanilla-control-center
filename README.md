<div align="center">
    <img src="data/icons/hicolor/scalable/apps/org.vanillaos.ControlCenter.svg" height="64">
    <h1>Vanilla OS Control Center</h1>
    <p>This utility is meant to be used in <a href="https://github.com/vanilla-os">Vanilla OS</a> 
    to manage its components (almost, apx) and drivers via ubuntu-drivers-common.</p>
    <hr />
    <a href="https://gitlocalize.com/repo/8091/whole_project?utm_source=badge"> <img src="https://gitlocalize.com/repo/8091/whole_project/badge.svg" /> </a>
    <br />
    <img src="data/screenshot.png">
</div>


## Build
### Dependencies
- build-essential
- meson
- libadwaita-1-dev
- gettext
- desktop-file-utils

### Build
```bash
meson build
ninja -C build
```

### Install
```bash
sudo ninja -C build install
```

## Run
```bash
vanilla-control-center
```
