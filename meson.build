project(
    'pcg-c',
    'c',
    version: '0.94.2',
    meson_version: '>= 0.58.0',
    default_options: ['warning_level=2', 'c_std=c99'],
)

cc = meson.get_compiler('c')

if cc.get_id() != 'msvc'
    extra_flags = [
        '-fno-common',
        '-fstack-protector-strong',
        '-Wformat-security',
        '-Wshadow',
        '-Wstrict-overflow=2',
        '-Werror=strict-aliasing',
    ]
    add_project_arguments(cc.get_supported_arguments(extra_flags), language: 'c')
endif

pcg_inc = include_directories('include')

subdir('src')

# As a subproject the superproject owns installation and our tests/samples are
# irrelevant, so install nothing and skip them. A standalone build installs the
# library and builds the rest.
is_standalone = not meson.is_subproject()

# MSVC shared libraries require __declspec(dllexport) on every public symbol;
# force static on Windows to avoid that requirement. Elsewhere, library() honours
# the built-in default_library option so a superproject can request a static build.
if host_machine.system() == 'windows'
    pcg_lib = static_library(
        meson.project_name(),
        _lib_sources,
        include_directories: pcg_inc,
        install: is_standalone,
    )
else
    pcg_lib = library(
        meson.project_name(),
        _lib_sources,
        include_directories: pcg_inc,
        version: meson.project_version(),
        soversion: 0,
        install: is_standalone,
    )
endif

pcg_dep = declare_dependency(
    link_with: pcg_lib,
    include_directories: pcg_inc,
)

if is_standalone
    install_headers('include/pcg_variants.h')

    pkg = import('pkgconfig')
    pkg.generate(
        pcg_lib,
        name: meson.project_name(),
        url: 'https://github.com/andy5995/pcg-c',
        description: 'PCG Random Number Generation library for C',
        version: meson.project_version(),
        subdirs: '.',
    )

    fs = import('fs')
    doc_files = ['README.md', 'ChangeLog.md']
    # License filenames differ between the git repo and release archives, so check
    # before including to allow the same meson.build to work with both.
    foreach f : [
        'LICENSE.txt',
        'LICENSE-APACHE.txt',
        'LICENSE-MIT.txt',
        'LICENSE.spdx',
        'CONTRIBUTING.md',
    ]
        if fs.is_file(f)
            doc_files += f
        endif
    endforeach
    install_data(doc_files, install_dir: get_option('docdir'))

    has_128bit = cc.compiles(
        'typedef __uint128_t t;',
        name: '128-bit integer support',
    )

    if get_option('build_tests')
        subdir('test-high')
        subdir('test-low')
    endif

    subdir('sample')
endif
