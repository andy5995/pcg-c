(in-progress):
  - Replace Makefiles with Meson build system with support for building and
    installing the shared library, pkg-config file, headers, and documentation
  - Meson test integration for both high-level (`test-high`) and low-level
    (`test-low`) test suites, with automatic skipping of 128-bit tests on
    platforms that lack `__uint128_t`
  - Use `PRIx64` instead of `%llx` for portable `uint64_t` format strings
    ([upstream PR #28](https://github.com/imneme/pcg-c/pull/28))
  - Fix MSVC warnings: suppress C4146 (intentional unsigned negation) in
    `pcg_variants.h` via pragma push/pop; cast narrowing shift in
    `pcg_output_xsh_rr_64_32` (C4244); replace non-portable `#warning` in
    `pcg_spinlock.h` with `#pragma message` under MSVC
