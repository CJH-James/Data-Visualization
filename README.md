# Content
- [Data-Visualization](#Data-Visualization)
- [Road map](#road-map)
- [Development](#development)


# Data-Visualization
For the big data more and more popular in these years, I want to do build an App to realize it

<br>

# Road map
- [x] Data Parse
  - [ ]  
- [ ] Data Show

# Development

### Package management (uv)
- This project manage the python package via [uv](https://github.com/astral-sh/uv), and this is the [uv tutorial](https://gist.github.com/CJH-James/9e174df8655e71fb15cfbd316c2a422d)

Sync the dev environment with uv
``` powershell
    uv python install 3.13
    uv sync
```
### Doxygen
Generate the doxygen files with this project

Guildline: [doc/Readme.md](doc/Readme.md)

### GUI (wxpython)
This project use the `wxPython` for building the GUI
But there is a little complex to install the `wxPython` on the `windows`, `Mac`, and `linux`
Please check the [wxPython offical website](https://wxpython.org/pages/downloads/) for your environment

Right now, because I am developing under the `Debian 13`
So I have to build from source
The dockerfile to generate the `wxPython` wheel under `Debian 13` is at the [third_party](third_party)

### Commit message format
```
  git config commit.template ./.gitmessage
```
