# Emake

Emake is an easy wrapper around CMake's CLI. It is meant to speed up the process
of configuring and building a CMake-based project from the command line. It
provides a user experience that smells vaguely like Autotools.

## Install

Emake is not in the Python Package Index at this time. To install Emake, build
it manually using the `build` module, or just install the directory directly
with Pip.

## Tutorial

> A small tour of Emake is offered below; see `emake -h` and `econf -h` for comprehensive help.

In most cases, all you need to do to configure and build a project is simply run
`emake` by itself:

```sh
emake		# Configure project (if needed), then build
```

> For simple projects, this will work 99% of the time.

If you wish to build a specific target, you may specify its name:

```sh
emake test	# Configure project (if needed), then build the `test` target
```

Sometimes you'll need to pass more arguments to CMake's configure step, as is
usual with larger, more complex projects. A project can be configured
(without building) using the `econf` tool. Once again, in the most simple case,
simply run `econf` by itself:

```sh
econf		# Configure the project (if needed)
```

Additional arguments can be passed through to CMake as follows:

```sh
econf -- -DCMAKE_BUILD_TYPE=Release
```

### Settings

Configuration and build settings can also be sourced from `emake.toml` in the
current working directory.

```toml
[configure]
generator = "Ninja"
```

Running `econf` with the following `emake.toml` present will cause Ninja to be
used as the CMake generator by default. For a full sample configuration, see
[`sample.toml`](docs/sample.toml).

## License

Copyright &copy; 2022&ndash;2023 Jon Palmisciano. All rights reserved.

Use of this source code is governed by the BSD 3-Clause license; a full copy of
the license can be found in the [LICENSE.txt](LICENSE.txt) file.
