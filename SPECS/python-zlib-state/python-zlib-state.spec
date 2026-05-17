# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zlib-state
%global pypi_name zlib_state

Name:           python-%{srcname}
Version:        0.1.12
Release:        %autorelease
Summary:        Low-level interface for capturing zlib decoding state
License:        MIT
URL:            https://github.com/seanmacavaney/zlib-state
VCS:            git:https://github.com/seanmacavaney/zlib-state
#!RemoteAsset:  sha256:ccbb06321daf165b022aa4d22d62effb7df76f55035d50bbe8b93696db416cf0
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} -l _%{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  zlib-devel

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
zlib-state exposes a low-level interface for capturing zlib decoding state.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
