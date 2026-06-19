# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname paddlepaddle

# Base package is CPU-only. ONNX Runtime integration is left as an explicit
# opt-in path for future backend work.
%bcond onnxruntime 0
# ROCm support is an explicit opt-in because the full Paddle ROCm dependency stack
# is not packaged in openRuyi yet.
%bcond rocm 0

Name:           python-%{srcname}
Version:        3.3.1
Release:        %autorelease
Summary:        Deep learning framework for machine learning
License:        Apache-2.0
URL:            https://www.paddlepaddle.org.cn/
VCS:            git:https://github.com/PaddlePaddle/Paddle
# PyPI 3.3.1 publishes wheels only (no sdist), so Source0 uses upstream tag tarball.
#!RemoteAsset:  git+https://github.com/PaddlePaddle/Paddle.git#7688495538f4d6c1893f084dd238a402e8f68ab6
#!CreateArchive
Source0:        %{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Avoid importing build-only modules during metadata generation (egg_info/dist_info).
Patch0:         0001-setup.py-short-circuit-metadata-phase-without-env_di.patch
# Replace third_party git checkout/apply flows with deterministic local patching.
Patch1:         0002-cmake-external-remove-git-checkout-from-third-party-patches.patch
# Disable x86 intrinsic include path on riscv64.
Patch2:         0003-phi-search_compute-disable-x86-intrinsics-on-riscv.patch
# Use distribution-provided protobuf, ONNX Runtime, and Paddle2ONNX.
Patch3:         0004-use-system-protobuf-onnxruntime-paddle2onnx.patch
# Use distribution-provided third-party dependencies instead of Paddle vendored
# external projects.
Patch4:         0005-use-system-third-party-dependencies.patch
# Fix system protobuf/glog integration and GCC 16 SSE macro handling.
Patch5:         0006-use-system-protobuf-glog-and-fix-sse2-restore.patch

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  patchelf
BuildRequires:  cpp-threadpool-devel
BuildRequires:  dlpack
BuildRequires:  eigen3
BuildRequires:  glog-devel
BuildRequires:  pocketfft-devel
BuildRequires:  sleef-devel
BuildRequires:  pkgconfig(gflags)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(openblas)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(pybind11-stubgen)
BuildRequires:  python3dist(numpy) >= 1.21
BuildRequires:  python3dist(protobuf) >= 3.20.2
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(safetensors) >= 0.6.0
BuildRequires:  python3dist(opt-einsum) >= 3.3
BuildRequires:  warp-ctc-devel
BuildRequires:  warp-transducer-devel
%if %{with onnxruntime}
BuildRequires:  onnxruntime-devel
BuildRequires:  paddle2onnx-devel
%endif

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
PaddlePaddle is a deep learning framework that supports model development,
training, and inference.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# GCC 15 needs fixed-width integer includes in core headers.
grep -q '^#include <cstdint>$' paddle/common/enforce.h || \
  sed -i '1i #include <cstdint>' paddle/common/enforce.h
grep -q '^#include <cstdint>$' paddle/phi/kernels/strings/unicode.h || \
  sed -i '1i #include <cstdint>' paddle/phi/kernels/strings/unicode.h
grep -q '^#include <cstdint>$' paddle/fluid/inference/api/paddle_api.h || \
  sed -i '1i #include <cstdint>' paddle/fluid/inference/api/paddle_api.h

# openRuyi riscv64 toolchain does not support -m64; strip it from upstream flags.
%ifarch riscv64
sed -i 's/[[:space:]]-m64//g' cmake/flags.cmake
%endif

# openRuyi uses lib64 on 64-bit architectures; make Paddle's OpenBLAS finder
# use the system package instead of falling back to bundled OpenBLAS.
sed -i 's|${OPENBLAS_ROOT}/lib |${OPENBLAS_ROOT}/%{_lib} ${OPENBLAS_ROOT}/lib |' cmake/cblas.cmake

# RISC-V must not enable x86 SSE denormal intrinsics path.
%ifarch riscv64
sed -i 's/!defined(PADDLE_WITH_RISCV)/!defined(__riscv)/g' paddle/phi/core/platform/denormal.cc
if ! grep -q '__riscv' paddle/phi/core/platform/denormal.cc; then
  sed -i 's/!defined(PADDLE_WITH_LOONGARCH)/!defined(PADDLE_WITH_LOONGARCH) \&\& !defined(__riscv)/' paddle/phi/core/platform/denormal.cc
fi
%endif

%build
export PY_VERSION=%{python3_version}
export PADDLE_VERSION=%{version}
export PROTOBUF_ROOT=%{_prefix}
export WITH_GPU=OFF
export WITH_MKL=OFF
export WITH_XPU=OFF
export WITH_DISTRIBUTE=OFF
export WITH_TESTING=OFF
export WITH_CPP_TEST=OFF
export WITH_SYSTEM_BLAS=ON
export WITH_SYSTEM_THIRD_PARTY=ON
export WITH_ONEDNN=OFF
export WITH_OPENVINO=OFF
export WITH_CINN=OFF
export WITH_XBYAK=OFF
export WITH_CRYPTO=OFF
%if %{with onnxruntime}
export WITH_ONNXRUNTIME=ON
export WITH_SYSTEM_ONNXRUNTIME=ON
export WITH_SYSTEM_PADDLE2ONNX=ON
%else
export WITH_ONNXRUNTIME=OFF
%endif
%if %{with rocm}
export WITH_ROCM=ON
export ROCM_PATH=%{_prefix}
%else
export WITH_ROCM=OFF
%endif
export OPENBLAS_ROOT=%{_prefix}
export CMAKE_INSTALL_PREFIX=$PWD/build/paddle-cmake-install
export SKIP_STUB_GEN=1
# riscv64 currently fails in link phase with "ld terminated with signal 11".
# Force bfd linker path and reduce linker memory pressure for huge shared libs.
%ifarch riscv64
export CFLAGS="${CFLAGS:+${CFLAGS} }-fuse-ld=bfd"
# Reduce C++ compile-time memory pressure on riscv64 workers.
export CXXFLAGS="${CXXFLAGS:+${CXXFLAGS} }-fuse-ld=bfd -fno-var-tracking-assignments"
export LDFLAGS="${LDFLAGS:+${LDFLAGS} }-fuse-ld=bfd -Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
export CMAKE_BUILD_PARALLEL_LEVEL=2
%endif
%pyproject_wheel

%install
export PY_VERSION=%{python3_version}
%pyproject_install
if [ -d %{buildroot}%{python3_sitearch}/paddle/libs ]; then
  unexpected_libs="$(find %{buildroot}%{python3_sitearch}/paddle/libs -maxdepth 1 -type f \( \
    -name 'libwarpctc.so*' -o \
    -name 'libwarprnnt.so*' -o \
    -name 'libgfortran.so*' -o \
    -name 'libquadmath.so*' -o \
    -name 'libblas.so*' -o \
    -name 'liblapack.so*' \
  \) -print)"
  if [ -n "$unexpected_libs" ]; then
    echo "ERROR: system third-party runtime libraries were copied into paddle.libs:" >&2
    echo "$unexpected_libs" >&2
    exit 1
  fi
fi
%ifarch riscv64
# Guardrail: fail fast if any x86_64 shared objects are still present.
if [ -d %{buildroot}%{python3_sitearch}/paddle/libs ]; then
  if find %{buildroot}%{python3_sitearch}/paddle/libs -maxdepth 1 -type f -name '*.so*' -exec file -L {} + | grep -q 'x86-64'; then
    echo "ERROR: x86_64 ELF detected in riscv64 package payload:" >&2
    find %{buildroot}%{python3_sitearch}/paddle/libs -maxdepth 1 -type f -name '*.so*' -exec file -L {} + | grep 'x86-64' >&2
    exit 1
  fi
fi
%endif
rm -f %{buildroot}%{python3_sitearch}/_foo*.so
%pyproject_save_files -l paddle

%check
# Skip test execution due heavy runtime and hardware-dependent test requirements.

%files -f %{pyproject_files}
%{_bindir}/paddle
%doc README.md
%license LICENSE

%changelog
%autochangelog
