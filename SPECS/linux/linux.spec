# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%ifarch riscv64
#!BuildConstraint: hardware:jobs 32
%endif

%{!?_debugdir: %global _debugdir %{_prefix}/lib/debug}

%global signmodules 1
%global kver %{version}-%{release}
%global kernel_make_flags LD=ld.bfd KBUILD_BUILD_VERSION=%{release}
%global debug_package %{nil}
Name:             linux
Version:          6.17.5
Release:          %autorelease
Summary:          The Linux Kernel
License:          GPL-2.0-only
URL:              https://www.kernel.org/

#!RemoteAsset
Source0:          https://cdn.kernel.org/pub/linux/kernel/v6.x/%{name}-%{version}.tar.xz
Source1:          config.%{_arch}

BuildRequires:    gcc, bison, binutils, glibc-devel, make, perl
BuildRequires:    flex, bison
BuildRequires:    bc, cpio, dwarves, gettext, python3, rsync, tar, xz, zstd
BuildRequires:    libasm-devel
BuildRequires:    libdebuginfod-dummy-devel
BuildRequires:    ncurses-devel
BuildRequires:    libcap-devel
BuildRequires:    libssh-devel
BuildRequires:    libdw-devel
BuildRequires:    libelf-devel
BuildRequires:    zstd-devel
BuildRequires:    python3-devel
BuildRequires:    slang-devel
BuildRequires:    zlib-devel
BuildRequires:    openssl-devel
BuildRequires:    kmod
BuildRequires:    rpm-config-openruyi

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-modules%{?_isa} = %{version}-%{release}
Requires(post):   kmod
Requires(post):   kernel-install
Requires(postun): kernel-install
%description
This is a meta-package that installs the core kernel image and modules.
For a minimal boot environment, install the 'linux-core' package instead.

%package core
Summary:        The core Linux kernel image and initrd

%description core
Contains the bootable kernel image (vmlinuz) and a generic, pre-built initrd,
providing the minimal set of files needed to boot the system.

%package modules
Summary:        Kernel modules for the Linux kernel
Requires:       %{name}-core = %{version}-%{release}

%description modules
Contains all the kernel modules (.ko files) and associated metadata for
the hardware drivers and kernel features.

%package devel
Summary:          Development files for building external kernel modules
Requires:         %{name} = %{version}-%{release}
Requires:         dwarves

%description devel
This package provides the kernel headers and Makefiles necessary to build
external kernel modules against the installed kernel. The development files are
located at %{_usrsrc}/kernels/%{kver}, with symlinks provided under
%{_prefix}/lib/modules/%{kver}/ for compatibility.

%package debuginfo
Summary:          Debug information for the Linux kernel
Requires:         %{name} = %{version}-%{release}

%description debuginfo
Contains the unstripped vmlinux file for debugging the kernel. This is
essential for tools like crash or for advanced kernel debugging.

%prep
%autosetup -p1
cp %{SOURCE1} .config
echo "-%{release}" > localversion

%make_build %{kernel_make_flags} olddefconfig

%build

%make_build %{kernel_make_flags}

%install
%define modpath %{buildroot}%{_libdir}/modules/%{kver}
%define kpath %{buildroot}%{_prefix}/lib/kernel
%define ksrcpath %{buildroot}%{_usrsrc}/kernels/%{kver}
%define debugpath %{buildroot}%{_debugdir}%{_lib}/modules/%{kver}
install -d %{modpath} %{kpath} %{ksrcpath} %{debugpath}

%make_build %{kernel_make_flags} INSTALL_MOD_PATH=%{buildroot}%{_prefix} INSTALL_MOD_STRIP=1 DEPMOD=true modules_install

%make_build run-command %{kernel_make_flags} KBUILD_RUN_COMMAND="$(pwd)/scripts/package/install-extmod-build %{ksrcpath}"

ln -sf ../../../../src/kernels/%{kver} %{modpath}/build
ln -sf ../../../../src/kernels/%{kver} %{modpath}/source

install -Dm644 $(make %{kernel_make_flags} -s image_name) %{kpath}/vmlinuz-%{kver}
install -m644 vmlinux %{debugpath}/vmlinux

echo "Module signing would happen here for version %{kver}."

%post
%{_sbindir}/depmod -a %{kver}
%{_bindir}/kernel-install add %{kver} %{_prefix}/lib/kernel/vmlinuz-%{kver}

%postun
if [ $1 -eq 0 ] ; then
    %{_bindir}/kernel-install remove %{kver}
fi

%files
%license COPYING
%doc README

%files core
%{_prefix}/lib/kernel/vmlinuz-%{kver}

%files modules
%{_prefix}/lib/modules/*

%files devel
%{_usrsrc}/kernels/%{kver}/
%{_libdir}/modules/%{kver}/build
%{_libdir}/modules/%{kver}/source

%files debuginfo
%{_debugdir}%{_lib}/modules/%{kver}/vmlinux

%changelog
%{?autochangelog}
