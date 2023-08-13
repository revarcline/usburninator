# USBurninator

a [balena etcher](https://etcher.balena.io/)-style TUI for burning images

## Features

### Pending

- Figure out privilege escalation (run as sudo? run sudo inline and get password?)
- menu-style tui
  - allow arrow keys and vi-keys for navigation
- List out available storage devices (exclude all partions on drive with `/` mountpoint for safety)
  - add ability to select these from menu
- Burn a local `.iso` or `.img` file to USB
  - add feature to get from url
  - automatically decompress compressed file (i.g. `img.xz`, `iso.gz` etc.)
- add "dry run" mode that prints expected behavior to stdout

### Complete
