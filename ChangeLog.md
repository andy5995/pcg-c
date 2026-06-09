(in-progress):

- Fix signed integer overflow UB in `pcg_advance_lcg_8` and
  `pcg_advance_lcg_16`: C's integer promotion rules convert `uint8_t`/`uint16_t`
  operands to signed `int` before arithmetic; large 16-bit products exceed
  `INT32_MAX`, triggering undefined behavior caught by UBSan. Cast through the
  next-wider unsigned type to keep all multiplications in unsigned arithmetic.
- When built as a Meson subproject, install nothing and skip the tests/samples.

2026-04-29

- pcg 0.94.1:
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
  - The following are upstream fixes present in the 0.94 release that were
    corrected in the upstream repository before this fork was created:
    - Fix critical typo in `entropy_getbytes`: `if (fd >= 0) return false`
      caused the function to always report failure when `/dev/urandom` opened
      successfully, making entropy collection entirely non-functional
    - Switch `entropy_getbytes` from `/dev/random` to `/dev/urandom` to avoid
      blocking on entropy-starved systems
    - Fix file descriptor leak and `int` vs `ssize_t` type mismatch in
      `entropy_getbytes`
    - Fix incorrect shift parameter in `pcg_output_xsh_rr_128_64` (`29u` →
      `35u`), which produced wrong output from 128-bit XSH RR generators
    - Rearrange `PCG_HAS_128BIT_OPS` guards in `pcg_variants.h` so the header
      compiles on platforms without `__SIZEOF_INT128__`
