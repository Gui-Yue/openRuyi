# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           paddle2onnx
Version:        1.0.0
Release:        %autorelease
Summary:        PaddlePaddle to ONNX model converter library
License:        Apache-2.0
URL:            https://github.com/PaddlePaddle/Paddle2ONNX
VCS:            git:https://github.com/PaddlePaddle/Paddle2ONNX.git
# PaddlePaddle 3.3.0 uses the IsExportable C++ API that was removed from newer
# Paddle2ONNX releases, so package the latest compatible stable release.
#!RemoteAsset:  git+https://github.com/PaddlePaddle/Paddle2ONNX.git#e2885162e5a40313856d9b9415fbb8bfb41f1938
#!CreateArchive
Source0:        %{name}-%{version}.tar.gz
#!RemoteAsset:  git+https://github.com/onnx/onnx.git#5b1346e30d66e4ec550f6b63c3883b258a2e8e3e
#!CreateArchive
Source1:        submodule-onnx.tar.gz
#!RemoteAsset:  git+https://github.com/onnx/optimizer.git#a37748b2c3a80dad4274401c45c5026c7a506730
#!CreateArchive
Source2:        submodule-optimizer.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
BuildOption(conf):  -DBUILD_PADDLE2ONNX_EXE=OFF
BuildOption(conf):  -DBUILD_PADDLE2ONNX_PYTHON=OFF
BuildOption(conf):  -DBUILD_ONNX_PYTHON=OFF
BuildOption(conf):  -DONNX_BUILD_TESTS=OFF
BuildOption(conf):  -DONNX_USE_PROTOBUF_SHARED_LIBS=ON
BuildOption(conf):  -DWITH_STATIC=OFF
BuildOption(conf):  -DCMAKE_INSTALL_LIBDIR=%{_lib}

# Use system protobuf and honor the distribution library directory.
Patch0:         0001-cmake-use-system-protobuf-and-libdir.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(python3)

%description
Paddle2ONNX provides a C++ library for converting PaddlePaddle models to ONNX.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

mkdir -p third/onnx
tar -C third/onnx --strip-components=1 -xf %{SOURCE1}
# Current system protobuf/abseil headers need newer C++ language support than
# the bundled ONNX CMake default.
sed -i 's/set(CMAKE_CXX_STANDARD 11)/set(CMAKE_CXX_STANDARD 17)/' \
  third/onnx/CMakeLists.txt
# The bundled ONNX CMake lookup assumes lib/, but openRuyi uses lib64 on
# 64-bit architectures.
sed -i 's|${_PROTOBUF_INSTALL_PREFIX}/lib|${_PROTOBUF_INSTALL_PREFIX}/lib ${_PROTOBUF_INSTALL_PREFIX}/%{_lib}|g' \
  third/onnx/CMakeLists.txt

mkdir -p third/optimizer
tar -C third/optimizer --strip-components=1 -xf %{SOURCE2}

cp -p third/onnx/LICENSE LICENSE.onnx
cp -p third/optimizer/LICENSE LICENSE.optimizer

%install -a
# libpaddle2onnx links these internal shared libraries; keep them in the main
# package while dropping ONNX development files that are not part of this API.
install -p -m 0755 %{_build}/paddle2onnx/proto/libp2o_paddle_proto.so \
  %{buildroot}%{_libdir}/libp2o_paddle_proto.so
rm -rf %{buildroot}%{_includedir}/onnx
rm -rf %{buildroot}%{_libdir}/cmake/ONNX
rm -f %{buildroot}%{_libdir}/libonnxifi_dummy.so
rm -f %{buildroot}%{_libdir}/libonnxifi_loader.a
rm -f %{buildroot}%{_prefix}/lib/libonnxifi.so
rmdir %{buildroot}%{_prefix}/lib || :

%files
%license LICENSE LICENSE.onnx LICENSE.optimizer
%{_libdir}/libonnx.so
%{_libdir}/libonnx_proto.so
%{_libdir}/libp2o_paddle_proto.so
%{_libdir}/libpaddle2onnx.so.*

%files devel
%{_includedir}/paddle2onnx/
%{_libdir}/libpaddle2onnx.so

%changelog
%autochangelog
