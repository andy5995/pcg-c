project(
    'pcg-c',
    'c',
    version: '0.94.1',
    meson_version: '>= 0.56.0',
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

pcg_lib = library(
    meson.project_name(),
    files(
        'src/pcg-advance-128.c',
        'src/pcg-advance-16.c',
        'src/pcg-advance-32.c',
        'src/pcg-advance-64.c',
        'src/pcg-advance-8.c',
        'src/pcg-global-32.c',
        'src/pcg-global-64.c',
        'src/pcg-output-128.c',
        'src/pcg-output-16.c',
        'src/pcg-output-32.c',
        'src/pcg-output-64.c',
        'src/pcg-output-8.c',
        'src/pcg-rngs-128.c',
        'src/pcg-rngs-16.c',
        'src/pcg-rngs-32.c',
        'src/pcg-rngs-64.c',
        'src/pcg-rngs-8.c',
    ),
    include_directories: pcg_inc,
    version: meson.project_version(),
    soversion: 0,
    install: true,
)

install_headers('include/pcg_variants.h')

pcg_dep = declare_dependency(
    link_with: pcg_lib,
    include_directories: pcg_inc,
)

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
doc_files = ['README.md']
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

if get_option('build_tests')
    subdir('test-high')
    subdir('test-low')
endif
