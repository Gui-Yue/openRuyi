# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname unlzw3

Name:           python-%{srcname}
Version:        0.2.3
Release:        %autorelease
Summary:        Pure Python decompression module for Unix compress files
License:        MIT
URL:            https://pypi.org/project/unlzw3/
# VCS: No VCS link available
#!RemoteAsset:  sha256:ede5d928c792fff9da406f20334f9739693327f448f383ae1df1774627197bbb
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools) >= 61
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
unlzw3 decompresses .Z files produced by the Unix compress utility.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
