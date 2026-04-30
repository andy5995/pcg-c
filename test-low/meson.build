fs = import('fs')
sh = find_program('sh')
has_128bit = cc.compiles(
    'typedef __uint128_t t;',
    name: '128-bit integer support',
)

test_inc = include_directories('.', '../extras')

test_names = [
    'check-mcg-128-rxs-m-64',
    'check-mcg-128-xsh-rr-64',
    'check-mcg-128-xsh-rs-64',
    'check-mcg-128-xsl-rr-64',
    'check-mcg-16-rxs-m-8',
    'check-mcg-16-xsh-rr-8',
    'check-mcg-16-xsh-rs-8',
    'check-mcg-32-rxs-m-16',
    'check-mcg-32-xsh-rr-16',
    'check-mcg-32-xsh-rs-16',
    'check-mcg-64-rxs-m-32',
    'check-mcg-64-xsh-rr-32',
    'check-mcg-64-xsh-rs-32',
    'check-mcg-64-xsl-rr-32',
    'check-oneseq-128-rxs-m-64',
    'check-oneseq-128-rxs-m-xs-128',
    'check-oneseq-128-xsh-rr-64',
    'check-oneseq-128-xsh-rs-64',
    'check-oneseq-128-xsl-rr-64',
    'check-oneseq-128-xsl-rr-rr-128',
    'check-oneseq-16-rxs-m-8',
    'check-oneseq-16-rxs-m-xs-16',
    'check-oneseq-16-xsh-rr-8',
    'check-oneseq-16-xsh-rs-8',
    'check-oneseq-32-rxs-m-16',
    'check-oneseq-32-rxs-m-xs-32',
    'check-oneseq-32-xsh-rr-16',
    'check-oneseq-32-xsh-rs-16',
    'check-oneseq-64-rxs-m-32',
    'check-oneseq-64-rxs-m-xs-64',
    'check-oneseq-64-xsh-rr-32',
    'check-oneseq-64-xsh-rs-32',
    'check-oneseq-64-xsl-rr-32',
    'check-oneseq-64-xsl-rr-rr-64',
    'check-oneseq-8-rxs-m-xs-8',
    'check-setseq-128-rxs-m-64',
    'check-setseq-128-rxs-m-xs-128',
    'check-setseq-128-xsh-rr-64',
    'check-setseq-128-xsh-rs-64',
    'check-setseq-128-xsl-rr-64',
    'check-setseq-128-xsl-rr-rr-128',
    'check-setseq-16-rxs-m-8',
    'check-setseq-16-rxs-m-xs-16',
    'check-setseq-16-xsh-rr-8',
    'check-setseq-16-xsh-rs-8',
    'check-setseq-32-rxs-m-16',
    'check-setseq-32-rxs-m-xs-32',
    'check-setseq-32-xsh-rr-16',
    'check-setseq-32-xsh-rs-16',
    'check-setseq-64-rxs-m-32',
    'check-setseq-64-rxs-m-xs-64',
    'check-setseq-64-xsh-rr-32',
    'check-setseq-64-xsh-rs-32',
    'check-setseq-64-xsl-rr-32',
    'check-setseq-64-xsl-rr-rr-64',
    'check-setseq-8-rxs-m-xs-8',
    'check-unique-128-rxs-m-64',
    'check-unique-128-rxs-m-xs-128',
    'check-unique-128-xsh-rr-64',
    'check-unique-128-xsh-rs-64',
    'check-unique-128-xsl-rr-64',
    'check-unique-128-xsl-rr-rr-128',
    'check-unique-16-rxs-m-8',
    'check-unique-16-rxs-m-xs-16',
    'check-unique-16-xsh-rr-8',
    'check-unique-16-xsh-rs-8',
    'check-unique-32-rxs-m-16',
    'check-unique-32-rxs-m-xs-32',
    'check-unique-32-xsh-rr-16',
    'check-unique-32-xsh-rs-16',
    'check-unique-64-rxs-m-32',
    'check-unique-64-rxs-m-xs-64',
    'check-unique-64-xsh-rr-32',
    'check-unique-64-xsh-rs-32',
    'check-unique-64-xsl-rr-32',
    'check-unique-64-xsl-rr-rr-64',
]

foreach name : test_names
    # Not all source files are present in every distribution (e.g. release
    # archives may omit some variants), so skip any that are missing.
    if not fs.is_file(name + '.c')
        continue
    endif
    if not has_128bit and name.contains('128')
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
        test(name, sh, args: ['-c',
            'tmp=$(mktemp) && ' + exe.full_path().replace('\\', '/') + ' > "$tmp" && diff "$tmp" ' + expected.replace('\\', '/') + '; rc=$?; rm -f "$tmp"; exit $rc'])
    else
        test(name, exe)
    endif
endforeach
