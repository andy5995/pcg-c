fs = import('fs')

test_inc = include_directories('.', '../extras')

test_names = [
    'check-pcg128i',
    'check-pcg128si',
    'check-pcg16i',
    'check-pcg16si',
    'check-pcg32',
    'check-pcg32f',
    'check-pcg32-global',
    'check-pcg32i',
    'check-pcg32s',
    'check-pcg32si',
    'check-pcg32u',
    'check-pcg64',
    'check-pcg64f',
    'check-pcg64-global',
    'check-pcg64i',
    'check-pcg64s',
    'check-pcg64si',
    'check-pcg64u',
    'check-pcg8i',
    'check-pcg8si',
]

foreach name : test_names
    # Not all source files are present in every distribution (e.g. release
    # archives may omit some variants), so skip any that are missing.
    if not fs.is_file(name + '.c')
        continue
    endif
    if not has_128bit and (name.contains('128') or name.contains('pcg64'))
        continue
    endif

    exe = executable(
        name,
        [name + '.c', '../extras/entropy.c'],
        include_directories: [test_inc, pcg_inc],
        dependencies: pcg_dep,
    )

    expected = meson.current_source_dir() / 'expected' / name + '.out'
    if fs.is_file(expected)
        test(name, python, args: [check_output, exe, expected])
    else
        test(name, exe)
    endif
endforeach
