<h1 align="center">
  <img src="https://storage.googleapis.com/tbx-web-assets-2bad228/banners/tilebox-banner.svg" alt="Tilebox Logo">
  <br>
</h1>

<div align="center">
  <a href="https://buf.build/tilebox/api">
    <img src="https://img.shields.io/badge/BSR-Module-0C65EC?style=flat-square&color=f43f5e" alt="BSR"/>
  </a>
  <a href="https://github.com/tilebox/api/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/tilebox/api.svg?style=flat-square&color=f43f5e" alt="MIT License"/>
  </a>
  <a href="https://tilebox.com/discord">
    <img src="https://img.shields.io/badge/Discord-%235865F2.svg?style=flat-square&logo=discord&logoColor=white" alt="Join us on Discord"/>
  </a>
</div>

<p align="center">
  <a href="https://docs.tilebox.com/introduction"><b>Documentation</b></a>
  |
  <a href="https://console.tilebox.com/"><b>Console</b></a>
</p>

# Tilebox API

Protocol Buffers used by [Tilebox](https://tilebox.com), a lightweight space data management and orchestration software - on ground and in orbit.

## Development

### Pre-commit hooks

We use [prek](https://prek.j178.dev/) to run linters before committing. Run the following command once to install the hooks:

```bash
uvx prek install
````

### Updating buf dependencies

```shell
buf dep update
```

## License

Distributed under the MIT License (`The MIT License`).
