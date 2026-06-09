if get_option('build_samples')
    sample_names = ['pcg32-demo', 'pcg32-global-demo', 'pcg32x2-demo']
    if has_128bit
        sample_names += ['pcg64-demo']
    endif

    extras_inc = include_directories('../extras')

    foreach name : sample_names
        exe = executable(
            name,
            [name + '.c', '../extras/entropy.c'],
            include_directories: extras_inc,
            dependencies: pcg_dep,
        )
        test(name, exe)
    endforeach
endif
